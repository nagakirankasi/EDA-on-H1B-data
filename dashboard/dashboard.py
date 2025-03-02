import streamlit as st
import pandas as pd

# Load processed data
DATA_PATH = "data/processed/h1b_cleaned_2024.csv"
df = pd.read_csv(DATA_PATH)

# Dashboard Title
st.title("H1B Visa Analysis Dashboard")

# Overview Metrics
st.subheader("Key Metrics")
col1, col2 = st.columns(2)
col1.metric("Total Applications", df.shape[0])
col2.metric("Total Employers", df["employer_(petitioner)_name"].nunique())

# Industry-wise approvals
st.subheader("Approvals by Industry")
industry_counts = df.groupby("industry_(naics)_code")["initial_approval"].sum().reset_index()
st.bar_chart(industry_counts.set_index("industry_(naics)_code"))

# State-wise H1B Trends
st.subheader("H1B Approvals by State")
st.map(df.rename(columns={"petitioner_city": "latitude", "petitioner_state": "longitude"}))

st.write("### Data Preview")
st.dataframe(df.head())

if __name__ == "__main__":
    st.write("Run `streamlit run scripts/dashboard.py` to start the dashboard.")
