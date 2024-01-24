# utility functions for handling the "custom" GameTypes
# packaged as a "Generator" to allow some generic handling

from django.utils import safestring

import json
import urllib.parse

from bingosync.generators.bingo_generator import BingoGenerator
from bingosync.models.game_type import GameType
import math


class InvalidBoardException(Exception):

    def __str__(self):
        # propagate the SafeText up to the template if that's the entire message
        if len(self.args) == 1 and isinstance(self.args[0], safestring.SafeText):
            return self.args[0]
        return super().__str__()


def _make_jsonlint_link(custom_json):
    href = 'https://jsonlint.com/?' + urllib.parse.urlencode({'json': custom_json}, quote_via=urllib.parse.quote)
    return '<a href="{}" target="_blank">jsonlint</a>'.format(href)


def _validate_square(i, square):
    if "name" not in square:
        raise InvalidBoardException(
                'Square {} ({}) is missing a "name" attribute'.format(i + 1, json.dumps(square)))
    elif square["name"] == "":
        raise InvalidBoardException(
                'Square {} ({}) has an empty "name" attribute'.format(i + 1, json.dumps(square)))


def _parse_simple_list(custom_board, game_type, size=5):
    if not isinstance(custom_board, list):
        raise InvalidBoardException('Board must be a list')
    
    if size==None:
        size = 5

    if game_type == GameType.custom and len(custom_board) != size*size:
        raise InvalidBoardException(
                'A fixed board must have exactly {} goals (found {})'.format(size*size, len(custom_board)))
    elif game_type == GameType.custom_randomized and len(custom_board) < size*size:
        raise InvalidBoardException(
                'A randomized board must have at least {} goals (found {})'.format(size*size, len(custom_board)))

    for i, square in enumerate(custom_board):
        _validate_square(i, square)

    return custom_board


def _validate_difficulty_tier(goals, tier):
    if not isinstance(goals, list):
        raise InvalidBoardException(
                'Element at difficulty tier {} was not a list (found {})'.format(tier, json.dumps(goals)))

    if not goals:
        raise InvalidBoardException(
                'Goal list at difficulty tier {} was empty'.format(tier))

    for i, goal in enumerate(goals):
        if "name" not in goal:
            raise InvalidBoardException(
                    'Goal {} ({}) in difficulty tier {} is missing a "name" attribute'
                    .format(i+1, json.dumps(goal), tier))
        if goal["name"] == "":
            raise InvalidBoardException(
                    'Goal {} ({}) in difficulty tier {} has an empty "name" attribute'
                    .format(i+1, json.dumps(goal), tier))


def _parse_srl_v5_list(custom_board, size=5):
    if size:
        provided_size = True
        size = int(size)
    else:
        provided_size = False
        size = int(math.sqrt(len(custom_board)))
    if not isinstance(custom_board, list):
        raise InvalidBoardException('Board must be a list')

    if len(custom_board) != size*size:
        if provided_size:
            raise InvalidBoardException(
                    'An SRL goal list must have exactly {} tiers (found {})'.format(size*size, len(custom_board)))
        else:
            raise InvalidBoardException(
                    'An SRL goal list must have exactly a square size (found {})'.format(len(custom_board)))

    for i, goals in enumerate(custom_board):
        _validate_difficulty_tier(goals, i+1)

    return custom_board


def _parse_isaac_list(custom_board):
    if not isinstance(custom_board, list):
        raise InvalidBoardException('Board must be a list')

    if len(custom_board) != 4:
        raise InvalidBoardException(
                'An Isaac goal list must have exactly 4 tiers (found {})'.format(len(custom_board)))

    for i, goals in enumerate(custom_board):
        _validate_difficulty_tier(goals, i+1)

    if len(custom_board[0]) < 10:
        raise InvalidBoardException(
                'An Isaac goal list must have at least 10 easy goals (found {})'.format(len(custom_board[0])))
    if len(custom_board[1]) < 10:
        raise InvalidBoardException(
                'An Isaac goal list must have at least 10 medium goals (found {})'.format(len(custom_board[1])))
    if len(custom_board[2]) < 4:
        raise InvalidBoardException(
                'An Isaac goal list must have at least 4 hard goals (found {})'.format(len(custom_board[2])))
    if len(custom_board[3]) < 1:
        raise InvalidBoardException(
                'An Isaac goal list must have at least 1 very hard goal (found {})'.format(len(custom_board[3])))

    return custom_board


class CustomGenerator:

    def __init__(self, game_type):
        if not game_type.is_custom:
            raise Exception(
                    'Tried to instantiate CustomGenerator with invalid GameType: {}'.format(game_type))
        self.game_type = game_type

    def validate_custom_json(self, custom_json, size=5):
        if size:
            size = int(size)
        try:
            custom_board = json.loads(custom_json)
        except json.decoder.JSONDecodeError as e:
            raise InvalidBoardException(safestring.mark_safe(
                'Couldn\'t parse board json, try {}'.format(_make_jsonlint_link(custom_json))))

        if self.game_type in (GameType.custom, GameType.custom_randomized):
            return _parse_simple_list(custom_board, self.game_type, size=size)
        elif self.game_type in (GameType.custom_srl_v5, GameType.custom_ccomm):
            return _parse_srl_v5_list(custom_board, size=size)
        elif self.game_type == GameType.custom_isaac:
            return _parse_isaac_list(custom_board)

        raise Exception('Unrecognized custom game type: {}'.format(self.game_type))

    def get_card(self, seed, custom_board=None, size=5):
        if self.game_type == GameType.custom:
            return seed, custom_board
        elif self.game_type in (GameType.custom_randomized, GameType.custom_srl_v5, GameType.custom_isaac, GameType.custom_ccomm):
            return BingoGenerator.instance(str(self.game_type.name)).get_card(seed, custom_board, size)

        raise Exception('Unrecognized custom game type: {}'.format(self.game_type))
