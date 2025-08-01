import streamlit as st
import pandas as pd

st.set_page_config(page_title="Court Case Dashboard", layout="wide")

st.title("📄 Court Case Dashboard")

try:
    df = pd.read_csv("court_cases.csv")
    st.success("CSV loaded successfully!")

    case_filter = st.text_input("Search by Case Number", "")
    if case_filter:
        df = df[df["Case No"].str.contains(case_filter, case=False)]

    st.dataframe(df)

    st.download_button("Download as CSV", data=df.to_csv(index=False), file_name="filtered_cases.csv")
except FileNotFoundError:
    st.warning("Please run scraper.py to generate court_cases.csv")
