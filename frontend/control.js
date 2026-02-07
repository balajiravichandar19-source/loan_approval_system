async function calculate() {

    let loan = document.getElementById("loan").value;
    let rate = document.getElementById("rate").value;
    let time = document.getElementById("time").value;

    let response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            loan: loan,
            rate: rate,
            time: time
        })
    });

    let data = await response.json();

    document.getElementById("current").innerText =
        "Current Interest: " + data.current_interest;

    document.getElementById("future").innerText =
        "Predicted Future Interest: " + data.future_interest;
}
