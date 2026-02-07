from flask import Flask, request, jsonify
from flask_cors import CORS
from model import loan_model   # importing trained model

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    # Example input (You must match dataset features later)
    input_data = [[
        float(data["loan"]),
        float(data["rate"]),
        float(data["time"])
    ]]

    prediction = loan_model.predict(input_data)

    return jsonify({
        "prediction": int(prediction[0])
    })

if __name__ == "__main__":
    app.run(debug=True)
