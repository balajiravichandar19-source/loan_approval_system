from model_loader import loan_model

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_data = [
        data['Gender'],
        data['Married'],
        data['Dependents'],
        data['Education'],
        data['Self_Employed'],
        data['ApplicantIncome'],
        data['CoapplicantIncome'],
        data['LoanAmount'],
        data['Loan_Amount_Term'],
        data['Credit_History'],
        data['Property_Area']
    ]
    result = loan_model.predict([input_data])[0]
    return jsonify({"Loan_Status": result})
