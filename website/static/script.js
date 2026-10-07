async function generatePrediction() {

    const button = document.querySelector(".predict-button");

    const patientData = {
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


    for (const key in patientData) {

        if (
            patientData[key] === "" ||
            Number.isNaN(patientData[key])
        ) {
            alert("Please fill in all fields.");
            return;
        }
    }


    button.disabled = true;
    button.innerHTML = "Analyzing...";


    try {

        const response = await fetch("/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(patientData)

        });


        const data = await response.json();


        if (!response.ok) {
            throw new Error("Prediction failed");
        }


        document.getElementById("resultTitle").textContent =
            data.result;

        document.getElementById("probability").textContent =
            data.probability;


        if (data.prediction === 1) {

            document.getElementById("resultIcon").textContent = "♥";

            document.getElementById("resultMessage").textContent =
                "The machine learning model predicts an elevated heart disease risk based on the information provided.";

        } else {

            document.getElementById("resultIcon").textContent = "✓";

            document.getElementById("resultMessage").textContent =
                "The machine learning model predicts a lower heart disease risk based on the information provided.";
        }


        document
            .getElementById("resultCard")
            .classList.remove("hidden");


        document
            .getElementById("resultCard")
            .scrollIntoView({
                behavior: "smooth",
                block: "center"
            });


    } catch (error) {

        alert(
            "Unable to connect to the prediction API."
        );

        console.error(error);

    }


    button.disabled = false;

    button.innerHTML = `
        <span>Generate Risk Assessment</span>
        <span class="button-arrow">→</span>
    `;
}


function resetPrediction() {

    document
        .getElementById("predictionForm")
        .reset();

    document
        .getElementById("resultCard")
        .classList.add("hidden");

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}