import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon
nltk.download('vader_lexicon')

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Page config
st.set_page_config(
    page_title="Twitter Sentiment Analysis",
    page_icon="🐦",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

/* Background Image */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1611926653458-09294b3142bf");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* Glass Effect Container */
.block-container {
    background-color: rgba(0, 0, 0, 0.75);
    padding: 2rem;
    border-radius: 20px;
}

/* White Heading */
h1 {
    color: white !important;
    text-align: center;
    text-shadow: 2px 2px 10px black;
}

/* White Text */
h2, h3, p, label {
    color: white !important;
}

/* Text Area */
.stTextArea textarea {
    background-color: rgba(255,255,255,0.1);
    color: white;
    border-radius: 10px;
}

/* Button */
.stButton button {
    background-color: #1DA1F2;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: bold;
    width: 100%;
}

/* Animated Twitter Logo */
.twitter-logo {
    position: fixed;
    top: 20px;
    right: 20px;
    width: 80px;
    z-index: 999;
    animation: float 4s ease-in-out infinite,
               rotate 8s linear infinite;
}

/* Floating Animation */
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(20px); }
    100% { transform: translateY(0px); }
}

/* Rotation Animation */
@keyframes rotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

</style>
""", unsafe_allow_html=True)

# Animated Twitter Logo
st.markdown("""
<img class="twitter-logo"
src="https://cdn-icons-png.flaticon.com/512/733/733579.png">
""", unsafe_allow_html=True)

# Title
st.title("🐦 Twitter Sentiment Analysis")

st.write("Enter a tweet and get instant sentiment analysis results.")

# Input
tweet = st.text_area("Paste Tweet Here")

# Analyze Button
if st.button("Analyze Sentiment"):

    if tweet:

        score = sia.polarity_scores(tweet)

        st.subheader("Sentiment Score")
        st.json(score)

        compound = score["compound"]

        if compound >= 0.05:
            st.success("😊 Positive Tweet")

        elif compound <= -0.05:
            st.error("😡 Negative Tweet")

        else:
            st.info("😐 Neutral Tweet")

    else:
        st.warning("Please enter a tweet first!")