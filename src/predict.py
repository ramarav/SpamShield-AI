import joblib
from utils import clean_text

model = joblib.load("models/spam_model.joblib")
vectorizer = joblib.load("models/vectorizer.joblib")

def predict_sms(text: str):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    
    prediction = model.predict(vec)[0]
    probability = model.predict_proba(vec)[0][prediction]

    return "Spam" if prediction == 1 else "Ham", float(probability)
