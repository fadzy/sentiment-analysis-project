from flask import Flask, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the pre-trained sentiment analysis model (vaderSentiment)
analyzer = SentimentIntensityAnalyzer()

# Define the API route for sentiment analysis
@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    tweet = data.get('tweet')  # Ensure you get the tweet text from the frontend

    if tweet:
        sentiment = classify_sentiment(tweet)  # Classify sentiment
        return jsonify({'sentiment': sentiment})
    else:
        return jsonify({'error': 'No tweet text provided'}), 400  # Return error if no tweet text

# Function to classify sentiment using vaderSentiment
def classify_sentiment(text):
    score = analyzer.polarity_scores(text)
    compound_score = score['compound']
    
    if compound_score >= 0.05:
        return 'Positive'
    elif compound_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

if __name__ == '__main__':
    app.run(debug=True)
