from flask import Flask, jsonify,request

    #Creating flask app instance 
app = Flask(__name__)


    # jsonify() converts Python data into a proper JSON HTTP response with correct headers and formatting.
@app.route("/")
def home():
        return jsonify({
            "message":"Api is running"
        })
@app.route("/test")
def test():
        return jsonify({
            "message":"The test is working."
        })

app.route("/user")
def user():
        return jsonify({
            "name":"Sujal",
            "role":"Developer"
        })

    #fake database
notes=[]

@app.route("/notes",methods=["GET"])
def get_notes():
        return jsonify(notes)

    #import "request" from flask
@app.route("/addnote",methods=["POST"])
def add_note():
        data = request.json
        notes.append(data)
        return jsonify({"message":"Note added Successfully"}),201

    #PUT request - update the database 
@app.route("/notes/<int:index>",methods=["PUT"])
def update(index):
        data = request.json

        if(index<len(notes)):
            notes[index]=data
            return jsonify({"message":"Note updated"}),200
    
        return jsonify({"erro":"Invalid index"}),400


    #DELETE - To delete the data 
@app.route("/notes/<int:index>",methods=["DELETE"])
def delete_note(index):
        if(index<len(notes)):
            notes.pop(index)
            return jsonify({"message":"Note deleted successfully"}),200
    
        return jsonify({"error":"Ivalid Index"}),400 


    #Ensusers the flask app runs only when the file is executed directly not when imported
if __name__ == "__main__":
   app.run(debug=True)