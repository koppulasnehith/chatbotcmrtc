from flask import Flask, render_template, request, jsonify
from chatgui import chatbot_response
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = chatbot_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)  