import streamlit as st
import pandas as pd
import numpy as np
import re
import nltk
import os
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from fpdf import FPDF
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --- Page Config ---
st.set_page_config(page_title="FactGuard AI Ultra", page_icon="🔮", layout="wide")

# --- Design System ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    :root { --primary: #3b82f6; --secondary: #8b5cf6; --danger: #ef4444; --success: #10b981; }
    html, body, [class*="css"] { font-family: 'Outfit', sans-serif; color: #f8fafc; }
    .stApp { background: radial-gradient(circle at top right, #1e1b4b, #020617); }
    .glass-card {
        background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 24px;
        padding: 2.5rem; margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%; border-radius: 12px; height: 4em;
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
        color: white; font-weight: 800; border: none; transition: all 0.4s ease;
    }
    .stButton>button:hover { transform: translateY(-5px); box-shadow: 0 20px 30px -10px rgba(139, 92, 246, 0.6); }
    </style>
    """, unsafe_allow_html=True)

if 'input_val' not in st.session_state: st.session_state.input_val = ""
if 'last_result' not in st.session_state: st.session_state.last_result = None

@st.cache_resource
def init_system():
    nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')

init_system()

def clean_text(text):
    if not isinstance(text, str): return ""
    text = text.lower(); text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = word_tokenize(text); stop_words = set(stopwords.words('english'))
    return " ".join([w for w in tokens if w not in stop_words])

@st.cache_resource
def get_ai_model():
    data = {
        'text': [
            "Federal Reserve interest rate hike.", "Climate study findings released.", "Medical breakthrough in vaccines.",
            "Local elections results finalized.", "Space exploration goals for 2030.", "SHOCKING: Secret revealed now!",
            "CLICK HERE to win a million!", "Aliens landed in your backyard.", "Immortal life hack secret juice."
        ]*10, 'label': [0, 0, 0, 0, 0, 1, 1, 1, 1]*10
    }
    df = pd.DataFrame(data); df['cleaned'] = df['text'].apply(clean_text)
    vec = TfidfVectorizer(max_features=5000, ngram_range=(1, 3))
    X = vec.fit_transform(df['cleaned']); y = df['label']
    model = RandomForestClassifier(n_estimators=100, random_state=42); model.fit(X, y)
    return model, vec

def scrape_content(url):
    try:
        r = requests.get(url, timeout=5); soup = BeautifulSoup(r.content, 'html.parser')
        for s in soup(["script", "style"]): s.extract()
        return '\n'.join(p.strip() for p in soup.get_text().splitlines() if p.strip())[:5000]
    except: return "Scraping failed."

def run_analysis(text):
    if text:
        model, vec = get_ai_model(); blob = TextBlob(text); cleaned = clean_text(text)
        features = vec.transform([cleaned]); probs = model.predict_proba(features)[0]; pred = model.predict(features)[0]
        st.session_state.result = {'pred': pred, 'conf': probs[pred], 'pol': (blob.sentiment.polarity+1)/2, 'sub': blob.sentiment.subjectivity, 'text': text}
        st.session_state.input_val = ""
    else: st.warning("No input provided.")

def draw_gauge(score, title, color):
    fig = go.Figure(go.Indicator(mode = "gauge+number", value = score*100, title = {'text': title, 'font': {'size': 18, 'color': '#94a3b8'}}, number = {'font': {'color': color, 'size': 32}},
        gauge = {'axis': {'range': [None, 100]}, 'bar': {'color': color}, 'bgcolor': "rgba(0,0,0,0)", 'borderwidth': 2, 'bordercolor': "#475569"}))
    fig.update_layout(height=220, margin=dict(l=20, r=20, t=50, b=20), paper_bgcolor='rgba(0,0,0,0)', font={'color': "#f8fafc"})
    return fig

# --- Layout ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/144/shield.png", width=80)
    st.title("FactGuard Ultra")
    st.markdown("---")
    if st.button("RESET PLATFORM"): st.session_state.clear(); st.rerun()
    st.info("High Sensitivity Mode Enabled.")

st.title("🛡️ Intelligence Dashboard")
tabs = st.tabs(["🚀 Scan Center", "🔗 URL Link", "🧬 How it Works"])

with tabs[0]:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    text_in = st.text_area("Source Text", height=200, placeholder="Paste content...", value=st.session_state.input_val)
    if st.button("INITIATE TEXT SCAN"): run_analysis(text_in)
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[1]:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    url_in = st.text_input("Source URL")
    if st.button("INITIATE URL SCRAPE"):
        with st.spinner("Scraping..."): run_analysis(scrape_content(url_in))
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[2]:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 🧬 AI Architecture")
    st.write("FactGuard AI utilizes a **Random Forest Ensemble** with a **TF-IDF Vectorizer** (ngram range 1-3).")
    st.markdown("#### 🛠️ Processing Pipeline:")
    st.code("1. Regex-based Noise Removal\n2. NLTK Tokenization\n3. Stopword Filtering\n4. Sentiment Polarity Mapping\n5. Ensemble Voting Classifier")
    st.info("This system is designed to detect 'Sensationalist' linguistic patterns.")
    st.markdown('</div>', unsafe_allow_html=True)

if 'result' in st.session_state:
    res = st.session_state.result
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.plotly_chart(draw_gauge(res['conf'], "Confidence", "#ef4444" if res['pred']==1 else "#10b981"), use_container_width=True)
    with c2: st.plotly_chart(draw_gauge(res['pol'], "Tone", "#8b5cf6"), use_container_width=True)
    with c3: st.plotly_chart(draw_gauge(res['sub'], "Bias", "#f59e0b"), use_container_width=True)
    with c4: st.write(f"### {'🚩 FAKE' if res['pred']==1 else '✅ REAL'}"); st.write(f"Words: {len(res['text'].split())}")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("FactGuard Ultra | Created by Suriya Sri")
