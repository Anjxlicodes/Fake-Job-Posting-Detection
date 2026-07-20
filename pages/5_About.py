import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About the Project")

st.markdown("""
Welcome to the **Fake Job Posting Detection System**.

This project uses **Machine Learning** and **Natural Language Processing (NLP)** to identify whether a job posting is genuine or fraudulent.
""")

st.divider()

# Project Overview
st.header("📌 Project Overview")

st.write("""
The increasing number of online job portals has made job searching easier, but it has also increased the number of fake job advertisements.

This project aims to detect fraudulent job postings using Machine Learning models trained on textual information extracted from job advertisements.

The application helps users identify potentially fraudulent jobs before applying.
""")

# Dataset Information
st.header("📂 Dataset")

st.write("""
**Dataset Name:**
Fake Job Posting Prediction Dataset

**Source:**
Kaggle

**Total Records:**
17,880

**Target Variable:**
Fraudulent (0 = Genuine, 1 = Fake)
""")

# Technologies Used
st.header("🛠️ Technologies Used")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
""")

with col2:

    st.markdown("""
- Streamlit
- Plotly
- Matplotlib
- WordCloud
- Joblib
""")
    
# Machine Learning Workflow
st.header("⚙️ Machine Learning Workflow")

st.markdown("""
1. Data Collection

2. Data Cleaning

3. Text Preprocessing

4. TF-IDF Vectorization

5. Train-Test Split

6. Model Training

7. Model Evaluation

8. Best Model Selection

9. Streamlit Deployment
""")


# Models Tested
st.header("🤖 Machine Learning Models")

st.table({
    "Model":[
        "Logistic Regression",
        "Naive Bayes",
        "Random Forest",
        "Linear SVM (SVC)"
    ],
    "Purpose":[
        "Baseline Model",
        "Probabilistic Classifier",
        "Ensemble Learning",
        "Final Selected Model"
    ]
})


# Why Linear SVM?
st.header("🏆 Why Linear SVM (SVC)?")

st.success("""
The Linear SVM (SVC) model was selected because it achieved the highest overall performance on the dataset.

It provided:

✅ High Accuracy

✅ High Recall

✅ Best F1 Score

✅ Probability Estimates

These characteristics make it well-suited for fraud detection tasks where balancing precision and recall is important.
""")

# Future Enhancements
st.header("🚀 Future Scope")

st.markdown("""
Future improvements can include:

- Deep Learning (LSTM/BERT)

- Real-time Job URL Analysis

- Browser Extension

- Email Scam Detection

- Multilingual Support

- Cloud Deployment
""")

# Developer Details
st.header("👨‍💻 Developer")

st.info("""
**Name:** Anjali Pandey

**Roll No:** 240004

**Department:** Computer Science Engineering

**Project:** Fake Job Posting Detection using Machine Learning and NLP
""")



st.markdown("""
<hr>

<div style='text-align:center;color:#94A3B8;font-size:15px;'>

Developed by <b>Anjali Pandey</b>

<br>
Made with ❤️ using Streamlit | Machine Learning | NLP
</div>
""", unsafe_allow_html=True)

st.sidebar.success("🟢 Model Loaded")

st.sidebar.info("Version 1.0")

st.sidebar.caption("© 2026 Anjali Pandey")