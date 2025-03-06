from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Load dataset
df = pd.read_csv("C:\\Users\\Dereck\\sentiment-analysis-app\\backend\\data\\Tweets.csv")


# Prepare the data for training
# Using 'text' column for tweet and 'airline_sentiment' for the true sentiment label
X = df['text']
y = df['airline_sentiment']

# Convert the text data to numeric vectors using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
X_vectorized = vectorizer.fit_transform(X)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy * 100:.2f}%')

# Save the trained model using pickle
with open('sentiment_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

# Also save the vectorizer to apply it in the Flask app later
with open('vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)
