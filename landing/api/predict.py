from http.server import BaseHTTPRequestHandler
import json
import pandas as pd
import numpy as np
import re
import nltk
from textblob import TextBlob
from bs4 import BeautifulSoup
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import os

# Download NLTK data to /tmp where Vercel serverless has write access
nltk.download('punkt', download_dir='/tmp')
nltk.download('punkt_tab', download_dir='/tmp')
nltk.download('stopwords', download_dir='/tmp')
nltk.data.path.append('/tmp')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def clean(t):
    t = str(t).lower()
    t = re.sub(r'[^a-z\s]', '', t)
    return " ".join([w for w in word_tokenize(t) if w not in stopwords.words('english')])

# Train simple model on-the-fly (matching original Streamlit logic)
def get_ai():
    d = {'t': ["Official news.", "Expert report.", "Win free money!", "Secret shocking news!"], 'l': [0, 0, 1, 1]}
    df = pd.DataFrame(d)
    df['c'] = df['t'].apply(clean)
    v = TfidfVectorizer(ngram_range=(1,2))
    X = v.fit_transform(df['c'])
    m = RandomForestClassifier(n_estimators=100)
    m.fit(X, df['l'])
    return m, v

m, v = get_ai()

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            
            mode = data.get('mode', 'text')
            text = data.get('text', '')
            
            if mode == 'url':
                try:
                    r = requests.get(text, timeout=5).text
                    s = BeautifulSoup(r, 'html.parser')
                    text = s.get_text()[:5000]
                except Exception as e:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(json.dumps({'error': 'Failed to scrape URL'}).encode('utf-8'))
                    return
                    
            if not text:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'No text provided'}).encode('utf-8'))
                return
                
            c = clean(text)
            f = v.transform([c])
            p = m.predict(f)[0]
            prob = m.predict_proba(f)[0]
            sentiment = TextBlob(text).sentiment
            
            res = {
                'prediction': int(p),
                'confidence': float(prob[p]),
                'polarity': float(sentiment.polarity),
                'subjectivity': float(sentiment.subjectivity),
                'raw_text': text[:1000]
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(res).encode('utf-8'))
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
