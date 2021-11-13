from flask import Flask,jsonify,request

app=Flask(__name__)

contacts=[
    {
        "id":1,
        "name":"Jeeya Talati",
        "profession":"student",
        "Contact Number":"9852546709"
    },
    {
        "id":1,
        "name":"Kayaan",
        "profession":"student",
        "Contact Number":"8576903452"
        
    }
]

@app.route("/")
def index():
    return jsonify({
        "status": "success",
        "message": "Hello world, I am Jeeya"
    }, 200)

@app.route("/addtask",methods=["POST"])
def addTask():
    if not request.json:
        return jsonify({
        "status": "error",
        "message": "Please provide data"
        }, 400)

    task = {
        "id": contacts[-1]['id'] + 1,
        "title": request.json["title"],
        "Description": request.json.get("Description"),
        "Done": False
    }

    contacts.append(task)
    return jsonify({
        "status": "success",
        "message": "Your task has been added."
    })


@app.route("/gettask")
def get_task():
    return jsonify({
        "data": contacts
    })


if __name__ == "__main__":
    app.run(debug=True)