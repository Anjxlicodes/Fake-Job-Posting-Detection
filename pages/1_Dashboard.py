import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Dashboard", layout="wide")

df = pd.read_csv("data/fake_job_processed.csv")

st.title("📊 Dataset Dashboard")

st.markdown(
"""
Explore the dataset through interactive visualizations.
"""
)
st.divider()


total_jobs = len(df)

real_jobs = (df["fraudulent"] == 0).sum()

fake_jobs = (df["fraudulent"] == 1).sum()

accuracy = 97.99

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Jobs", total_jobs)

c2.metric("Real Jobs", real_jobs)

c3.metric("Fake Jobs", fake_jobs)

c4.metric("Accuracy", f"{accuracy}%")


pie = px.pie(
    df,
    names="fraudulent",
    title="Real vs Fake Jobs",
    color="fraudulent",
    color_discrete_map={
        0: "#2ecc71",
        1: "#e74c3c"
    }
)

st.plotly_chart(pie, use_container_width=True)




employment = (
    df["employment_type"]
    .value_counts()
    .reset_index()
)

employment.columns = ["Employment Type", "Count"]

fig = px.bar(
    employment,
    x="Employment Type",
    y="Count",
    title="Employment Types"
)

st.plotly_chart(fig, use_container_width=True)

df["country"] = df["location"].str.split(",").str[0]
country = (
    df["country"]
    .value_counts()
    .head(10)
    .reset_index()
)

country.columns = ["Country", "Jobs"]

fig = px.bar(
    country,
    x="Country",
    y="Jobs",
    title="Top Countries"
)

st.plotly_chart(fig, use_container_width=True)







from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = " ".join(df["clean_text"])

wordcloud = WordCloud(
    width=900,
    height=500,
    background_color="white"
).generate(text)

fig, ax = plt.subplots(figsize=(12,6))

ax.imshow(wordcloud)

ax.axis("off")

st.pyplot(fig)




st.subheader("Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)





st.sidebar.success("🟢 Model Loaded")

st.sidebar.info("Version 1.0")

st.sidebar.caption("© 2026 Anjali Pandey")