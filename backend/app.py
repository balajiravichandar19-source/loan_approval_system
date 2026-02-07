from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = pickle.load(open("loan_model.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    
    loan = float(data["loan"])
    rate = float(data["rate"])
    time = float(data["time"])
    
    current_interest = (loan * rate * time) / 100
    
    prediction = model.predict([[loan, rate, time]])
    
    return jsonify({
        "current_interest": current_interest,
        "future_interest": float(prediction[0])
    })

if __name__ == "__main__":
    app.run(debug=True)

