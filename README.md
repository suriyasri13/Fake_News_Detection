# 📰 Fake News Detection System

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![ML Framework](https://img.shields.io/badge/ML-Scikit--Learn-orange.svg)](https://scikit-learn.org/)
[![Expert Build](https://img.shields.io/badge/Status-Expert%20Grade-brightgreen.svg)]()

A high-performance, modular Machine Learning pipeline designed to classify news articles as **Real** or **Fake**. This project leverages state-of-the-art NLP techniques and a suite of 8 advanced classifiers to provide robust predictions.

---

## 🚀 Key Features

- **Robust NLP Preprocessing**: Custom regex-based cleaning, tokenization, and stopword removal using NLTK.
- **Advanced Feature Engineering**: TF-IDF vectorization with optimized 5,000-feature mapping.
- **Ensemble Suite**: Includes 8 powerful models:
  - 📈 **Logistic Regression** (Baseline)
  - 🌲 **Random Forest** (Bagging)
  - 🌊 **Gradient Boosting** (Boosting)
  - 🛡️ **SVM** (Linear separation)
  - 🧠 **Multinomial NB** (Probabilistic)
  - ⚡ **XGBoost** (Extreme Gradient Boosting)
  - 💎 **LightGBM** (Light Gradient Boosting)
  - 🐱 **CatBoost** (Categorical Boosting)
- **Automated Pipeline**: End-to-end execution from raw CSV to individual model submissions.

---

## 🛠️ Installation & Setup

1. **Clone the environment**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Prepare Data**:
   Ensure `xy_train.csv` and `x_test.csv` are in the root directory. If you don't have data, run the generator:
   ```bash
   python generate_sample_data.py
   ```

3. **Run the Pipeline**:
   ```bash
   python fake_news_detector.py
   ```

---

## 📊 Pipeline Workflow

### 1. Preprocessing
Converts raw, noisy text into a clean format by removing special characters, numbers, and common English stopwords.

### 2. Feature Extraction
Uses `TfidfVectorizer` to transform cleaned text into numerical vectors that capture the importance of words across the dataset.

### 3. Training & Evaluation
Iterates through 8 classifiers, training on 80% of the data and validating on the remaining 20%. Each model provides an accuracy score and a detailed classification report.

### 4. Prediction Export
Generates submission-ready CSV files for each model in the `submissions/` directory.

---

## 📂 Project Structure

```text
├── submissions/           # Generated prediction CSVs
├── fake_news_detector.py  # Main pipeline logic
├── generate_sample_data.py # Dummy data generator
├── requirements.txt       # Dependencies
└── README.md              # Documentation
```

---

## 👨‍💻 Author
**Suriya Sri**  
*Expert Machine Learning Engineer*
