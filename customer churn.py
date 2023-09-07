import numpy as np
import pandas as pd

# Define the number of synthetic records
num_records = 1000

# Generate synthetic data
customer_ids = np.arange(1, num_records + 1)
names = np.random.choice(['John', 'Jane', 'Bob', 'Alice'], num_records)
ages = np.random.randint(18, 65, num_records)
usage_frequency = np.random.randint(1, 11, num_records)
customer_feedback = np.random.choice(["Great service! I love the app.",
                                      "The app is easy to use, but it could use more features.",
                                      "I've had some issues with the app crashing.",
                                      "Excellent customer support, they resolved my issue quickly.",
                                      "The pricing is bad for the value provided."],
                                         num_records)
# ... generate data for other attributes ...

# Create a Pandas DataFrame to store the synthetic data
synthetic_data = pd.DataFrame({
    'customer_id': customer_ids,
    'name': names,
    'age': ages,
    'usage_frequency': usage_frequency,
    'customer_feedback': customer_feedback
    # ... add other columns ...
})

# Assuming you've already generated the synthetic data in the 'synthetic_data' DataFrame

# Assuming you've already generated the synthetic data in the 'synthetic_data' DataFrame

import mysql.connector
from sqlalchemy import create_engine

# mysql stuff to connect to my database
host = 'localhost'
user = 'root'
password = 'ashraf457'
database = 'customer_churn'

# using mysql connector module
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a SQLAlchemy engine to connect to the MySQL database
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

# idk what this does tbh
"""synthetic_data.to_sql('customer_data', con=engine, if_exists='replace', index=False)

# close connection
conn.close()"""

# Assuming you've already generated the synthetic data in the 'synthetic_data' DataFrame


# Define the number of days or time periods over which you want to calculate usage frequency
num_time_periods = 30  # You can adjust this based on your data

# Generate random usage data for each customer over the specified time periods
usage_data = np.random.randint(1, 11, (num_records, num_time_periods))

# Calculate usage frequency as the sum of interactions over the time periods
usage_frequency = usage_data.sum(axis=1)

# Add the 'usage_frequency' column to the DataFrame
synthetic_data['usage_frequency'] = usage_frequency

# Display the updated DataFrame
#print(synthetic_data.head())

import random

# Create synthetic customer feedback
customer_feedback = [
    "Great service! I love the app.",
    "The app is easy to use, but it could use more features.",
    "I've had some issues with the app crashing.",
    "Excellent customer support, they resolved my issue quickly.",
    "The pricing is bad for the value provided.",
    
    # Add more synthetic feedback here
]
#print(synthetic_data)

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')  # Download the VADER lexicon

# Create a SentimentIntensityAnalyzer object
sia = SentimentIntensityAnalyzer()

# Function to perform sentiment analysis
def analyze_sentiment(text):
    sentiment_scores = sia.polarity_scores(text)
    # Use the compound score to categorize sentiment
    compound_score = sentiment_scores['compound']
    if compound_score >= 0.05:
        return 'Positive'
    elif compound_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment analysis to customer feedback
synthetic_data['sentiment_analysis'] = synthetic_data['customer_feedback'].apply(analyze_sentiment)

synthetic_data.to_sql('customer_data', con=engine, if_exists='replace', index=False)

# close connection
conn.close()
print(synthetic_data)
print("hi")




