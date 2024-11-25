var ChatSocket = (function(){
    "use strict";

    var ChatSocket = function(chatPanel, board, playersPanel, socketsUrl, refereePanel, handleKickMessage, handleRefereeMessage) {
        this.chatPanel = chatPanel;
        this.board = board;
        this.playersPanel = playersPanel;
        this.socketsUrl = socketsUrl;
        this.refereePanel = refereePanel;
        this.handleKickMessage = handleKickMessage;
        this.handleRefereeMessage = handleRefereeMessage;
    };

    ChatSocket.prototype.init = function(socketKey) {
        this.socketKey = socketKey;
        this.chatSocket = new WebSocket(this.socketsUrl);

        this.chatSocket.onopen = this.onSocketOpen.bind(this);
        this.chatSocket.onmessage = this.onSocketMessage.bind(this);
        this.chatSocket.onclose = this.onSocketClose.bind(this);
    };

    ChatSocket.prototype.onSocketOpen = function() {
        console.log("socket opened!");
        this.chatSocket.send(JSON.stringify({"socket_key": this.socketKey}));
    };

    ChatSocket.prototype.onSocketClose = function() {
        var disconnectText = "*** Disconnected from server, try refreshing.";
        var message = $("<div>", {"class": "connection-message", text: disconnectText}).toHtml();
        this.chatPanel.appendChatMessage(message);
    };

    ChatSocket.prototype.onSocketMessage = function(evt) {
        var json = JSON.parse(evt.data);
        if (json["type"] === "error") {
            console.log("Got error message from socket: ", json);
            return;
        } else if (json["type"] === "goal") {
            this.board.getSquare(json["square"]["slot"]).setColors(json["square"]["colors"]);
            this.playersPanel.updateGoalCounters(this.board);
            this.board.hideSquares();
        }
        else if(json["type"] === "color") {
            if (!json["player"]["is_referee"]){
                this.playersPanel.setPlayer(json["player"]);
                this.playersPanel.updateGoalCounters(this.board);
            }
        }
        else if(json["type"] === "connection") {
            if(json["event_type"] === "connected") {
                this.refereePanel.playedJoined(json["player"]);
                if (!json["player"]["is_spectator"]  && !json["player"]["is_referee"]) {
                    this.playersPanel.setPlayer(json["player"]);
                    this.playersPanel.updateGoalCounters(this.board);
                }
            }
            else if(json["event_type"] === "disconnected") {
                this.refereePanel.playedLeft(json["player"]);
                this.playersPanel.removePlayer(json["player"]);
            }
        }
        else if(json["type"] === "kick") {
            this.handleKickMessage(json["player_uuid"]);
        }
        else if(json["type"] === "referee") {
            this.handleRefereeMessage(json["player_uuid"]);
        }
        else if(json["type"] === "new-card") {
            // TODO: remove this external dependency
            // if the card was never revealed show what the seed was in the chat anyway
            $("#bingo-chat .new-card-message .seed-hidden").text(ROOM_SETTINGS.seed).removeClass('seed-hidden').addClass('seed');
            refreshBoard();
        } else if (json["type"] === "chat") {
            // no special effects for chat, it just gets written to the panel
        } else {
            console.log("unrecognized event type: ", json);
        }
        this.chatPanel.handleEvent(json);
    };


    return ChatSocket;
})();
