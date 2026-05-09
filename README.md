A machine learning-based web application built using Streamlit that detects whether a given news article or message is Real or Fake and also identifies potential phishing content. The system uses trained ML models to analyze textual data and provide instant predictions.

📌 Features

Detects Fake News using Machine Learning

Detects Phishing Text / Messages

Uses trained ML models with text preprocessing

User-friendly Streamlit web interface

Fast and lightweight application

🛠️ Technologies Used

Python

Streamlit

Scikit-learn

Pandas

NumPy

Pickle

NLP (TF-IDF Vectorizer)

📂 Project Structure
phishing-news-app-detector/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── fake.csv
├── true.csv
├── README.md
⚙️ Installation & Setup
pip install -r requirements.txt
streamlit run app.py
🧪 How It Works

User enters text

Text is cleaned and vectorized

ML model predicts result

Output is displayed

📊 Model Details

Algorithm: Logistic Regression / Naive Bayes

Feature Extraction: TF-IDF Vectorizer

Dataset: Fake & Real News CSV files

🚀 Future Enhancements

Add Deep Learning models

Multi-language support

Cloud deployment

UI improvements
