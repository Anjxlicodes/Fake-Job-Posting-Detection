import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
import joblib
import plotly.express as px
from pathlib import Path
import json
BASE_DIR = Path(__file__).resolve().parent.parent

metrics_path = BASE_DIR / "artifacts" / "metrics.json"

results_path = BASE_DIR / "artifacts" / "model_results.csv"
with open(metrics_path) as f:
    metrics = json.load(f)
results = pd.read_csv(results_path)


st.set_page_config(page_title="Model Performance", layout="wide")

st.title("📈 Model Performance")
st.write(
    "Performance comparison of all machine learning models."
)
st.divider()


c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Accuracy",
    f"{metrics['accuracy']}%"
)

c2.metric(
    "Precision",
    f"{metrics['precision']}%"
)

c3.metric(
    "Recall",
    f"{metrics['recall']}%"
)

c4.metric(
    "F1 Score",
    f"{metrics['f1_score']}%"
)


st.subheader("📋 Model Comparison")
st.dataframe(
    results,
    use_container_width=True
)




fig = px.bar(
    results,
    x="Model",
    y="F1 Score",
    color="Model",
    text="F1 Score",
    title="Model Comparison (F1 Score)"
)
st.plotly_chart(
    fig,
    use_container_width=True
)




image_path = BASE_DIR / "images" / "confusion_matrix.png"

st.subheader("Confusion Matrix")

st.image(
    image_path,
    use_container_width=True
)

roc_path = BASE_DIR / "images" / "roc_curve.png"

st.subheader("ROC Curve")

st.image(
    roc_path,
    use_container_width=True
)

st.subheader("Model Comparison")
st.image(
    "images/model_comparison.png",
    use_container_width=True
)


st.subheader("🏆 Why Linear SVM (SVC)?")

st.success(
"""
Linear SVM (SVC) achieved the highest balance between Precision,
Recall and F1 Score.

Since this is a fraud detection problem, F1 Score and Recall
are more important than Accuracy.

The model also supports probability estimation,
allowing confidence scores to be displayed in the prediction page.
"""
)



st.sidebar.success("🟢 Model Loaded")

st.sidebar.info("Version 1.0")

st.sidebar.caption("© 2026 Anjali Pandey")