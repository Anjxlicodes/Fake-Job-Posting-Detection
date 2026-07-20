import streamlit as st
from pathlib import Path
from streamlit_card import card

st.set_page_config(
    page_title="Fake Job Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Load CSS ----------
css = Path("styles/style.css")
with open(css) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ---------- Sidebar ----------
st.sidebar.title("🛡️ Fake Job Detector")
ASSETS = Path(__file__).parent / "assets"

st.sidebar.image(
    ASSETS / "logo.png",
    use_container_width=True
)
st.sidebar.markdown("## Fake Job Detector")
st.sidebar.caption("AI Powered Fraud Detection")

st.sidebar.info(
    """
    **Machine Learning + NLP**

    Detect whether a job posting is **Genuine** or **Fraudulent**.
    """
)

st.sidebar.success("Model: Linear SVM")
st.sidebar.divider()

st.sidebar.success("✔ AI Model Ready")

st.sidebar.info("Version 1.0")

st.sidebar.caption("Developed by Anjali Pandey")
# ---------- Hero ----------

col1, col2 = st.columns([2,1])

with col1:

    st.title("🛡 Fake Job Posting Detection")

    st.markdown("""
### AI Powered Fraud Detection

Detect fraudulent job advertisements using
Machine Learning and Natural Language Processing.

✔ Fast Prediction

✔ High Accuracy

✔ Explainable Results
""")

with col2:

    st.image(
        "assets/hero.png",
        use_container_width=True
    )

# ---------- Quick Actions ----------
st.markdown("## 🚀 Quick Actions")
c1, c2, c3,c4 = st.columns([1.2, 1.2, 1.2, 1])

with c1:
    if st.button("🚀 Start Prediction", use_container_width=True):
        st.switch_page("pages/2_Predict.py")

with c2:
    if st.button("📊 View Dashboard", use_container_width=True):
        st.switch_page("pages/1_Dashboard.py")
with c3:
    if st.button("📈 ModelPerformance", use_container_width=True):
        st.switch_page("pages/3_Model_Performance.py")
    
st.markdown("<br>", unsafe_allow_html=True)

# ---------- Metrics ----------
st.markdown("## 📈 Project Statistics")
col1, col2, col3, col4 = st.columns(4)

col1.metric("📁 Dataset", "17,880")
# col2.metric("🧠 Features", "18")
col2.metric("🎯 Accuracy", "97.99%")
# col4.metric("🟢 Genuine Jobs", "17,014")
col3.metric("🔴 Fake Jobs", "866")
col4.metric("🏆 Best Model", "Linear SVM")

st.markdown("<br>", unsafe_allow_html=True)

# ---------- Feature Cards ----------
st.subheader("✨ Features")

col1, col2, col3 = st.columns(3)

with col1:
    if card(
        title="🔍 Smart Prediction",
        text="Analyze job advertisements instantly using NLP and classify them as Genuine or Fraudulent.",
        styles={
            "card": {
                "width": "100%",
                "height": "340px",
                "padding": "32px",
                "border-radius": "26px",
                "background": "linear-gradient(145deg,#2563EB,#4F46E5,#7C3AED)",
                "border": "1.5px solid rgba(255,255,255,0.12)",
                "box-shadow": "0 20px 45px rgba(0,0,0,0.35)",
                "display": "flex",
                "flex-direction": "column",
                "justify-content": "center",
                "align-items": "center",
                "text-align": "center",
                "transition": "all 0.35s ease",
                "cursor": "pointer"
            },

            "title": {
                "font-size": "32px",
                "font-weight": "800",
                "color": "#FFFFFF",
                "margin-bottom": "18px",
                "line-height": "1.3",
                "letter-spacing": "0.4px"
            },

            "text": {
                "font-size": "17px",
                "font-weight": "400",
                "line-height": "1.8",
                "color": "#E2E8F0",
                "padding": "0 8px"
            }
        },
        key="prediction_card"
    ):
        st.switch_page("pages/2_Predict.py")

with col2:
    if card(
        title="📊 Interactive Dashboard",
        text="Explore dataset insights, visualizations and fraud statistics.",
        styles={
            "card": {
                "width": "100%",
                "height": "340px",
                "padding": "32px",
                "border-radius": "26px",
                "background": "linear-gradient(145deg,#059669,#0891B2,#2563EB)",
                "border": "1.5px solid rgba(255,255,255,0.12)",
                "box-shadow": "0 20px 45px rgba(0,0,0,0.35)",
                "display": "flex",
                "flex-direction": "column",
                "justify-content": "center",
                "align-items": "center",
                "text-align": "center",
                "transition": "all 0.35s ease",
                "cursor": "pointer"
            },

            "title": {
                "font-size": "32px",
                "font-weight": "800",
                "color": "#FFFFFF",
                "margin-bottom": "18px",
                "line-height": "1.3",
                "letter-spacing": "0.4px"
            },

            "text": {
                "font-size": "17px",
                "font-weight": "400",
                "line-height": "1.8",
                "color": "#E2E8F0",
                "padding": "0 8px"
            }
        },
        key="dashboard_card"
    ):
        st.switch_page("pages/1_Dashboard.py")

with col3:
    if card(
        title="🤖 AI Insights",
        text="Understand why the model classified a job posting as fake or genuine.",
        styles={
            "card": {
                "width": "100%",
                "height": "340px",
                "padding": "32px",
                "border-radius": "26px",
                "background": "linear-gradient(145deg,#F59E0B,#EA580C,#DC2626)",
                "border": "1.5px solid rgba(255,255,255,0.12)",
                "box-shadow": "0 20px 45px rgba(0,0,0,0.35)",
                "display": "flex",
                "flex-direction": "column",
                "justify-content": "center",
                "align-items": "center",
                "text-align": "center",
                "transition": "all 0.35s ease",
                "cursor": "pointer"
            },

            "title": {
                "font-size": "32px",
                "font-weight": "800",
                "color": "#FFFFFF",
                "margin-bottom": "18px",
                "line-height": "1.3",
                "letter-spacing": "0.4px"
            },

            "text": {
                "font-size": "17px",
                "font-weight": "400",
                "line-height": "1.8",
                "color": "#E2E8F0",
                "padding": "0 8px"
            }
        },
        key="insights_card"
    ):
        st.switch_page("pages/3_AI_Insights.py")

st.markdown("---")

st.header("⭐ Why Choose This System?")

left,right = st.columns(2)

with left:

    st.markdown("""
✅ Machine Learning Powered

✅ NLP Based Detection

✅ Confidence Score

✅ PDF Report Generation
""")

with right:

    st.markdown("""
✅ Fraud Probability

✅ AI Insights

✅ Interactive Dashboard

✅ Easy to Use
""")
    
    
st.markdown("""
<hr>

<div style='text-align:center;color:#94A3B8;font-size:15px;'>

Developed by <b>Anjali Pandey</b>

<br>

Made with ❤️ using Streamlit | Machine Learning | NLP

</div>
""", unsafe_allow_html=True)