import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

# Load model and tokenizer
roberta = "cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)
labels = ['Negative', 'Neutral', 'Positive']

# Function to preprocess the tweet
def preprocess_tweet(tweet):
    tweet_words = []
    for word in tweet.split(' '):
        if word.startswith('@') and len(word) > 1:
            word = '@user'
        elif word.startswith('http'):
            word = "http"
        tweet_words.append(word)
    return " ".join(tweet_words)

# Function for sentiment analysis
def sentiment_analysis(tweet):
    tweet_proc = preprocess_tweet(tweet)
    encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')
    output = model(**encoded_tweet)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    results = {}
    for i in range(len(scores)):
        results[labels[i]] = scores[i]
    return results

# Emojis for sentiment labels
emojis = {
    'Negative': '😞',
    'Neutral': '😐',
    'Positive': '😊'
}

# Streamlit app
st.title('Tweet Sentiment Analysis')
st.sidebar.write("Created by Nitin Rai")
st.sidebar.write("Website: [Nitin Rai's Blog](https://nitinkrai.blogspot.com/)")

tweet_input = st.sidebar.text_input('Enter your tweet:', value='', max_chars=None)

if st.sidebar.button('Analyze'):
    if tweet_input:
        results = sentiment_analysis(tweet_input)
        st.write("Sentiment Analysis Results:")
        for label, score in results.items():
            emoji = emojis.get(label, '')
            st.write(f"{label}: {score:.4f} {emoji}")
    else:
        st.write("Please enter a tweet.")
