import streamlit as st
import pandas as pd
import plotly.express as px
import os
import sqlite3


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "scraper", "data", "joblens.db")

st.set_page_config(page_title="JobLens India", page_icon="🔍", layout="wide")
st.title("🔍 JobLens India — Data & AI Jobs Dashboard")

# Load data — single connection using absolute path
conn = sqlite3.connect(DB_PATH)
df = pd.read_sql("SELECT * FROM jobs_clean", conn)
conn.close()

# Sidebar filters
st.sidebar.header("Filters")
roles = st.sidebar.multiselect("Role", df["role_category"].unique(), default=df["role_category"].unique())
cities = st.sidebar.multiselect("City", df["job_city"].dropna().unique())

filtered = df[df["role_category"].isin(roles)]
if cities:
    filtered = filtered[filtered["job_city"].isin(cities)]

# Metrics row
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Jobs", len(filtered))
col2.metric("Companies", filtered["employer_name"].nunique())
col3.metric("Cities", filtered["job_city"].nunique())
col4.metric("Roles", filtered["role_category"].nunique())

st.divider()

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Jobs by Role")
    fig = px.bar(filtered["role_category"].value_counts().reset_index(),
                 x="role_category", y="count", color="role_category")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Top 10 Cities")
    city_data = filtered["job_city"].value_counts().head(10).reset_index()
    fig2 = px.bar(city_data, x="job_city", y="count")
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Top Hiring Companies")
company_data = filtered["employer_name"].value_counts().head(15).reset_index()
fig3 = px.bar(company_data, x="count", y="employer_name", orientation="h")
st.plotly_chart(fig3, use_container_width=True)

# Job table
st.subheader("Job Listings")
st.dataframe(
    filtered[["job_title", "employer_name", "job_city", "role_category",
              "job_employment_type", "job_posted_at_datetime_utc"]].sort_values(
        "job_posted_at_datetime_utc", ascending=False
    ),
    use_container_width=True
)