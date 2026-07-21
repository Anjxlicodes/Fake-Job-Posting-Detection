import streamlit as st
import pandas as pd
import json
from pathlib import Path
from utils.scam_analyzer import analyze_text
from utils.model_loader import vectorizer
from utils.preprocessing import clean_text

st.set_page_config(
    page_title="AI Insights",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Insights")
st.write("Understand how the system detects fraudulent job postings and learn how to identify scams.")
st.divider()

st.header("🚨 Common Characteristics of Fake Job Postings")

col1, col2 = st.columns(2)

with col1:
    st.error("""
### Warning Signs

- Unrealistic salary
- No company details
- Immediate joining
- Registration fee
- WhatsApp/Telegram only
- Vague job description
""")

with col2:
    st.success("""
### Genuine Job Indicators

- Verified company profile
- Professional language
- Detailed responsibilities
- Required skills mentioned
- Employee benefits
- Official contact information
""")
    
st.header("⚠ Common Scam Keywords")

keywords = [
    "Earn Money Fast",
    "Registration Fee",
    "Immediate Joining",
    "Work From Home",
    "No Experience",
    "Limited Seats",
    "WhatsApp",
    "Telegram",
    "Investment",
    "Quick Money"
]

st.write("These keywords frequently appear in fraudulent job advertisements.")

st.table(pd.DataFrame({"Suspicious Keywords": keywords}))

st.header("🛡 Safety Tips")

tips = [
    "Never pay money to apply for a job.",
    "Verify the company's official website.",
    "Avoid offers with unrealistic salaries.",
    "Research the employer on LinkedIn.",
    "Do not share Aadhaar, PAN or bank details immediately.",
    "Apply only through trusted job portals."
]

for tip in tips:
    st.success("✔ " + tip)

st.header("🤖 How Our AI Detects Fake Jobs")

st.info("""
### Detection Pipeline

1. Job details are entered.

2. Text is cleaned and preprocessed.

3. TF-IDF converts text into numerical features.

4. The trained Linear SVM (SVC) model predicts:

• Genuine Job

or

• Fraudulent Job

5. Confidence score and recommendations are displayed.
""")

st.header("🔄 Machine Learning Workflow")

st.markdown("""
Raw Dataset
│
▼
Data Cleaning
│
▼
Text Preprocessing
│
▼
TF-IDF Vectorization
│
▼
Train-Test Split
│
▼
Model Training
│
▼
Prediction
│
▼
AI Insights
            """)


BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "artifacts" / "dataset_info.json") as f:
    data = json.load(f)

    st.header("📊 Dataset Overview")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Jobs", data["total_jobs"])
    c2.metric("Genuine Jobs", data["real_jobs"])
    c3.metric("Fraudulent Jobs", data["fake_jobs"])


if "analyzer_text" not in st.session_state:
    st.session_state.analyzer_text = ""
st.divider()

st.header("📝 Interactive Scam Analyzer")

st.write(
    "Paste a job advertisement below or load one of the sample examples to analyze suspicious keywords."
)
col1, col2 = st.columns(2)
if "analyzer_text" not in st.session_state:
    st.session_state.analyzer_text = ""
col1, col2, col3 = st.columns(3)

with col1:

    if st.button("🟢 Load Genuine Example"):

        st.session_state.analyzer_text = """
ABC Technologies Pvt Ltd is hiring Python Developers.

Requirements:
Python
Django
REST APIs
Git

Benefits:
Health Insurance
Flexible Hours
Remote Work
"""

with col2:

    if st.button("🔴 Load Scam Example"):

        st.session_state.analyzer_text = """
Earn ₹50,000 per week!

No experience required!

Immediate joining!

Limited seats!

Pay registration fee.

WhatsApp now.
"""

with col3:

    if st.button("🗑️ Clear"):

        st.session_state.analyzer_text = ""

        st.rerun()
with st.form("scam_form"):

    user_text = st.text_area(
        "Paste Job Advertisement",
        key="analyzer_text",
        height=220
    )

    submitted = st.form_submit_button(
        "🔍 Analyze Text"
    )
if submitted:
    import time

    with st.spinner("🤖 AI is analyzing the job posting..."):

        time.sleep(2)
    if not user_text.strip():

        st.warning("⚠️ Please enter some text to analyze.")

    if len(user_text.strip()) < 100:
            st.warning(
                "Please enter at least 100 characters for reliable analysis."
            )
            st.stop()
    else:
        
        cleaned = clean_text(user_text)
        vector = vectorizer.transform([cleaned])
        if vector.nnz < 10:
            st.warning(
                """
        The entered text does not contain enough recognizable job-related content.

        Please paste a complete job advertisement.
        """
            )
            st.stop()

        detected, score, level = analyze_text(user_text)
        st.divider()

        st.subheader("📋 Analysis Result")
        st.subheader("⚠️ Suspicious Keywords")

        if detected:

            for word in detected:

                st.error(f"🔴 {word}")

        else:

            st.success("✅ No suspicious keywords detected.")
        st.subheader("📊 Risk Score")

        st.progress(score / 100)

        col1, col2 = st.columns([1,1])

        with col1:

            st.metric(
                "Risk Score",
                f"{score}%"
            )

        with col2:

            if level == "LOW":

                st.success("🟢 LOW RISK")

            elif level == "MEDIUM":

                st.warning("🟡 MEDIUM RISK")

            else:

                st.error("🔴 HIGH RISK")
                st.subheader("💡 AI Explanation")

        if detected:

            st.info(
                f"""
The analyzer detected **{len(detected)} suspicious keyword(s)**.

This does **not** mean the posting is definitely fraudulent,
but these keywords frequently appear in fake job advertisements.

Always verify the employer before applying.
"""
            )

        


st.header("💡 Future Improvements")

st.warning("""
Future versions of this project may include:

• BERT-based NLP models

• Deep Learning (LSTM)

• Real-time URL scanning

• Browser extension

• Resume fraud detection

• Explainable AI (SHAP/LIME)

• Cloud deployment
""")

st.divider()

st.caption(
    "🤖 AI Insights | Fake Job Posting Detection System"
)


st.sidebar.success("🟢 Model Loaded")

st.sidebar.info("Version 1.0")

st.sidebar.caption("© 2026 Anjali Pandey")