import streamlit as st
from src.predict import predict_sms

st.set_page_config(page_title="SpamShield AI", layout="centered")

st.title("📡 SpamShield AI — SMS Spam Detector")
st.write("An ML + NLP powered app that detects spam messages instantly.")

user_input = st.text_area("Enter SMS text:", height=150)

if st.button("Predict"):
    if user_input.strip():
        label, confidence = predict_sms(user_input)
        
        st.subheader("🔍 Prediction:")
        if label == "Spam":
            st.error(f"🚨 SPAM detected! (Confidence: {confidence:.2f})")
        else:
            st.success(f"✅ HAM (Not Spam) (Confidence: {confidence:.2f})")
    else:
        st.warning("Please enter a message to analyze.")
