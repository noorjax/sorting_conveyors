from flask import Flask, request, jsonify

app = Flask(__name__)


idCount=4


@app.route("/update-all", methods=["POST"])
def update_all():
    global idCount
    data = request.get_json()
    # should create the algorithm to manage the data and create a new response
    idCount=idCount+2 # something like this

    response = [
        {
            "newSeq": [
                {"Id": "0", "RouteId": "r3", "Priority": 25},
                {"Id": "1", "RouteId": "r8", "Priority": 1},
                {"Id": "2", "RouteId": "r9", "Priority": 12}
            ],
            "priority": [
                {"Id": "100", "Priority": 25}
            ],
            "inject": [
                {"Id": str(idCount), "RouteId": "r3", "Priority": idCount},
                {"Id": str(idCount+1), "RouteId": "r7", "Priority": (idCount+1)}
            ]
        }
    ]

    return jsonify(response), 201


@app.route("/update-current-conveyor", methods=["POST"])
def update_currentConveyor():
    data = request.get_json()
    # create a random route
    response = [
        {"Id": "0", "RouteId": "r3", "Priority": 25},
        {"Id": "1", "RouteId": "r8", "Priority": 1},
        {"Id": "2", "RouteId": "r9", "Priority": 12}
    ]
    return jsonify(response), 201


@app.route("/update-current-priority", methods=["POST"])
def update_currentPriority():
    data = request.get_json()
    # changes the priority of the agent
    response = [
        {"Id": "100", "Priority": 25}
    ]
    return jsonify(response), 201


@app.route("/inject-agents", methods=["POST"])
def inject_agents():
    data = request.get_json()
    # injects new agents to the model
    global idCount
    idCount=idCount+2
    response = [
        {"Id": str(idCount), "RouteId": "r2", "Priority": idCount},
        {"Id": str(idCount+1), "RouteId": "r2", "Priority": (idCount+1)}
    ]
    return jsonify(response), 201


if __name__ == "__main__":
    app.run(debug=True)
