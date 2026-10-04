const textInput = document.getElementById("textInput");
const analyzeBtn = document.getElementById("analyzeBtn");
const result = document.getElementById("result");

analyzeBtn.addEventListener("click", async function () {

    // User ka text lena
    const text = textInput.value.trim();

    // Empty input check
    if (text === "") {
        result.textContent = "Please enter some text.";
        return;
    }

    // Loading message
    result.textContent = "Analyzing...";

    try {

        // FastAPI ko request bhejna
        const response = await fetch("http://127.0.0.1:8000/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                text: text
            })
        });

        // Agar API response successful nahi hai
        if (!response.ok) {
            throw new Error("API request failed");
        }

        // FastAPI ka response lena
        const data = await response.json();

        // Result screen par show karna
        result.textContent = "Sentiment: " + data.sentiment;

    } catch (error) {

        // API/server error
        result.textContent = "Unable to connect to the server.";

    }
});