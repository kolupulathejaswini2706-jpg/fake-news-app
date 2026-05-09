import streamlit as st
import pickle

# Load saved model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Web page title
st.title("📰 Fake News Detection App")
st.subheader("Paste any news article below to check if it's Fake or Real")

# Text input from user
input_text = st.text_area("Enter News Article Text:")

if st.button("Predict"):
    if input_text.strip() == "":
        st.warning("Please enter some news text!")
    else:
        input_vec = vectorizer.transform([input_text])
        result = model.predict(input_vec)[0]
        confidence = model.predict_proba(input_vec).max()

        if result == 1:
            st.success(f"🟢 Real News (Confidence: {confidence:.2f})")
        else:
            st.error(f"🔴 Fake News (Confidence: {confidence:.2f})")