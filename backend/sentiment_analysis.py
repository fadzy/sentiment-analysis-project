import pandas as pd

# Load datasetpython sentiment_analysis.py

df = pd.read_csv(r"C:\Users\Dereck\sentiment-analysis-app\backend\data\Tweets.csv")

# Check the first few rows
print(df.head())

# Check unique sentiment labels
print(df["airline_sentiment"].value_counts())