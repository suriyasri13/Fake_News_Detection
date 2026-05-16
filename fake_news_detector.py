"""
Fake News Detection Project
==========================
An expert-level Machine Learning pipeline to classify news articles as Real or Fake.
This script implements a modular workflow including:
1. Data Loading
2. Text Preprocessing (Regex, Tokenization, Stopwords)
3. Feature Extraction (TF-IDF)
4. Model Training & Evaluation (8 Classifiers)
5. Prediction & Export

Author: Antigravity (Expert ML Engineer)
Date: 2026-05-16
"""

import os
import re
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import xgboost as xgb
import lightgbm as lgb
from catboost import CatBoostClassifier
from colorama import Fore, Style, init

# Initialize colorama for beautiful terminal output
init(autoreset=True)

# --- Step 1: Imports & Setup ---
def setup_environment():
    """Ensures necessary NLTK resources are downloaded and directories exist."""
    print(f"{Fore.CYAN}[1/6] Setting up environment...")
    resources = ['tokenizers/punkt', 'tokenizers/punkt_tab', 'corpora/stopwords']
    for res in resources:
        try:
            nltk.data.find(res)
        except LookupError:
            print(f"{Fore.YELLOW}Downloading NLTK resource: {res}...")
            nltk.download(res.split('/')[-1])
    
    if not os.path.exists('submissions'):
        os.makedirs('submissions')
        print(f"{Fore.GREEN}Created 'submissions' directory.")

# --- Step 2: Data Loading ---
def load_datasets(train_path='xy_train.csv', test_path='x_test.csv'):
    """
    Loads training and testing data from CSV files.
    
    Returns:
        tuple: (train_df, test_df)
    """
    print(f"{Fore.CYAN}[2/6] Loading data...")
    if not os.path.exists(train_path) or not os.path.exists(test_path):
        raise FileNotFoundError(f"Missing data files: {train_path} or {test_path}")
    
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    
    print(f"{Fore.GREEN}Loaded {len(train_df)} training samples and {len(test_df)} test samples.")
    return train_df, test_df

# --- Step 3: Text Preprocessing ---
def clean_text(text):
    """
    Performs robust text cleaning:
    - Lowercase conversion
    - Special characters and numbers removal
    - Tokenization
    - Stopword removal
    """
    if not isinstance(text, str):
        return ""
    
    # 1. Lowercase
    text = text.lower()
    
    # 2. Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # 3. Tokenize
    tokens = word_tokenize(text)
    
    # 4. Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if w not in stop_words]
    
    return " ".join(filtered_tokens)

def preprocess_data(train_df, test_df, text_col='text'):
    """Applies cleaning function to dataframes."""
    print(f"{Fore.CYAN}[3/6] Preprocessing text data...")
    train_df['cleaned_text'] = train_df[text_col].apply(clean_text)
    test_df['cleaned_text'] = test_df[text_col].apply(clean_text)
    print(f"{Fore.GREEN}Preprocessing complete.")
    return train_df, test_df

# --- Step 4: Feature Extraction ---
def extract_features(train_df, test_df, target_col='label'):
    """
    Converts text to TF-IDF features and performs 80/20 split.
    """
    print(f"{Fore.CYAN}[4/6] Extracting features with TF-IDF (max_features=5000)...")
    vectorizer = TfidfVectorizer(max_features=5000)
    
    X = vectorizer.fit_transform(train_df['cleaned_text'])
    y = train_df[target_col]
    
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    
    X_test_tfidf = vectorizer.transform(test_df['cleaned_text'])
    
    print(f"{Fore.GREEN}Feature extraction complete. Training shape: {X_train.shape}")
    return X_train, X_val, y_train, y_val, X_test_tfidf, vectorizer

# --- Step 5: Model Training & Evaluation ---
def get_model_dictionary():
    """Returns a dictionary of classifiers to iterate through."""
    return {
        'Logistic Regression': LogisticRegression(max_iter=1000),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(random_state=42),
        'SVM': SVC(probability=True, random_state=42),
        'Multinomial NB': MultinomialNB(),
        'XGBoost': xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42),
        'LightGBM': lgb.LGBMClassifier(random_state=42, verbose=-1),
        'CatBoost': CatBoostClassifier(verbose=0, random_state=42)
    }

def train_and_evaluate_models(X_train, X_val, y_train, y_val):
    """Fits models and prints performance metrics."""
    print(f"{Fore.CYAN}[5/6] Training and evaluating models...")
    models = get_model_dictionary()
    trained_models = {}
    
    for name, model in models.items():
        print(f"\n{Fore.YELLOW}Fitting {name}...")
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_val)
        acc = accuracy_score(y_val, y_pred)
        
        print(f"{Fore.GREEN}Accuracy: {acc:.4f}")
        print(f"{Fore.WHITE}Classification Report for {name}:")
        print(classification_report(y_val, y_pred))
        
        trained_models[name] = model
        
    return trained_models

# --- Step 6: Prediction & Export ---
def generate_submissions(trained_models, X_test_tfidf, test_df):
    """Generates and saves prediction CSVs for each model."""
    print(f"\n{Fore.CYAN}[6/6] Generating prediction exports...")
    
    for name, model in trained_models.items():
        # Sanitize name for filename
        short_name = name.split()[0].replace("Logistic", "Logis").replace("Random", "RF").replace("Gradient", "GBM")
        filename = f"submissions/{short_name}_submission.csv"
        
        predictions = model.predict(X_test_tfidf)
        
        submission_df = pd.DataFrame({
            'id': test_df.index,
            'label': predictions
        })
        
        submission_df.to_csv(filename, index=False)
        print(f"{Fore.GREEN}Saved: {filename}")

def main():
    print(f"{Fore.MAGENTA}{Style.BRIGHT}=== FAKE NEWS DETECTION PIPELINE ===")
    
    try:
        setup_environment()
        
        train_df, test_df = load_datasets()
        
        # Check if text column exists
        text_col = 'text' if 'text' in train_df.columns else train_df.columns[0]
        label_col = 'label' if 'label' in train_df.columns else train_df.columns[-1]
        
        train_df, test_df = preprocess_data(train_df, test_df, text_col=text_col)
        
        X_train, X_val, y_train, y_val, X_test_tfidf, vectorizer = extract_features(train_df, test_df, target_col=label_col)
        
        trained_models = train_and_evaluate_models(X_train, X_val, y_train, y_val)
        
        generate_submissions(trained_models, X_test_tfidf, test_df)
        
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}Pipeline execution completed successfully!")
        
    except Exception as e:
        print(f"\n{Fore.RED}Critical Error: {str(e)}")
        print(f"{Fore.YELLOW}Tip: Ensure 'xy_train.csv' and 'x_test.csv' are in the project folder.")

if __name__ == "__main__":
    main()
