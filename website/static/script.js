const form = document.getElementById("predictionForm");
const resultDiv = document.getElementById("result");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const data = {
        age: Number(document.getElementById("age").value),
        sex: Number(document.getElementById("sex").value),
        cp: Number(document.getElementById("cp").value),
        trestbps: Number(document.getElementById("trestbps").value),
        chol: Number(document.getElementById("chol").value),
        fbs: Number(document.getElementById("fbs").value),
        restecg: Number(document.getElementById("restecg").value),
        thalach: Number(document.getElementById("thalach").value),
        exang: Number(document.getElementById("exang").value),
        oldpeak: Number(document.getElementById("oldpeak").value),
        slope: Number(document.getElementById("slope").value),
        ca: Number(document.getElementById("ca").value),
        thal: Number(document.getElementById("thal").value)
    };

    resultDiv.classList.remove("hidden", "success", "danger");
    resultDiv.textContent = "Analyzing patient data...";

    try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error("Prediction request failed");
        }

        const result = await response.json();

        resultDiv.classList.remove("hidden");

        if (result.prediction === 1) {
            resultDiv.classList.add("danger");

            resultDiv.innerHTML = `
                <div>${result.result}</div>
                <div>Model Probability: ${result.probability}%</div>
            `;
        } else {
            resultDiv.classList.add("success");

            resultDiv.innerHTML = `
                <div>${result.result}</div>
                <div>Model Probability: ${result.probability}%</div>
            `;
        }

    } catch (error) {
        resultDiv.classList.remove("hidden");
        resultDiv.classList.add("danger");
        resultDiv.textContent =
            "Unable to connect to the prediction API. Please make sure the API is running.";
    }
});