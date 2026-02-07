from flask import Flask, request, jsonify
from flask_cors import CORS
from model import LoanModel

app = Flask(__name__)
CORS(app)

loan_model = LoanModel()

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    loan = float(data["loan"])
    rate = float(data["rate"])
    time = float(data["time"])

    current_interest = loan_model.calculate_current_interest(loan, rate, time)
    future_interest = loan_model.predict_future_interest(loan, rate, time)

    return jsonify({
        "current_interest": current_interest,
        "future_interest": future_interest
    })

if __name__ == "__main__":
    app.run(debug=True)
