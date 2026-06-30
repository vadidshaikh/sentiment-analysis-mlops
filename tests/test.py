import joblib
import pytest

# Load your model artifacts
model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

# Define your test cases: (input_text, expected_label)
@pytest.mark.parametrize("text, expected_sentiment", [
    ("good", "positive"),    # Replace "positive" with your model's actual positive label
    ("nice", "positive"),    # Replace "positive" with your model's actual positive label
    ("bad", "negative"),     # Replace "negative" with your model's actual negative label
    ("boring", "negative")   # Replace "negative" with your model's actual negative label
])
def test_sentiment_logic(text, expected_sentiment):
    # Transform input
    vec = vectorizer.transform([text])
    
    # Predict
    pred = model.predict(vec)
    
    # Assert
    assert pred[0] == expected_sentiment