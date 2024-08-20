git add requirements.txt
git commit -m "Add requirements.txt"
git push origin main

import streamlit as st
from textblob import TextBlob

# Title of the app
st.title("Sentiment Analysis App")

# Input text box
user_input = st.text_area("Enter a sentence to analyze:")

# Analyze button
if st.button("Analyze"):
    # Perform sentiment analysis
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity

    # Display the result
    if sentiment > 0:
        st.write("The sentiment is **positive**! 😊")
    elif sentiment < 0:
        st.write("The sentiment is **negative**. 😔")
    else:
        st.write("The sentiment is **neutral**. 😐")
