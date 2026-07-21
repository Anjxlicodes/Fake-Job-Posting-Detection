"""
Prediction Page

This page accepts job posting information,
preprocesses the text,
loads the trained SVC model,
and predicts whether the job is genuine or fraudulent.
"""

import streamlit as st
from utils.insights import get_insights
from utils.pdf_generator import generate_report
from utils.sample_data import GENUINE_JOB, FAKE_JOB
from datetime import datetime
from utils.scam_analyzer import analyze_text

st.set_page_config(
    page_title="Prediction",
    layout="wide"
)

st.title("🔍 Fake Job Prediction")

st.write(
    "Fill in the job information below to determine whether the posting is genuine or fraudulent."
)

st.divider()

if "title" not in st.session_state:
    st.session_state.title = ""
    st.session_state.company = ""
    st.session_state.description = ""
    st.session_state.requirements = ""
    st.session_state.benefits = ""
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🟢 Load Genuine Example"):
        st.session_state.title = GENUINE_JOB["title"]
        st.session_state.company = GENUINE_JOB["company"]
        st.session_state.description = GENUINE_JOB["description"]
        st.session_state.requirements = GENUINE_JOB["requirements"]
        st.session_state.benefits = GENUINE_JOB["benefits"]

        st.rerun()

with col2:
    if st.button("🔴 Load Fraudulent Example"):
        st.session_state.title = FAKE_JOB["title"]
        st.session_state.company = FAKE_JOB["company"]
        st.session_state.description = FAKE_JOB["description"]
        st.session_state.requirements = FAKE_JOB["requirements"]
        st.session_state.benefits = FAKE_JOB["benefits"]

        st.rerun()
with col3:
    if st.button("🗑️ Clear Form"):
        st.session_state.title = ""
        st.session_state.company = ""
        st.session_state.description = ""
        st.session_state.requirements = ""
        st.session_state.benefits = ""

        st.rerun()

with st.form("prediction_form"):

    title = st.text_input(
        "Job Title",
        key="title"
    )

    company = st.text_area(
        "Company Profile",
        key="company"
    )

    description = st.text_area(
        "Job Description",
        height=220,
        key="description"
    )

    requirements = st.text_area(
        "Requirements",
        key="requirements"
    )

    benefits = st.text_area(
        "Benefits",
        key="benefits"
    )

    submitted = st.form_submit_button("Predict")



if submitted:

    from utils.preprocessing import clean_text
    from utils.model_loader import model, vectorizer

    # Validation
    if not title.strip():
        st.error("Please enter the Job Title.")
        st.stop()

    if not description.strip():
        st.error("Please enter the Job Description.")
        st.stop()

    combined = " ".join([
        title,
        company,
        description,
        requirements,
        benefits
    ]).strip()
    # Analyze suspicious keywords
    detected_keywords, keyword_score, keyword_level = analyze_text(combined)
    if not combined:
        st.warning("Please enter job information.")
        st.stop()

    # Preprocess
    cleaned = clean_text(combined)

    # Vectorize
    vector = vectorizer.transform([cleaned])
    # Ensure enough recognizable vocabulary
    if vector.nnz < 10:
        st.warning(
            "The entered text contains too few recognizable words. "
            "Please enter a complete and meaningful job posting."
        )
        st.stop()

    # Predict
    import time

    with st.spinner("🔍 Analyzing Job Posting..."):
        time.sleep(2)
        prediction = model.predict(vector)[0]
    probabilities = model.predict_proba(vector)[0]
    confidence = probabilities.max() * 100
    positive, warnings, recommendation = get_insights(
    combined,
    prediction
    )
    
    fake_probability = probabilities[1] * 100
    real_probability = probabilities[0] * 100
    # Hybrid Risk Score
    hybrid_score = (fake_probability * 0.7) + (keyword_score * 0.3)

    if hybrid_score < 30:
        final_level = "LOW"
    elif hybrid_score < 70:
        final_level = "MEDIUM"
    else:
        final_level = "HIGH"


    # Show Positive Indicators
    st.subheader("✅ Positive Indicators")
    if positive:
        for item in positive:
            st.success(item)
    else:
        st.info("No strong positive indicators detected.")

    # Show Warning Signs
    st.subheader("⚠ Warning Signs")
    if warnings:
        for item in warnings:
            st.warning(item)
    else:
        st.success("No suspicious keywords detected.")

    # Show Recommendation
    st.subheader("💡 AI Recommendation")

    if final_level == "LOW":

        st.success("""
    The posting appears legitimate based on both the machine learning model and the keyword analysis.

    Even so, always verify the employer before sharing personal information.
    """)

    elif final_level == "MEDIUM":

        st.warning("""
    The posting contains some suspicious characteristics.

    Research the company carefully, confirm the contact details, and avoid paying any fees.
    """)

    else:

        st.error("""
    The posting has a high fraud risk according to the combined analysis.

    Avoid sending money or sensitive documents until the employer's authenticity is verified.
    """)



    st.divider()

    col1, col2 = st.columns([2, 1])

    with col1:

        if prediction == 0:
            st.success("✅ Genuine Job Posting")
        else:
            st.error("🚨 Fraudulent Job Posting")

    with col2:
        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

    st.subheader("Prediction Probability")

    st.progress(fake_probability / 100)

    col1, col2 = st.columns(2)

    col1.metric(
        "Real Job",
        f"{real_probability:.2f}%"
    )

    col2.metric(
        "Fake Job",
        f"{fake_probability:.2f}%"
    )
    st.divider()

    st.subheader("🤖 AI Risk Analysis")
    col1,col2 = st.columns(2)

    with col1:
        st.metric(
            "ML Fraud Probability",
            f"{fake_probability:.2f}%"
        )
    st.divider()
    st.subheader("🤖 Hybrid AI Analysis")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Hybrid Risk Score",
            f"{hybrid_score:.2f}%"
        )

    with c2:
        if final_level == "LOW":
            st.success("🟢 LOW RISK")
        elif final_level == "MEDIUM":
            st.warning("🟡 MEDIUM RISK")
        else:
            st.error("🔴 HIGH RISK")

    st.subheader("⚠ Suspicious Keywords")
    if detected_keywords:
        for word in detected_keywords:
            st.error(f"🔴 {word}")
    else:
        st.success("✅ No suspicious keywords detected.")


    now = datetime.now()
    current_time = now.strftime("%d-%m-%Y %H:%M")
    report_file = "prediction_report.pdf"
    generate_report(
        current_time,
        report_file,
        title,
        "Genuine Job Posting" if prediction == 0 else "Fraudulent Job Posting",
        hybrid_score,
        final_level,
        detected_keywords,
        confidence,
        real_probability,
        fake_probability,
        positive,
        warnings,
        recommendation
    )
    with open(report_file, "rb") as file:
        st.download_button(
            label="📄 Download Prediction Report",
            data=file,
            file_name="prediction_report.pdf",
            mime="application/pdf"
        )





st.sidebar.success("🟢 Model Loaded")

st.sidebar.info("Version 1.0")

st.sidebar.caption("© 2026 Anjali Pandey")