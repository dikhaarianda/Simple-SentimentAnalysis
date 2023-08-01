import nltk
import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#get dataset
nltk.download('vader_lexicon')

st.header("Picture Sentiment Analysis")
st.image("WindowsLogo.png", caption='Windows Logo', width=300)
usr_input = st.text_input("What's your opinion on this Operating System?")

#Process
sentiment = SentimentIntensityAnalyzer()
score = sentiment.polarity_scores(usr_input)
# st.write(score)

#Show Result
if score["neu"] > score["neg"] and score["neu"] > score["pos"]:
  st.warning("Your respon is: \n # Neutral")
elif score["neg"] > score["pos"]:
  st.error(" Your respon is: \n # Negative")
elif score["pos"] > score["neg"]:
  st.success("Your respon is: \n # Positive")