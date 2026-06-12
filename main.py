import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# ---------- DOWNLOAD LEXICON ----------
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Twitter Sentiment Analysis",
    page_icon="🐦",
    layout="centered"
)

# ---------- CUSTOM CSS ----------
page_bg = """
<style>

/* Background Image */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1611926653458-09294b3142bf");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* Glass Effect */
.block-container {
    background-color: rgba(0,0,0,0.75);
    padding: 2rem;
    border-radius: 15px;
}

/* Text Colors */
h1, h2, h3, p {
    color: white;
}

/* Input Box */
.stTextArea textarea {
    background-color: #1e1e1e;
    color: white;
    border-radius: 10px;
}

/* Button */
.stButton button {
    background-color: #1DA1F2;
    color: white;
    border-radius: 8px;
    padding: 0.5rem 1rem;
    border: none;
    font-weight: bold;
}

/* Twitter Logo Animation */
.twitter-logo {
    position: fixed;
    top: 20px;
    right: 20px;
    width: 80px;
    animation: float 4s ease-in-out infinite, rotate 8s linear infinite;
    z-index: 999;
}

/* Float Animation */
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(20px); }
    100% { transform: translateY(0px); }
}

/* Rotate Animation */
@keyframes rotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# ---------- TWITTER LOGO ----------
st.markdown("""
<img class="twitter-logo" src="https://cdn-icons-png.flaticon.com/512/733/733579.png">
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.title("🐦 Twitter Sentiment Analysis")
st.write("Enter a tweet and get instant sentiment result")

# ---------- INPUT ----------
tweet = st.text_area("Paste Tweet Here")

# ---------- ANALYSIS ----------
if st.button("Analyze Sentiment"):
    if tweet:
        score = sia.polarity_scores(tweet)

        st.subheader("Result")
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
        