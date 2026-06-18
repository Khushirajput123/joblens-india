# 🔍 JobLens India — Data & AI Job Market Analytics

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://khushirajput123-joblens-india-appstreamlit-app-ulhuwr.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![SQLite](https://img.shields.io/badge/Database-SQLite-green?logo=sqlite)
![Streamlit](https://img.shields.io/badge/Streamlit-1.58-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> A real-time job market analytics dashboard that tracks hiring trends for Data & AI roles across India — built with an end-to-end ETL pipeline from API to interactive dashboard.

---

## 🚀 Live Demo

🔗 **[View Live Dashboard →](https://khushirajput123-joblens-india-appstreamlit-app-ulhuwr.streamlit.app)**

---

## 📌 What It Does

JobLens India fetches live job listings from the JSearch API, cleans and stores them in a SQLite database, and displays interactive hiring insights on a Streamlit dashboard.

| Feature | Description |
|---|---|
| 📊 160+ Live Job Listings | Real job data fetched from JSearch API across India |
| 🏙️ City-wise Breakdown | Top hiring cities — Bengaluru, Hyderabad, Pune, Mumbai and more |
| 🏢 Company Rankings | Top companies actively hiring for Data & AI roles |
| 🎯 Role Filter | Filter by Data Analyst, ML Engineer, Data Scientist, and more |
| 📈 Interactive Charts | Built with Plotly — bar charts, pie charts, company rankings |
| 🗄️ SQL-powered Backend | Full ETL pipeline with SQLite — raw → clean → dashboard |

---

## 🏗️ Architecture

```
JSearch API
     ↓
scraper/fetchjobs.py      →    SQLite (jobs_raw table)
     ↓
analysis/clean_data.py    →    SQLite (jobs_clean table)
     ↓
app/streamlit_app.py      →    Interactive Dashboard
     ↓
Streamlit Cloud           →    Live on Internet
```

---

## 📁 Project Structure

```
joblens-india/
├── scraper/
│   ├── fetchjobs.py           # Fetches jobs from JSearch API
│   └── data/
│       └── joblens.db         # SQLite database
├── analysis/
│   └── clean_data.py          # Cleans and transforms raw data
├── app/
│   └── streamlit_app.py       # Streamlit dashboard
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python** | Core language |
| **Pandas** | Data cleaning and transformation |
| **SQLite** | Local database — raw and clean tables |
| **Requests** | REST API calls to JSearch |
| **Streamlit** | Interactive web dashboard |
| **Plotly** | Data visualizations |
| **Streamlit Cloud** | Free cloud deployment |

---

## 🚀 Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Khushirajput123/joblens-india.git
cd joblens-india
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your API key
Create a `.env` file:
```
RAPIDAPI_KEY=your_rapidapi_key_here
```
Get your free key at [rapidapi.com](https://rapidapi.com) → search JSearch.

### 4. Run the pipeline
```bash
python scraper/fetchjobs.py     # Step 1: Fetch data
python analysis/clean_data.py   # Step 2: Clean data
streamlit run app/streamlit_app.py  # Step 3: Launch dashboard
```

Open **http://localhost:8501** in your browser.

---

## 📊 Data Pipeline — How It Works

### Step 1 — Fetch (`fetchjobs.py`)
- Calls JSearch RapidAPI for 6 role categories
- Fetches 5 pages per role across major Indian cities
- Handles rate limiting with 1.5s delay between API calls
- Saves raw data to `jobs_raw` table in SQLite

### Step 2 — Clean (`clean_data.py`)
- Removes duplicate listings by `job_id`
- Filters India-only jobs (`job_country == "IN"`)
- Converts date strings to datetime format
- Categorizes roles into standard buckets
- Saves clean data to `jobs_clean` table

### Step 3 — Visualize (`streamlit_app.py`)
- Reads from `jobs_clean` table via Pandas + SQL
- Sidebar filters for role and city
- Metric cards, bar charts, pie charts, company leaderboard

---

## 📈 Roles Tracked

`Data Analyst` · `Data Scientist` · `ML Engineer` · `Data Engineer` · `Business Analyst` · `AI Engineer`

---

## 💡 Key Learnings

- End-to-end ETL pipeline from REST API to production dashboard
- REST API integration with pagination and rate limiting
- Data cleaning and deduplication with Pandas
- SQLite schema design — raw vs clean table separation
- Interactive dashboard development with Streamlit and Plotly
- Cloud deployment via GitHub + Streamlit Cloud

---

## 👩‍💻 Author

**Khushi Rajput**

[![GitHub](https://img.shields.io/badge/GitHub-Khushirajput123-black?logo=github)](https://github.com/Khushirajput123)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/khushirajput)
[![LeetCode](https://img.shields.io/badge/LeetCode-1600%2B_Rating-orange?logo=leetcode)](https://leetcode.com/khushirajput)

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

