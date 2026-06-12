import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download VADER Lexicon
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Page Configuration
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
    background-image: url("https://images.unsplash.com/photo-1563986768609-322da13575f3?q=80&w=2070");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* Glass Effect Container */
.block-container {
    background: rgba(0, 0, 0, 0.80);
    backdrop-filter: blur(15px);
    padding: 2rem;
    border-radius: 25px;
    margin-top: 20px;
}

/* Title */
h1 {
    color: white !important;
    text-align: center;
    font-size: 3rem;
    text-shadow: 2px 2px 10px black;
}

/* Text */
h2, h3, p, label {
    color: white !important;
}

/* Text Area */
.stTextArea textarea {
    background-color: white !important;
    color: black !important;
    border-radius: 15px !important;
    border: 2px solid #1DA1F2 !important;
    font-size: 18px !important;
    font-weight: 500;
}

.stTextArea textarea::placeholder {
    color: gray !important;
}

/* Button */
.stButton button {
    width: 100%;
    background-color: #1DA1F2;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
    border: none;
    padding: 12px;
}

.stButton button:hover {
    background-color: #0d8de1;
}

/* Animated Twitter Logo */
.twitter-logo {
    position: fixed;
    top: 20px;
    right: 20px;
    width: 80px;
    z-index: 999;
    animation: float 3s ease-in-out infinite;
}

/* Floating Animation */
@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(15px);}
    100% {transform: translateY(0px);}
}

</style>
""", unsafe_allow_html=True)

# Twitter Logo
st.markdown("""
<img class="twitter-logo"
src="https://cdn-icons-png.flaticon.com/512/733/733579.png">
""", unsafe_allow_html=True)

# Title
st.title("🐦 Twitter Sentiment Analysis")

st.markdown(
    "<h3 style='text-align:center;'>Analyze Tweet Sentiment Instantly</h3>",
    unsafe_allow_html=True
)

# Input Box
tweet = st.text_area(
    "Enter Tweet",
    placeholder="Type or paste a tweet here..."
)

# Analyze Button
if st.button("🔍 Analyze Sentiment"):

    if tweet.strip():

        score = sia.polarity_scores(tweet)

        st.subheader("📊 Sentiment Score")
        st.json(score)

        compound = score["compound"]

        if compound >= 0.05:
            st.success("😊 Positive Tweet")

        elif compound <= -0.05:
            st.error("😡 Negative Tweet")

        else:
            st.info("😐 Neutral Tweet")

    else:
        st.warning("⚠ Please enter a tweet first!")