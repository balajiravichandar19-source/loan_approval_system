function checkLoan() {
  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      Gender: 1,              // Male=1, Female=0
      Married: 1,             // Yes=1, No=0
      Dependents: 1,
      Education: 0,           // Graduate=0, Not Graduate=1
      Self_Employed: 0,       // Yes=1, No=0
      ApplicantIncome: 5000,
      CoapplicantIncome: 1500,
      LoanAmount: 150,
      Loan_Amount_Term: 360,
      Credit_History: 1,
      Property_Area: 2        // Urban=2, Semiurban=1, Rural=0
    })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("result").innerHTML =
      `Loan Status: ${data.Loan_Status}<br>
       EMI: ₹${data.Estimated_EMI}`;
  });
}