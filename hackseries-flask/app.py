import os

from flask import Flask, jsonify, request

app = Flask(__name__)
# Keep this in-memory learning API bounded against oversized request bodies.
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024


@app.errorhandler(413)
def request_too_large(_error):
    return jsonify({"error": "Request body exceeds the 16 KiB limit."}), 413


# In-memory storage is intentionally for this learning exercise only.
notes = []


@app.get("/")
def home():
    return jsonify({"message": "API is running"})


@app.get("/test")
def test():
    return jsonify({"message": "The test is working."})


@app.get("/user")
def user():
    return jsonify({"name": "Sujal", "role": "Developer"})


@app.get("/notes")
def get_notes():
    return jsonify(notes)


@app.post("/addnote")
def add_note():
    data = request.get_json(silent=True)
    if not isinstance(data, dict) or not data:
        return jsonify({"error": "Request body must be a non-empty JSON object."}), 400

    notes.append(data)
    return jsonify({"message": "Note added successfully", "note": data}), 201


@app.put("/notes/<int:index>")
def update_note(index):
    if not 0 <= index < len(notes):
        return jsonify({"error": "Invalid note index."}), 404

    data = request.get_json(silent=True)
    if not isinstance(data, dict) or not data:
        return jsonify({"error": "Request body must be a non-empty JSON object."}), 400

    notes[index] = data
    return jsonify({"message": "Note updated", "note": data}), 200


@app.delete("/notes/<int:index>")
def delete_note(index):
    if not 0 <= index < len(notes):
        return jsonify({"error": "Invalid note index."}), 404

    notes.pop(index)
    return jsonify({"message": "Note deleted successfully"}), 200


if __name__ == "__main__":
    # Enable the debugger only when explicitly requested in a local environment.
    app.run(debug=os.getenv("FLASK_DEBUG") == "1")
