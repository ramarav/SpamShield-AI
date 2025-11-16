# SpamShield AI — SMS Spam Detector (ML + NLP + Streamlit)

SpamShield AI is a modern SMS Spam Detection system built using **Machine Learning, NLP, and Streamlit**.  
It classifies messages as **Spam** or **Ham (Not Spam)** using TF‑IDF + Logistic Regression and includes a clean UI.

---

## 🚀 Features
- ✔ Detects SMS spam with high accuracy  
- ✔ Clean, fast Streamlit UI  
- ✔ Real-time predictions  
- ✔ NLP preprocessing & TF‑IDF vectorization  
- ✔ Fully open-source and extensible  

---

## 🧠 Tech Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| Machine Learning | Scikit‑Learn | Spam classification |
| NLP | TF‑IDF Vectorizer | Text representation |
| Frontend | Streamlit | UI for predictions |
| Backend | Python | ML inference |
| Storage | joblib | Model persistence |

---

## 📦 Project Structure

```
SpamShield-AI/
│── data/
│   └── spam.csv
│── models/
│   └── spam_model.pkl
│── app.py
│── train.py
│── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/ramarav/SpamShield-AI
cd SpamShield-AI
pip install -r requirements.txt
```

---

## 🏋️‍♂️ Train the Model

```bash
python train.py
```

This creates:
```
models/spam_model.pkl
models/tfidf.pkl
```

---

## ▶️ Run the Streamlit App

```bash
streamlit run app.py
```

---

## 🧪 Example Output

- **Input:** "Congratulations! You've won a prize. Click claim now!"
- **Output:** Spam 🚫

---

## 📈 Future Enhancements
- Add LLM‑based explanations  
- Deploy as a web service  
- Add dashboard analytics  

---

## 🤝 Contributing
Pull requests are welcome.

---

## 📜 License
MIT License.
