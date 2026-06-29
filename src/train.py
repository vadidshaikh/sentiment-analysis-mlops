import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import mlflow
import dagshub

# Initialize DagsHub
dagshub.init(repo_owner='vadidshaikh', repo_name='sentiment-analysis-mlops', mlflow=True)

# Create model directory if it doesn't exist
os.makedirs("model", exist_ok=True)

print("Loading data...")
df = pd.read_csv('data/raw/data.csv')

# Extract features and labels
reviews = df['review']
sentiments = df['sentiment']

print("Splitting data...")
x_train, x_test, y_train, y_test = train_test_split(reviews, sentiments, test_size=0.2, random_state=42)

print("Vectorizing text with n-grams...")
vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
x_train_vec = vectorizer.fit_transform(x_train)
x_test_vec = vectorizer.transform(x_test)

print("Training model with C parameter...")
with mlflow.start_run():
    model = LogisticRegression(C=0.5, max_iter=1000)
    model.fit(x_train_vec, y_train)

    print("Evaluating...")
    predictions = model.predict(x_test_vec)
    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy:", accuracy)

    # Logging
    mlflow.log_param("max_features", 5000)
    mlflow.log_param("ngram_range", "(1, 2)")
    mlflow.log_param("model_type", "LogisticRegression")
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "model")

    # Save artifacts for the API
    joblib.dump(model, 'model/model.pkl')
    joblib.dump(vectorizer, 'model/vectorizer.pkl')

print("Training complete and artifacts saved.")