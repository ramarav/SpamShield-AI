import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
from utils import clean_text

df = pd.read_csv("data/sms_spam.csv")

df['clean_text'] = df['message'].apply(clean_text)

X = df['clean_text']
y = df['label'].map({'ham': 0, 'spam': 1})

vectorizer = TfidfVectorizer(stop_words='english')
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

y_pred = model.predict(X_vec)
print(classification_report(y, y_pred))

joblib.dump(model, "models/spam_model.joblib")
joblib.dump(vectorizer, "models/vectorizer.joblib")

print("Training complete. Model saved.")
