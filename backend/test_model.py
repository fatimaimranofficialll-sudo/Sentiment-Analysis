import joblib

# Load the trained model
model = joblib.load("model.pkl")

# Load the TF-IDF vectorizer
vectorizer = joblib.load("vectorizer.pkl")

# Test sentences
texts = [
    "I love this product",
    "This is the worst experience",
    "The product arrived today",
    "The meeting is scheduled for tomorrow."
]

# Convert text into TF-IDF features
text_vectors = vectorizer.transform(texts)

# Make predictions
predictions = model.predict(text_vectors)

# Display results
for text, prediction in zip(texts, predictions):
    print("Text:", text)
    print("Prediction:", prediction)
    print()