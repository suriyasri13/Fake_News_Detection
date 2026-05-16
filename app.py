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
st.set_page_config(page_title="Fake News Detection AI", page_icon="🛡️", layout="wide", initial_sidebar_state="expanded")

# --- Elite Design System (Custom CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
        color: #f8fafc;
    }

    /* Background Gradient */
    .stApp {
        background: radial-gradient(circle at top right, #1e1b4b, #020617);
    }

    /* Hide Streamlit Branding */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}

    /* Glassmorphism Containers */
    .glass-card {
        background: rgba(15, 23, 42, 0.6);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 30px;
        margin-bottom: 20px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }

    /* Neon Gradient Text */
    .title-text {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(to right, #3b82f6, #8b5cf6, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
        letter-spacing: -2px;
    }

    /* Custom Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 14px;
        height: 3.5em;
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        font-weight: 800;
        border: none;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(59, 130, 246, 0.4);
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: rgba(2, 6, 23, 0.95);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }

    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        background-color: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre;
        background-color: rgba(30, 41, 59, 0.3);
        border-radius: 12px;
        color: #94a3b8;
        font-weight: 600;
        padding: 10px 25px;
    }

    .stTabs [aria-selected="true"] {
        background-color: #3b82f6 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NLTK & AI Setup ---
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
def get_model():
    data = {'text': ["Policy update from government.", "Scientific breakthrough in health.", "Sports results announced.", "Weather report for tomorrow.", "SHOCKING secret revealed!", "CLICK here to win!", "Aliens landed in London."], 'label': [0, 0, 0, 0, 1, 1, 1]}
    df = pd.DataFrame(data); df['cleaned'] = df['text'].apply(clean_text)
    vec = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
    X = vec.fit_transform(df['cleaned']); y = df['label']
    model = RandomForestClassifier(n_estimators=100); model.fit(X, y)
    return model, vec

def scrape(url):
    try:
        r = requests.get(url, timeout=5); s = BeautifulSoup(r.content, 'html.parser')
        for script in s(["script", "style"]): script.extract()
        return '\n'.join(p.strip() for p in s.get_text().splitlines() if p.strip())[:5000]
    except: return "Connection failed."

def run_analysis(text):
    if text:
        model, vec = get_model(); b = TextBlob(text); c = clean_text(text)
        f = vec.transform([c]); p = model.predict(f)[0]; prob = model.predict_proba(f)[0]
        st.session_state.result = {'pred': p, 'conf': prob[p], 'pol': (b.sentiment.polarity+1)/2, 'sub': b.sentiment.subjectivity, 'text': text}
    else: st.warning("No input provided.")

# --- Sidebar ---
with st.sidebar:
    st.markdown('<div style="text-align:center"><img src="https://img.icons8.com/fluency/144/shield.png" width="80"></div>', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center'>FactGuard Pro</h2>", unsafe_allow_html=True)
    st.markdown("---")
    if st.button("RESET PLATFORM"): st.session_state.clear(); st.rerun()
    st.markdown("---")
    st.info("System calibrated for journalistic pattern analysis.")

# --- Main UI ---
st.markdown("<h1 class='title-text'>FAKE NEWS DETECTION</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#94a3b8; font-size:1.2rem; margin-top:-20px; margin-bottom:30px;'>Advanced Misinformation Analysis Engine by Suriya Sri</p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚀 SCAN CENTER", "🔗 URL SCAN", "🧬 SYSTEM INTEL"])

with tab1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    t_in = st.text_area("Source Material", height=200, placeholder="Paste your article or headline here...")
    if st.button("INITIATE DEEP SCAN"): run_analysis(t_in)
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    u_in = st.text_input("Source URL")
    if st.button("FETCH & ANALYZE"):
        with st.spinner("Connecting to source..."): run_analysis(scrape(u_in))
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 🧬 AI Architecture")
    st.write("Using a Random Forest Ensemble with TF-IDF Vectorization.")
    st.markdown("#### Process:")
    st.code("1. Clean -> 2. Tokenize -> 3. Vectorize -> 4. Classify")
    st.markdown('</div>', unsafe_allow_html=True)

# --- Results ---
if 'result' in st.session_state:
    r = st.session_state.result
    st.markdown("---")
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    res_color = "#10b981" if r['pred'] == 0 else "#ef4444"
    res_label = "✅ LIKELY AUTHENTIC" if r['pred'] == 0 else "🚩 FAKE NEWS DETECTED"
    
    st.markdown(f"<h1 style='color:{res_color}; font-weight:900;'>{res_label}</h1>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        fig = go.Figure(go.Indicator(mode="gauge+number", value=r['conf']*100, title={'text': "Confidence", 'font':{'color':'#94a3b8'}}, number={'font':{'color':res_color}},
            gauge={'axis':{'range':[None,100]}, 'bar':{'color':res_color}, 'bgcolor':'rgba(0,0,0,0)'}))
        fig.update_layout(height=250, paper_bgcolor='rgba(0,0,0,0)', font={'color':'white'})
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = go.Figure(go.Indicator(mode="gauge+number", value=r['pol']*100, title={'text': "Tone", 'font':{'color':'#94a3b8'}}, number={'font':{'color':'#8b5cf6'}},
            gauge={'axis':{'range':[None,100]}, 'bar':{'color':'#8b5cf6'}, 'bgcolor':'rgba(0,0,0,0)'}))
        fig.update_layout(height=250, paper_bgcolor='rgba(0,0,0,0)', font={'color':'white'})
        st.plotly_chart(fig, use_container_width=True)
    with c3:
        fig = go.Figure(go.Indicator(mode="gauge+number", value=r['sub']*100, title={'text': "Bias Index", 'font':{'color':'#94a3b8'}}, number={'font':{'color':'#f59e0b'}},
            gauge={'axis':{'range':[None,100]}, 'bar':{'color':'#f59e0b'}, 'bgcolor':'rgba(0,0,0,0)'}))
        fig.update_layout(height=250, paper_bgcolor='rgba(0,0,0,0)', font={'color':'white'})
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.download_button("📥 DOWNLOAD REPORT", FPDF().output(dest='S').encode('latin-1'), "Report.pdf", "application/pdf")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; opacity:0.5; font-size:0.8rem; margin-top:50px;'>FAKE NEWS DETECTION | PRO ENGINE v3.5 | CREATED BY SURIYA SRI</p>", unsafe_allow_html=True)
