import pandas as pd 
import pyodbc 
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer  


# function to read data from the database 
def fetch_data_from_sql(): 
    conn_str = (
        "Driver={SQL Server};"  # Specify the driver for SQL Server
        "Server=NASR-OHD-PC01\SA;"  # Specify your SQL Server instance
        "Database=PortfolioProject_MarketingAnalytics;"  # Specify the database name
        "Trusted_Connection=yes;"
    )

    conn = pyodbc.connect(conn_str) 

    query = "Select ReviewID, CustomerID, ProductID,  ReviewDate, Rating, ReviewText from customer_reviews "

    df = pd.read_sql(query , conn)

    conn.close() 

    return df 

customer_reviews_df = fetch_data_from_sql() 

# print(customer_reviews_df)

sia = SentimentIntensityAnalyzer() 

def calculate_sentiment(review) : 
    sentiemnt = sia.polarity_scores(review) 


    return sentiemnt['compound']
    # Positive: Compound score is greater than or equal to 0.05 (>= 0.05)
    # Neutral: Compound score is between -0.05 and 0.05 (-0.05 < score < 0.05)
    # Negative: Compound score is less than or equal to -0.05 (<= -0.05)

# a function to categorize sentiment using both rating and sentiment compound score 

def categorize_sentiment(rating , score) :
    if score >= .05 : 
        if rating >=4 : 
            return "Positive" # high rating and positive sentiment
        elif rating == 3: 
            return "Mixed Positive" # Neutral rating but positive sentiment  
        else : 
            return "Mixed Negative" # low rating but positive sentiment 
    elif score <= -0.05 : 
        if rating <=2 : 
            return "Negative"
        elif rating == 3 : 
            return "Mixed Negative" # netral rating but negative sentiment 
        else : 
            return "Mixed Positive" # high rating but negative sentiment 
    else : 
        if rating >=4 : 
            return "Positive"  # High rating with neutral sentiment
        elif rating <= 2 : 
            return "Negative"  # Low rating with neutral sentiment
        else : 
            return "Neutral"          # Neutral rating and neutral sentiment




def sentiment_bucket(score):
    if score >= 0.5:
        return '0.5 to 1.0'  # Strongly positive sentiment
    elif 0.0 <= score < 0.5:
        return '0.0 to 0.49'  # Mildly positive sentiment
    elif -0.5 <= score < 0.0:
        return '-0.49 to 0.0'  # Mildly negative sentiment
    else:
        return '-1.0 to -0.5'  # Strongly negative sentiment

customer_reviews_df['SentimentScore'] = customer_reviews_df['ReviewText'].apply(calculate_sentiment)

customer_reviews_df['SentimentCategory'] = customer_reviews_df.apply( 
           lambda row : categorize_sentiment(row["Rating"] , row['SentimentScore']) , axis=1)

customer_reviews_df['SentimentBucket'] = customer_reviews_df['SentimentScore'].apply(sentiment_bucket)

print(customer_reviews_df.head())

customer_reviews_df.to_csv('fact_customer_reviews_with_sentiment.csv', index=False)
