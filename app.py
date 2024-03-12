from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

# Specify the user you want to fetch tweets from
user = 'PMOIndia'

# Define the date range
begin_date = dt.date(2024, 3, 3)
end_date = dt.date(2024, 3, 8)

# Specify other parameters
limit = 10000

# Construct the search query with the user's username and date range
search_query = f'from:{user} since:{begin_date} until:{end_date}'

# Query tweets based on the search query
tweets = query_tweets(query=search_query, limit=limit)

# Create a DataFrame with the tweet text
df = pd.DataFrame({'text': [tweet.text for tweet in tweets]})

# Print the DataFrame containing the tweet text
print("Tweets by PMOIndia:")
print(df)

# Use this if you want to search for a specific phrase or word within the same date range
search_phrase = 'Content'
tweets_phrase = query_tweets(search_phrase, limit=limit)

# Create a DataFrame with the tweet text containing the specified phrase or word
df_phrase = pd.DataFrame({'text': [tweet.text for tweet in tweets_phrase]})

# Print the DataFrame containing the tweets with the specified phrase or word
print("\nTweets containing 'Content':")
print(df_phrase)
