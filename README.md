# Sentiment Analysis

This Streamlit app analyzes the sentiment of a given tweet using a pre-trained sentiment analysis model.

Overview
This app utilizes the Hugging Face transformers library to load a pre-trained sentiment analysis model, specifically the cardiffnlp/twitter-roberta-base-sentiment model. It takes user input in the form of a tweet and predicts whether the sentiment of the tweet is Negative, Neutral, or Positive.

Usage
To use the app:

Clone this repository to your local machine.

Install the required Python dependencies by running:
pip install -r requirements.txt

Enter a tweet in the provided text input field and click the "Analyze" button to see the sentiment analysis results.
Dependencies
streamlit: Used for creating the web app interface.
transformers: Used for loading the pre-trained sentiment analysis model.
scipy: Used for computing softmax scores.

About
This app was created by Nitin Rai as a demonstration of sentiment analysis using pre-trained models. Feel free to reach out for any questions or feedback.

