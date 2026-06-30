from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import joblib
import os

app = FastAPI()

# Load the model and vectorizer from the model directory
model_path = os.path.join("model", "model.pkl")
vectorizer_path = os.path.join("model", "vectorizer.pkl")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# Retro Yellow 8-bit HTML Template
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Sentiment Analyzer</title>
    <style>
        body {
            background-color: #f6d32d; /* Retro Yellow */
            color: #000000;
            font-family: 'Courier New', Courier, monospace;
            text-align: center;
            padding: 50px;
            text-transform: uppercase;
        }
        .container {
            border: 8px solid #000;
            padding: 30px;
            max-width: 600px;
            margin: 0 auto;
            background-color: #fff;
            box-shadow: 10px 10px 0px #000;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
            text-shadow: 2px 2px #ffb300;
        }
        textarea {
            width: 90%;
            height: 100px;
            border: 4px solid #000;
            font-family: 'Courier New', Courier, monospace;
            font-size: 1.2em;
            padding: 10px;
            margin-bottom: 20px;
            resize: none;
            box-shadow: 4px 4px 0px #000;
            outline: none;
        }
        button {
            background-color: #000;
            color: #f6d32d;
            border: none;
            padding: 15px 30px;
            font-size: 1.5em;
            font-family: 'Courier New', Courier, monospace;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 4px 4px 0px #555;
            transition: transform 0.1s, box-shadow 0.1s;
        }
        button:active {
            transform: translate(4px, 4px);
            box-shadow: 0px 0px 0px #555;
        }
        #result {
            margin-top: 30px;
            font-size: 2em;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Sentiment Analyzer 3000</h1>
        <p>Insert Quarter to Play... or just type below</p>
        <textarea id="inputText" placeholder="ENTER TEXT HERE..."></textarea><br>
        <button onclick="analyzeText()">ANALYZE</button>
        <div id="result"></div>
    </div>

    <script>
        async function analyzeText() {
            const text = document.getElementById('inputText').value;
            if (!text) {
                document.getElementById('result').innerText = "ERROR: NO TEXT DETECTED";
                return;
            }
            
            document.getElementById('result').innerText = "ANALYZING...";
            
            try {
                const response = await fetch('/predict/?text=' + encodeURIComponent(text), {
                    method: 'POST'
                });
                const data = await response.json();
                document.getElementById('result').innerText = "RESULT: " + data.sentiment;
            } catch (error) {
                document.getElementById('result').innerText = "SYSTEM FAILURE";
            }
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def read_root():
    return html_content

@app.post("/predict/")
def predict(text: str):
    # Vectorize the input
    text_vec = vectorizer.transform([text])
    # Predict
    prediction = model.predict(text_vec)
    return {"sentiment": str(prediction[0])}