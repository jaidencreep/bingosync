# Generated by Django 4.1.5 on 2023-01-09 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bingosync', '0031_auto_20200120_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_type_value',
            field=models.IntegerField(choices=[(1, 'Zelda: Ocarina of Time - Normal'), (2, 'Super Mario 64 - Normal'), (3, "Zelda: Majora's Mask - Normal"), (4, 'Super Metroid - Normal'), (5, 'Castlevania: Symphony of the Night - Normal'), (6, 'Super Mario World - Legacy SRL'), (7, 'Pokémon Red/Blue - Normal'), (8, 'Pokémon Crystal - Normal'), (9, 'Donkey Kong 64'), (10, 'Pikmin'), (11, 'Super Mario Sunshine - Normal'), (12, 'Pokémon Red/Blue - Randomizer'), (13, 'Final Fantasy 1 - Normal'), (14, 'Crash Twinsanity - Normal'), (15, 'Lufia 2 - Ancient Cave'), (16, 'LEGO Star Wars: The Video Game'), (17, "Spyro 2: Ripto's Rage - 3.1"), (18, 'Custom (Advanced) - Fixed Board'), (19, 'Pokémon Snap'), (20, 'Zelda: Ocarina of Time - Blackout'), (21, 'Zelda: Ocarina of Time - Short'), (22, 'Zelda: Ocarina of Time - Short Blackout'), (23, 'Pokémon Ruby/Sapphire'), (24, 'The Addams Family (SNES)'), (25, 'Sonic Adventure 2 - Normal'), (26, 'Dark Souls'), (27, 'Road Trip Adventure'), (28, 'Psychonauts'), (29, 'Super Mario Galaxy'), (30, 'Banjo-Tooie - Normal'), (31, 'Final Fantasy 4 - Ancient Cave'), (32, 'Zelda: Breath of the Wild - Normal'), (33, 'Sonic Adventure 2 - Hero Story'), (34, 'The Witness - Normal'), (35, 'Pikmin 2 - Normal'), (36, 'Zelda: A Link to the Past - Randomizer'), (37, 'Pokémon Platinum'), (38, 'Rayman (PS1)'), (39, 'Pokémon Crystal - Current Randomizer'), (40, 'Pokémon Emerald - Old Randomizer'), (41, 'Pokémon Crystal - Classic Randomizer'), (42, 'Sonic Adventure 2 - Dark Story'), (43, 'Sonic Adventure 2 - Long'), (44, 'Zelda: Skyward Sword'), (45, 'Super Mario Odyssey - Normal'), (46, 'Super Mario Odyssey - Long'), (47, 'Rabi-Ribi'), (48, 'Generic Bingo - Normal'), (49, 'Generic Bingo - Deluxe'), (50, 'Harry Potter and the Chamber of Secrets'), (51, 'Pokémon Emerald - Short Old Randomizer'), (52, 'Hollow Knight - Normal'), (53, 'Jade Cocoon: Story of the Tamamayu'), (54, 'Mass Effect 2'), (55, 'Zelda: A Link to the Past - Enemy Randomizer'), (56, 'Happy Wheels Level Editor'), (57, 'Secret of Mana - Normal'), (58, 'Secret of Mana - German'), (59, 'Secret of Mana - Short'), (60, 'Secret of Mana - Short German'), (61, 'Final Fantasy 1 - Randomizer Short'), (62, 'Final Fantasy 1 - Randomizer Long (Defeat Chaos)'), (63, 'Final Fantasy 4 - Free Enterprise'), (64, "Spyro 2: Ripto's Rage - 4.1"), (65, 'Yu-Gi-Oh! Forbidden Memories - Normal'), (66, "Zelda: Link's Awakening - Randomizer"), (67, 'Dark Souls 3'), (68, 'Bloodborne'), (69, 'Cuphead'), (70, 'Pokémon Black/White'), (71, 'BattleBlock Theater'), (72, 'SpongeBob SquarePants: Battle for Bikini Bottom'), (73, "Luigi's Mansion - Normal"), (74, "Luigi's Mansion: Dark Moon"), (75, "Yoku's Island Express - Vanilla"), (76, 'League of Legends ARAM'), (77, 'Legend of Mana'), (78, 'Castlevania: Aria of Sorrow'), (79, 'NieR: Automata'), (80, 'Octopath Traveler - Standard'), (81, 'Splatoon 2 - Octo Expansion'), (82, 'Pokémon Emerald - Randomizer'), (83, 'Resident Evil: HD - Randomizer'), (84, 'Wii Sports Resort - Normal'), (85, 'Wii Sports Resort - All Stamps'), (86, 'Cardfight!! Vanguard'), (87, 'Super Mario Odyssey - Short'), (88, 'Yooka-Laylee'), (89, 'Zelda: Ocarina of Time - Item Randomizer'), (90, 'Zelda: Ocarina of Time - Item Randomizer Blackout'), (91, 'DOOM (2016)'), (92, 'Pokémon HeartGold/SoulSilver - Randomizer'), (93, 'Super Mario Galaxy 2'), (94, 'Super Mario Odyssey - All Kingdoms'), (95, 'Zelda: Breath of the Wild - Short'), (96, 'Zelda: Breath of the Wild - Long'), (97, 'The Binding of Isaac: Afterbirth+ - Normal'), (98, 'Super Mario Sunshine - Tournament'), (99, 'Super Mario Sunshine - Lockout'), (100, 'Super Mario Odyssey - All Kingdoms + Post Game'), (101, 'Super Smash Bros. Brawl - All Brawl'), (102, 'Super Smash Bros. Brawl - Basic'), (103, 'Transistor'), (104, 'Sonic Adventure DX'), (105, 'New Super Mario Bros. Wii'), (106, 'Celeste - Normal'), (107, 'Paper Mario - Normal'), (108, 'Mega Man 11'), (109, 'World of Warcraft - Normal'), (110, 'Super Mario 63'), (111, "PokéPark Wii: Pikachu's Adventure"), (112, 'Super Mario Sunshine - 1v1'), (113, 'Wii Sports'), (114, 'Zelda: The Wind Waker SD - Normal'), (115, 'Dream'), (116, 'Toy Story 2 - 1.0'), (117, 'Mario Party Advance'), (118, 'Darkest Dungeon - Normal'), (119, 'Club Penguin'), (120, 'Slime Rancher - Normal'), (121, 'Slime Rancher - Lockout'), (122, 'Zelda: Breath of the Wild - Normal - JP'), (123, 'Zelda: Breath of the Wild - Short - JP'), (124, 'Zelda: Breath of the Wild - Long - JP'), (125, 'Darkest Dungeon - Lockout'), (126, 'Ittle Dew 2 - Normal'), (127, 'Super Paper Mario'), (128, 'LEGO Batman: The Video Game - Long'), (129, 'Into the Breach'), (130, 'Make a Good Mega Man Level Contest 2'), (131, 'Super Mario Sunshine - 1v1 Beta'), (132, 'LEGO Pirates of the Caribbean'), (133, 'Banjo-Dreamie'), (134, 'Chibi-Robo! Plug Into Adventure'), (135, 'Touhou Luna Nights'), (136, 'Ittle Dew 2 - Blackout/Lockout'), (137, 'Ittle Dew 2 - Expert'), (138, 'Iconoclasts'), (139, 'Zelda: Ocarina of Time - Beta Quest'), (140, 'Octopath Traveler - Story'), (141, 'Dragon Warrior Monsters'), (142, 'Kirby & The Amazing Mirror'), (143, 'Jak and Daxter: The Precursor Legacy - Normal'), (144, 'Wii Sports Resort - All Stamps Lite'), (145, 'Castlevania: Symphony of the Night - Randomizer'), (146, 'The Binding of Isaac: Afterbirth+ - Racing+'), (147, 'Terraria - 1.3 Hardmode'), (148, 'LEGO Batman: The Video Game - Normal'), (149, 'Crash Team Racing'), (150, 'The Simpsons: Hit & Run'), (151, 'Paper Mario - New'), (152, 'Super Mario 64 - Randomizer Lockout'), (153, 'Dark Devotion'), (154, 'Dark Souls 2'), (155, 'Terraria - 1.3 Pre-Hardmode'), (156, 'Wii Sports Club - All Sports Expert'), (157, 'Super Mario Maker 2 - Normal'), (158, 'Minecraft - 1.16.1'), (159, 'New Super Mario Bros. DS'), (160, 'Wii Sports Club - Golf Only'), (161, 'A Hat in Time'), (162, 'Wii Sports Series - All Sports'), (163, 'Super Metroid - Experimental'), (164, 'Super Metroid - Double Anti-Bingo'), (165, 'Final Fantasy 1 - Randomizer Winter DAB'), (166, 'Super Metroid & A Link to the Past Crossover Randomizer'), (167, "Disney's Magical Mirror Starring Mickey Mouse"), (168, 'Myst'), (169, 'Super Mario Sunshine - 2v2'), (170, 'LEGO Star Wars: The Complete Saga DS'), (171, 'Celeste - Blackout'), (172, 'Custom (Advanced) - Randomized'), (173, 'Final Fantasy 8'), (174, 'Revenge of the Bird King'), (175, 'MGS: Peace Walker'), (176, "Yoku's Island Express - Randomizer"), (177, 'Wii Sports Club - All Sports'), (178, 'Sekiro: Shadows Die Twice'), (179, 'Hollow Knight - Item Randomizer'), (180, 'Monster Rancher 2 - Normal'), (181, 'Lucah: Born of a Dream'), (182, 'Wii Play'), (183, 'Super Mario World - Normal'), (184, 'Illusion of Gaia - Randomizer'), (185, 'Pikmin 2 - All Areas Unlocked'), (186, 'Yu-Gi-Oh! Forbidden Memories - Type B'), (187, 'Custom (Advanced) - SRL v5'), (188, 'Custom (Advanced) - Isaac'), (189, 'Kingdom Hearts Final Mix - Normal'), (190, 'Pokémon Emerald - Vanilla'), (191, 'The Witness - Low%'), (192, 'Cat Quest 2'), (193, 'Sonic Adventure 2 - Nightmare'), (194, 'Jak and Daxter: The Precursor Legacy - Easy'), (195, 'Celeste - Long'), (196, 'Celeste - Normal - CN'), (197, 'Celeste - Blackout - CN'), (198, 'Hollow Knight - Normal - CN'), (199, 'Wii Party - Global Trot'), (200, 'Pokémon Sword/Shield'), (201, 'Otogi: Myth of Demons'), (202, 'Zelda: The Minish Cap Randomizer'), (203, 'Yooka-Laylee and the Impossible Lair'), (204, 'Banjo-Tooie - Short'), (205, 'Banjo-Tooie - Long'), (206, 'Need for Speed: Carbon'), (207, 'Star Wars: Knights of the Old Republic'), (208, 'Sonic R'), (209, 'Celeste - Normal - Turkish'), (210, 'MGS: Portable Ops+ - Training'), (211, 'Old School Runescape - F2P + Entrana'), (212, 'Super Mario Sunshine - Normal - JP'), (213, 'Super Mario Sunshine - 1v1 - JP'), (214, 'Xenoblade Chronicles: Future Connected'), (215, 'Hollow Knight - Item Randomizer - CN'), (216, 'Hollow Knight - Item Randomizer - Portuguese'), (217, "Spyro 2: Ripto's Rage - 4.1 No Dragon Shores"), (218, 'Kingdom Hearts II Final Mix - Original'), (219, 'Sludgelife'), (220, 'Undertale'), (221, 'Pikmin 3'), (222, 'Zelda: Twilight Princess'), (223, '102 Dalmatians: Puppies to the Rescue'), (224, 'Hollow Knight - Item Randomizer - Cursed'), (225, 'Hollow Knight - Item Randomizer - No Tiebreakers'), (226, "A Bug's Life"), (227, 'Bloodstained: Ritual of the Night Randomizer'), (228, 'Zelda: A Link to the Past - Vanilla'), (229, 'Zelda: Ocarina of Time - Item Randomizer Short'), (230, 'Pokémon Omega Ruby/Alpha Sapphire'), (231, 'Monster Rancher 2 - RNG Lite'), (232, 'Fallout: New Vegas'), (233, 'Minecraft - Most recent (1.18)'), (234, "Donald Duck: Goin' Quackers!"), (235, 'Monsters, Inc. Scare Island'), (236, 'Kingdom Hearts II Final Mix - Current'), (237, "Luigi's Mansion - All Doors Unlocked"), (238, 'Spyro: Year of the Dragon'), (239, 'Medabots AX: Rokusho'), (240, 'Pen Pen TriIcelon'), (241, 'Spelunky 2'), (242, 'NiGHTS: Into Dreams'), (243, 'The Elder Scrolls V: Skyrim'), (244, 'Jak and Daxter: The Precursor Legacy - NG+'), (245, 'Pokémon Colosseum'), (246, 'Zelda: Breath of the Wild - Normal - FR'), (247, 'Zelda: Breath of the Wild - Short - FR'), (248, 'Zelda: Breath of the Wild - Long - FR'), (249, 'Terraria - Pre-Hardmode'), (250, 'Phasmophobia'), (251, 'Monster Rancher 2 - Viewers'), (252, 'Rayman Legends'), (253, 'Smash Ultimate: World of Light'), (254, "Tony Hawk's Pro Skater 1+2"), (255, 'Riven: The Sequel to Myst'), (256, 'World of Warcraft - New Character'), (257, 'Metroid Prime - Randomizer Balanced'), (258, 'Metroid Prime - Randomizer Chaos'), (259, 'Stardew Valley - Normal'), (260, "Zelda: Link's Awakening (Switch)"), (261, 'Mario Sports Mix'), (262, 'Pokémon X and Y'), (263, 'LEGO Batman: The Video Game - Semi-Random Level Names'), (264, 'LEGO Batman: The Video Game - Semi-Random Level Numbers'), (265, 'LEGO Batman: The Video Game - Random Level Names'), (266, 'LEGO Batman: The Video Game - Random Level Numbers'), (267, 'World of Warcraft - Random Level 1'), (268, 'Halo: The Master Chief Collection - Normal'), (269, 'Runescape 3 - Clue Scroll'), (270, 'Hades'), (271, 'Minecraft - 1.8.9'), (272, 'Soul Knight'), (273, 'Escape from Tarkov'), (274, 'Hollow Knight - Cratthew'), (275, 'Super Mario Maker 2 - 2021'), (276, 'Video Games Bingo'), (277, 'Halo: The Master Chief Collection - Synergy'), (278, 'Cyberpunk 2077'), (279, 'Splatoon 2 - Hero Mode'), (280, 'Chess.com'), (281, 'SaGa Frontier (PS1)'), (282, 'Call of Duty: Warzone'), (283, 'Mario Kart 8 Deluxe'), (284, 'Crystalis - Randomizer'), (285, 'Golden Sun: The Lost Age Randomizer'), (286, 'Metroid Prime 2: Echoes - Randomizer Balanced'), (287, 'Metroid Prime 2: Echoes - Randomizer Chaos'), (288, 'New Super Mario Bros. U'), (289, 'Hollow Knight - Item Randomizer - DAB'), (290, 'Snailiad'), (291, 'Geometry Dash'), (292, 'Mario Kart: Double Dash'), (293, "Bowser's Fury - Blackout"), (294, "Bowser's Fury - Lockout"), (295, 'Super Meat Boy'), (296, 'Pokémon Crystal - 2021 Summer Tournament Randomizer'), (297, 'New Super Mario Bros. 2'), (298, "Crash Bandicoot 4: It's About Time"), (299, 'Kingdom Hearts Final Mix - Randomizer'), (300, 'Celeste - Normal - Portuguese'), (301, "Yoku's Island Express - Vanilla (Simplified)"), (302, "Yoku's Island Express - Randomizer (Simplified)"), (303, 'Octopath Traveler - Short Card v2'), (304, 'Octopath Traveler - Medium Card'), (305, 'Octopath Traveler - Long Card'), (306, 'Stardew Valley - Challenge Cup'), (307, 'Salt and Sanctuary'), (308, 'Untitled Goose Game'), (309, "Death's Door"), (310, 'Hogs of War'), (311, 'Celeste Classic - Mods'), (312, "Don't Starve Together"), (313, 'Monster Hunter World'), (314, "Zelda: Majora's Mask - Item Randomizer"), (315, "Luigi's Mansion 3"), (316, 'Fantastic Contraption'), (317, "Luigi's Mansion - All Rooms"), (318, 'Zelda: The Wind Waker SD - Randomizer'), (319, 'Doodle Champion Island Games Begin!'), (320, 'Quest for Glory 1 VGA'), (321, 'Reventure'), (322, 'Crash Twinsanity - Hoverless'), (323, 'Around the Clock at Bikini Bottom'), (324, 'Bug Fables: The Everlasting Sapling'), (325, 'Civilization V'), (326, 'Horizon Zero Dawn - Normal'), (327, 'Crash Bandicoot 2: Cortex Strikes Back'), (328, 'Crash Bandicoot 3; Warped'), (329, 'Spyro the dragon'), (330, 'Toy Story 2 - 2.0'), (331, 'Pokémon Legends: Arceus'), (332, 'Hollow Knight - Item Randomizer - JP'), (333, 'Story of Seasons: Pioneers of Olive Town - All Items'), (334, 'Metroid Fusion - Randomizer'), (335, 'Azure Dreams (PS1)'), (336, 'Monkey Island (1-3)'), (337, "No Man's Sky"), (338, 'Pokémon Crystal Clear,'), (339, 'Disneyland Adventures'), (340, 'Robot 64'), (341, 'Call of Duty: Black Ops Zombies Saga'), (342, 'Grand Theft Auto V'), (343, 'LEGO City Undercover'), (344, 'Super Mario RPG - Randomizer'), (345, 'Oceanhorn 2: Knights of the Lost Realm'), (346, 'Animal Crossing: New Horizons'), (347, 'Threads of Fate'), (348, 'Counter-Strike: Global Offensive'), (349, 'Hitman 3 - Paris'), (350, 'Hitman 3 - Sapienza'), (351, 'Hitman 3 - Hokkaido'), (352, 'Hitman 3 - Miami'), (353, 'Hitman 3 - Santa Fortuna'), (354, 'Hitman 3 - Whittleton Creek'), (355, 'Hitman 3 - Berlin'), (356, 'Hitman 3 - Chongqing'), (357, 'Hitman 3 - Mendoza'), (358, 'Horizon Zero Dawn - The Frozen Wilds')], verbose_name='Game Type'),
        ),
        migrations.AlterField(
            model_name='newcardevent',
            name='game_type_value',
            field=models.IntegerField(choices=[(1, 'Zelda: Ocarina of Time - Normal'), (2, 'Super Mario 64 - Normal'), (3, "Zelda: Majora's Mask - Normal"), (4, 'Super Metroid - Normal'), (5, 'Castlevania: Symphony of the Night - Normal'), (6, 'Super Mario World - Legacy SRL'), (7, 'Pokémon Red/Blue - Normal'), (8, 'Pokémon Crystal - Normal'), (9, 'Donkey Kong 64'), (10, 'Pikmin'), (11, 'Super Mario Sunshine - Normal'), (12, 'Pokémon Red/Blue - Randomizer'), (13, 'Final Fantasy 1 - Normal'), (14, 'Crash Twinsanity - Normal'), (15, 'Lufia 2 - Ancient Cave'), (16, 'LEGO Star Wars: The Video Game'), (17, "Spyro 2: Ripto's Rage - 3.1"), (18, 'Custom (Advanced) - Fixed Board'), (19, 'Pokémon Snap'), (20, 'Zelda: Ocarina of Time - Blackout'), (21, 'Zelda: Ocarina of Time - Short'), (22, 'Zelda: Ocarina of Time - Short Blackout'), (23, 'Pokémon Ruby/Sapphire'), (24, 'The Addams Family (SNES)'), (25, 'Sonic Adventure 2 - Normal'), (26, 'Dark Souls'), (27, 'Road Trip Adventure'), (28, 'Psychonauts'), (29, 'Super Mario Galaxy'), (30, 'Banjo-Tooie - Normal'), (31, 'Final Fantasy 4 - Ancient Cave'), (32, 'Zelda: Breath of the Wild - Normal'), (33, 'Sonic Adventure 2 - Hero Story'), (34, 'The Witness - Normal'), (35, 'Pikmin 2 - Normal'), (36, 'Zelda: A Link to the Past - Randomizer'), (37, 'Pokémon Platinum'), (38, 'Rayman (PS1)'), (39, 'Pokémon Crystal - Current Randomizer'), (40, 'Pokémon Emerald - Old Randomizer'), (41, 'Pokémon Crystal - Classic Randomizer'), (42, 'Sonic Adventure 2 - Dark Story'), (43, 'Sonic Adventure 2 - Long'), (44, 'Zelda: Skyward Sword'), (45, 'Super Mario Odyssey - Normal'), (46, 'Super Mario Odyssey - Long'), (47, 'Rabi-Ribi'), (48, 'Generic Bingo - Normal'), (49, 'Generic Bingo - Deluxe'), (50, 'Harry Potter and the Chamber of Secrets'), (51, 'Pokémon Emerald - Short Old Randomizer'), (52, 'Hollow Knight - Normal'), (53, 'Jade Cocoon: Story of the Tamamayu'), (54, 'Mass Effect 2'), (55, 'Zelda: A Link to the Past - Enemy Randomizer'), (56, 'Happy Wheels Level Editor'), (57, 'Secret of Mana - Normal'), (58, 'Secret of Mana - German'), (59, 'Secret of Mana - Short'), (60, 'Secret of Mana - Short German'), (61, 'Final Fantasy 1 - Randomizer Short'), (62, 'Final Fantasy 1 - Randomizer Long (Defeat Chaos)'), (63, 'Final Fantasy 4 - Free Enterprise'), (64, "Spyro 2: Ripto's Rage - 4.1"), (65, 'Yu-Gi-Oh! Forbidden Memories - Normal'), (66, "Zelda: Link's Awakening - Randomizer"), (67, 'Dark Souls 3'), (68, 'Bloodborne'), (69, 'Cuphead'), (70, 'Pokémon Black/White'), (71, 'BattleBlock Theater'), (72, 'SpongeBob SquarePants: Battle for Bikini Bottom'), (73, "Luigi's Mansion - Normal"), (74, "Luigi's Mansion: Dark Moon"), (75, "Yoku's Island Express - Vanilla"), (76, 'League of Legends ARAM'), (77, 'Legend of Mana'), (78, 'Castlevania: Aria of Sorrow'), (79, 'NieR: Automata'), (80, 'Octopath Traveler - Standard'), (81, 'Splatoon 2 - Octo Expansion'), (82, 'Pokémon Emerald - Randomizer'), (83, 'Resident Evil: HD - Randomizer'), (84, 'Wii Sports Resort - Normal'), (85, 'Wii Sports Resort - All Stamps'), (86, 'Cardfight!! Vanguard'), (87, 'Super Mario Odyssey - Short'), (88, 'Yooka-Laylee'), (89, 'Zelda: Ocarina of Time - Item Randomizer'), (90, 'Zelda: Ocarina of Time - Item Randomizer Blackout'), (91, 'DOOM (2016)'), (92, 'Pokémon HeartGold/SoulSilver - Randomizer'), (93, 'Super Mario Galaxy 2'), (94, 'Super Mario Odyssey - All Kingdoms'), (95, 'Zelda: Breath of the Wild - Short'), (96, 'Zelda: Breath of the Wild - Long'), (97, 'The Binding of Isaac: Afterbirth+ - Normal'), (98, 'Super Mario Sunshine - Tournament'), (99, 'Super Mario Sunshine - Lockout'), (100, 'Super Mario Odyssey - All Kingdoms + Post Game'), (101, 'Super Smash Bros. Brawl - All Brawl'), (102, 'Super Smash Bros. Brawl - Basic'), (103, 'Transistor'), (104, 'Sonic Adventure DX'), (105, 'New Super Mario Bros. Wii'), (106, 'Celeste - Normal'), (107, 'Paper Mario - Normal'), (108, 'Mega Man 11'), (109, 'World of Warcraft - Normal'), (110, 'Super Mario 63'), (111, "PokéPark Wii: Pikachu's Adventure"), (112, 'Super Mario Sunshine - 1v1'), (113, 'Wii Sports'), (114, 'Zelda: The Wind Waker SD - Normal'), (115, 'Dream'), (116, 'Toy Story 2 - 1.0'), (117, 'Mario Party Advance'), (118, 'Darkest Dungeon - Normal'), (119, 'Club Penguin'), (120, 'Slime Rancher - Normal'), (121, 'Slime Rancher - Lockout'), (122, 'Zelda: Breath of the Wild - Normal - JP'), (123, 'Zelda: Breath of the Wild - Short - JP'), (124, 'Zelda: Breath of the Wild - Long - JP'), (125, 'Darkest Dungeon - Lockout'), (126, 'Ittle Dew 2 - Normal'), (127, 'Super Paper Mario'), (128, 'LEGO Batman: The Video Game - Long'), (129, 'Into the Breach'), (130, 'Make a Good Mega Man Level Contest 2'), (131, 'Super Mario Sunshine - 1v1 Beta'), (132, 'LEGO Pirates of the Caribbean'), (133, 'Banjo-Dreamie'), (134, 'Chibi-Robo! Plug Into Adventure'), (135, 'Touhou Luna Nights'), (136, 'Ittle Dew 2 - Blackout/Lockout'), (137, 'Ittle Dew 2 - Expert'), (138, 'Iconoclasts'), (139, 'Zelda: Ocarina of Time - Beta Quest'), (140, 'Octopath Traveler - Story'), (141, 'Dragon Warrior Monsters'), (142, 'Kirby & The Amazing Mirror'), (143, 'Jak and Daxter: The Precursor Legacy - Normal'), (144, 'Wii Sports Resort - All Stamps Lite'), (145, 'Castlevania: Symphony of the Night - Randomizer'), (146, 'The Binding of Isaac: Afterbirth+ - Racing+'), (147, 'Terraria - 1.3 Hardmode'), (148, 'LEGO Batman: The Video Game - Normal'), (149, 'Crash Team Racing'), (150, 'The Simpsons: Hit & Run'), (151, 'Paper Mario - New'), (152, 'Super Mario 64 - Randomizer Lockout'), (153, 'Dark Devotion'), (154, 'Dark Souls 2'), (155, 'Terraria - 1.3 Pre-Hardmode'), (156, 'Wii Sports Club - All Sports Expert'), (157, 'Super Mario Maker 2 - Normal'), (158, 'Minecraft - 1.16.1'), (159, 'New Super Mario Bros. DS'), (160, 'Wii Sports Club - Golf Only'), (161, 'A Hat in Time'), (162, 'Wii Sports Series - All Sports'), (163, 'Super Metroid - Experimental'), (164, 'Super Metroid - Double Anti-Bingo'), (165, 'Final Fantasy 1 - Randomizer Winter DAB'), (166, 'Super Metroid & A Link to the Past Crossover Randomizer'), (167, "Disney's Magical Mirror Starring Mickey Mouse"), (168, 'Myst'), (169, 'Super Mario Sunshine - 2v2'), (170, 'LEGO Star Wars: The Complete Saga DS'), (171, 'Celeste - Blackout'), (172, 'Custom (Advanced) - Randomized'), (173, 'Final Fantasy 8'), (174, 'Revenge of the Bird King'), (175, 'MGS: Peace Walker'), (176, "Yoku's Island Express - Randomizer"), (177, 'Wii Sports Club - All Sports'), (178, 'Sekiro: Shadows Die Twice'), (179, 'Hollow Knight - Item Randomizer'), (180, 'Monster Rancher 2 - Normal'), (181, 'Lucah: Born of a Dream'), (182, 'Wii Play'), (183, 'Super Mario World - Normal'), (184, 'Illusion of Gaia - Randomizer'), (185, 'Pikmin 2 - All Areas Unlocked'), (186, 'Yu-Gi-Oh! Forbidden Memories - Type B'), (187, 'Custom (Advanced) - SRL v5'), (188, 'Custom (Advanced) - Isaac'), (189, 'Kingdom Hearts Final Mix - Normal'), (190, 'Pokémon Emerald - Vanilla'), (191, 'The Witness - Low%'), (192, 'Cat Quest 2'), (193, 'Sonic Adventure 2 - Nightmare'), (194, 'Jak and Daxter: The Precursor Legacy - Easy'), (195, 'Celeste - Long'), (196, 'Celeste - Normal - CN'), (197, 'Celeste - Blackout - CN'), (198, 'Hollow Knight - Normal - CN'), (199, 'Wii Party - Global Trot'), (200, 'Pokémon Sword/Shield'), (201, 'Otogi: Myth of Demons'), (202, 'Zelda: The Minish Cap Randomizer'), (203, 'Yooka-Laylee and the Impossible Lair'), (204, 'Banjo-Tooie - Short'), (205, 'Banjo-Tooie - Long'), (206, 'Need for Speed: Carbon'), (207, 'Star Wars: Knights of the Old Republic'), (208, 'Sonic R'), (209, 'Celeste - Normal - Turkish'), (210, 'MGS: Portable Ops+ - Training'), (211, 'Old School Runescape - F2P + Entrana'), (212, 'Super Mario Sunshine - Normal - JP'), (213, 'Super Mario Sunshine - 1v1 - JP'), (214, 'Xenoblade Chronicles: Future Connected'), (215, 'Hollow Knight - Item Randomizer - CN'), (216, 'Hollow Knight - Item Randomizer - Portuguese'), (217, "Spyro 2: Ripto's Rage - 4.1 No Dragon Shores"), (218, 'Kingdom Hearts II Final Mix - Original'), (219, 'Sludgelife'), (220, 'Undertale'), (221, 'Pikmin 3'), (222, 'Zelda: Twilight Princess'), (223, '102 Dalmatians: Puppies to the Rescue'), (224, 'Hollow Knight - Item Randomizer - Cursed'), (225, 'Hollow Knight - Item Randomizer - No Tiebreakers'), (226, "A Bug's Life"), (227, 'Bloodstained: Ritual of the Night Randomizer'), (228, 'Zelda: A Link to the Past - Vanilla'), (229, 'Zelda: Ocarina of Time - Item Randomizer Short'), (230, 'Pokémon Omega Ruby/Alpha Sapphire'), (231, 'Monster Rancher 2 - RNG Lite'), (232, 'Fallout: New Vegas'), (233, 'Minecraft - Most recent (1.18)'), (234, "Donald Duck: Goin' Quackers!"), (235, 'Monsters, Inc. Scare Island'), (236, 'Kingdom Hearts II Final Mix - Current'), (237, "Luigi's Mansion - All Doors Unlocked"), (238, 'Spyro: Year of the Dragon'), (239, 'Medabots AX: Rokusho'), (240, 'Pen Pen TriIcelon'), (241, 'Spelunky 2'), (242, 'NiGHTS: Into Dreams'), (243, 'The Elder Scrolls V: Skyrim'), (244, 'Jak and Daxter: The Precursor Legacy - NG+'), (245, 'Pokémon Colosseum'), (246, 'Zelda: Breath of the Wild - Normal - FR'), (247, 'Zelda: Breath of the Wild - Short - FR'), (248, 'Zelda: Breath of the Wild - Long - FR'), (249, 'Terraria - Pre-Hardmode'), (250, 'Phasmophobia'), (251, 'Monster Rancher 2 - Viewers'), (252, 'Rayman Legends'), (253, 'Smash Ultimate: World of Light'), (254, "Tony Hawk's Pro Skater 1+2"), (255, 'Riven: The Sequel to Myst'), (256, 'World of Warcraft - New Character'), (257, 'Metroid Prime - Randomizer Balanced'), (258, 'Metroid Prime - Randomizer Chaos'), (259, 'Stardew Valley - Normal'), (260, "Zelda: Link's Awakening (Switch)"), (261, 'Mario Sports Mix'), (262, 'Pokémon X and Y'), (263, 'LEGO Batman: The Video Game - Semi-Random Level Names'), (264, 'LEGO Batman: The Video Game - Semi-Random Level Numbers'), (265, 'LEGO Batman: The Video Game - Random Level Names'), (266, 'LEGO Batman: The Video Game - Random Level Numbers'), (267, 'World of Warcraft - Random Level 1'), (268, 'Halo: The Master Chief Collection - Normal'), (269, 'Runescape 3 - Clue Scroll'), (270, 'Hades'), (271, 'Minecraft - 1.8.9'), (272, 'Soul Knight'), (273, 'Escape from Tarkov'), (274, 'Hollow Knight - Cratthew'), (275, 'Super Mario Maker 2 - 2021'), (276, 'Video Games Bingo'), (277, 'Halo: The Master Chief Collection - Synergy'), (278, 'Cyberpunk 2077'), (279, 'Splatoon 2 - Hero Mode'), (280, 'Chess.com'), (281, 'SaGa Frontier (PS1)'), (282, 'Call of Duty: Warzone'), (283, 'Mario Kart 8 Deluxe'), (284, 'Crystalis - Randomizer'), (285, 'Golden Sun: The Lost Age Randomizer'), (286, 'Metroid Prime 2: Echoes - Randomizer Balanced'), (287, 'Metroid Prime 2: Echoes - Randomizer Chaos'), (288, 'New Super Mario Bros. U'), (289, 'Hollow Knight - Item Randomizer - DAB'), (290, 'Snailiad'), (291, 'Geometry Dash'), (292, 'Mario Kart: Double Dash'), (293, "Bowser's Fury - Blackout"), (294, "Bowser's Fury - Lockout"), (295, 'Super Meat Boy'), (296, 'Pokémon Crystal - 2021 Summer Tournament Randomizer'), (297, 'New Super Mario Bros. 2'), (298, "Crash Bandicoot 4: It's About Time"), (299, 'Kingdom Hearts Final Mix - Randomizer'), (300, 'Celeste - Normal - Portuguese'), (301, "Yoku's Island Express - Vanilla (Simplified)"), (302, "Yoku's Island Express - Randomizer (Simplified)"), (303, 'Octopath Traveler - Short Card v2'), (304, 'Octopath Traveler - Medium Card'), (305, 'Octopath Traveler - Long Card'), (306, 'Stardew Valley - Challenge Cup'), (307, 'Salt and Sanctuary'), (308, 'Untitled Goose Game'), (309, "Death's Door"), (310, 'Hogs of War'), (311, 'Celeste Classic - Mods'), (312, "Don't Starve Together"), (313, 'Monster Hunter World'), (314, "Zelda: Majora's Mask - Item Randomizer"), (315, "Luigi's Mansion 3"), (316, 'Fantastic Contraption'), (317, "Luigi's Mansion - All Rooms"), (318, 'Zelda: The Wind Waker SD - Randomizer'), (319, 'Doodle Champion Island Games Begin!'), (320, 'Quest for Glory 1 VGA'), (321, 'Reventure'), (322, 'Crash Twinsanity - Hoverless'), (323, 'Around the Clock at Bikini Bottom'), (324, 'Bug Fables: The Everlasting Sapling'), (325, 'Civilization V'), (326, 'Horizon Zero Dawn - Normal'), (327, 'Crash Bandicoot 2: Cortex Strikes Back'), (328, 'Crash Bandicoot 3; Warped'), (329, 'Spyro the dragon'), (330, 'Toy Story 2 - 2.0'), (331, 'Pokémon Legends: Arceus'), (332, 'Hollow Knight - Item Randomizer - JP'), (333, 'Story of Seasons: Pioneers of Olive Town - All Items'), (334, 'Metroid Fusion - Randomizer'), (335, 'Azure Dreams (PS1)'), (336, 'Monkey Island (1-3)'), (337, "No Man's Sky"), (338, 'Pokémon Crystal Clear,'), (339, 'Disneyland Adventures'), (340, 'Robot 64'), (341, 'Call of Duty: Black Ops Zombies Saga'), (342, 'Grand Theft Auto V'), (343, 'LEGO City Undercover'), (344, 'Super Mario RPG - Randomizer'), (345, 'Oceanhorn 2: Knights of the Lost Realm'), (346, 'Animal Crossing: New Horizons'), (347, 'Threads of Fate'), (348, 'Counter-Strike: Global Offensive'), (349, 'Hitman 3 - Paris'), (350, 'Hitman 3 - Sapienza'), (351, 'Hitman 3 - Hokkaido'), (352, 'Hitman 3 - Miami'), (353, 'Hitman 3 - Santa Fortuna'), (354, 'Hitman 3 - Whittleton Creek'), (355, 'Hitman 3 - Berlin'), (356, 'Hitman 3 - Chongqing'), (357, 'Hitman 3 - Mendoza'), (358, 'Horizon Zero Dawn - The Frozen Wilds')]),
        ),
    ]
