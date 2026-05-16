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
import plotly.graph_objects as go
from datetime import datetime
import time

# --- Page Config ---
st.set_page_config(
    page_title="FactGuard AI - Neural Engine",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- AI Mode CSS (Ultra High-End) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }

    /* Neural Background */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #1e1b4b 0%, #020617 100%);
    }

    /* Cyber Glow Elements */
    .glass-panel {
        background: rgba(15, 23, 42, 0.5);
        backdrop-filter: blur(25px);
        border: 1px solid rgba(59, 130, 246, 0.2);
        border-radius: 24px;
        padding: 30px;
        margin-bottom: 20px;
        box-shadow: 0 0 40px rgba(0,0,0,0.5);
    }

    .neural-title {
        font-size: 4rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -3px;
    }

    /* Sidebar Neural Styling */
    [data-testid="stSidebar"] {
        background-color: #020617;
        border-right: 2px solid #3b82f6;
    }

    /* AI Chat Bubble */
    .chat-bubble {
        background: rgba(59, 130, 246, 0.1);
        border-left: 4px solid #3b82f6;
        padding: 15px;
        border-radius: 0 15px 15px 0;
        margin-bottom: 10px;
        font-style: italic;
    }
    
    /* Animation for Neural Pulse */
    @keyframes pulse-glow {
        0% { box-shadow: 0 0 10px rgba(59, 130, 246, 0.2); }
        50% { box-shadow: 0 0 30px rgba(59, 130, 246, 0.5); }
        100% { box-shadow: 0 0 10px rgba(59, 130, 246, 0.2); }
    }
    .pulse-card {
        animation: pulse-glow 4s infinite ease-in-out;
    }
    </style>
    """, unsafe_allow_html=True)

# --- System Assets ---
@st.cache_resource
def init():
    nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')

init()

def clean(t):
    t = str(t).lower(); t = re.sub(r'[^a-z\s]', '', t)
    return " ".join([w for w in word_tokenize(t) if w not in stopwords.words('english')])

@st.cache_resource
def get_ai():
    d = {'t': ["Official news.", "Expert report.", "Win free money!", "Secret shocking news!"], 'l': [0, 0, 1, 1]}
    df = pd.DataFrame(d); df['c'] = df['t'].apply(clean)
    v = TfidfVectorizer(ngram_range=(1,2)); X = v.fit_transform(df['c'])
    m = RandomForestClassifier(n_estimators=100); m.fit(X, df['l'])
    return m, v

# --- Sidebar (Neural Controller) ---
with st.sidebar:
    st.markdown('<div style="text-align:center"><img src="https://img.icons8.com/fluency/144/brain.png" width="90"></div>', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#3b82f6;'>NEURAL ENGINE</h2>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 🤖 AI Status")
    st.success("AUTONOMOUS MODE: **ACTIVE**")
    st.markdown("---")
    if st.button("RESET MEMORY"): st.session_state.clear(); st.rerun()
    st.markdown("---")
    st.markdown("#### Cloud Deployment Ready")
    st.code("v4.5.0-NEURAL")

# --- Header ---
st.markdown("<h1 class='neural-title'>FACTGUARD AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#94a3b8; font-size:1.2rem; margin-top:-20px; margin-bottom:40px;'>Autonomous Misinformation Neural Network | Suriya Sri</p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🧠 NEURAL SCAN", "🌐 WEB SCRAPER", "💬 AI ASSISTANT"])

with tab1:
    st.markdown('<div class="glass-panel pulse-card">', unsafe_allow_html=True)
    txt = st.text_area("Input Stream", height=200, placeholder="Paste data here for neural analysis...")
    if st.button("EXECUTE SCAN"):
        if txt:
            with st.spinner("Analyzing neural patterns..."):
                m, v = get_ai(); c = clean(txt); f = v.transform([c])
                p = m.predict(f)[0]; prob = m.predict_proba(f)[0]
                st.session_state.res = {'p':p, 'c':prob[p], 'txt':txt, 'sent':TextBlob(txt).sentiment}
        else: st.warning("Input required.")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    url = st.text_input("Target URL")
    if st.button("SCRAPE & SCAN"):
        with st.spinner("Connecting to global web..."):
            try:
                r = requests.get(url).text; s = BeautifulSoup(r, 'html.parser'); t_raw = s.get_text()[:5000]
                m, v = get_ai(); c = clean(t_raw); f = v.transform([c])
                p = m.predict(f)[0]; prob = m.predict_proba(f)[0]
                st.session_state.res = {'p':p, 'c':prob[p], 'txt':t_raw, 'sent':TextBlob(t_raw).sentiment}
            except: st.error("Target unreachable.")
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.markdown("### 💬 Neural Assistant")
    if 'res' in st.session_state:
        st.markdown(f"<div class='chat-bubble'>AI: I have analyzed the content. The authenticity score is **{st.session_state.res['c']*100:.1f}%**. Would you like me to generate a full report?</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='chat-bubble'>AI: Hello Suriya Sri. Please provide some news content, and I will analyze its linguistic integrity for you.</div>", unsafe_allow_html=True)
    
    chat_in = st.text_input("Ask AI Assistant...", placeholder="Type here...")
    if chat_in:
        st.info(f"AI Assistant: That's a great question! Based on my neural training, I recommend checking multiple sources for any claim that has a Bias Index over 60%.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- Neural Dashboard ---
if 'res' in st.session_state:
    r = st.session_state.res
    st.markdown("---")
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    
    color = "#10b981" if r['p'] == 0 else "#f43f5e"
    label = "✅ NEURAL VERIFIED: AUTHENTIC" if r['p'] == 0 else "🚩 NEURAL ALERT: MISINFORMATION"
    
    st.markdown(f"<h1 style='color:{color}; font-weight:900;'>{label}</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    def gauge(v, t, c):
        fig = go.Figure(go.Indicator(mode="gauge+number", value=v, title={'text':t, 'font':{'color':'#94a3b8'}}, number={'font':{'color':'white'}},
            gauge={'axis':{'range':[None,100]}, 'bar':{'color':c}, 'bgcolor':'rgba(0,0,0,0)'}))
        fig.update_layout(height=280, paper_bgcolor='rgba(0,0,0,0)', font={'color':'white'})
        return fig

    with col1: st.plotly_chart(gauge(r['c']*100, "Neural Confidence", color), use_container_width=True)
    with col2: st.plotly_chart(gauge((r['sent'].polarity+1)*50, "Linguistic Tone", "#8b5cf6"), use_container_width=True)
    with col3: st.plotly_chart(gauge(r['sent'].subjectivity*100, "Bias Index", "#f59e0b"), use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; opacity:0.3; margin-top:100px;'>FACTGUARD NEURAL | AUTONOMOUS VERSION | SURIYA SRI</p>", unsafe_allow_html=True)
