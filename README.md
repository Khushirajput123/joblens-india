# JobLens India 🔍
> Real-time Data & AI Job Market Analytics Dashboard for India

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.58-red)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌐 Live Demo
**[View Live Dashboard →](https://khushirajput123-joblens-india-appstreamlit-app-ulhuwr.streamlit.app)**

---

## 📌 What It Does

JobLens India tracks real-time hiring trends for Data & AI roles across India. It fetches live job listings from the JSearch API, cleans and stores them in a SQLite database, and displays interactive insights on a Streamlit dashboard.

- Browse **160+ live job listings** across India
- Filter by **role category** and **city**
- See **top hiring companies**, city trends, and role breakdown
- Data refreshed by re-running the fetch pipeline

---

## 🖥️ Dashboard Preview

| Metric Cards | Charts |
|---|---|
| Total Jobs, Companies, Cities, Roles | Jobs by Role, Top 10 Cities, Top Companies |

---

## 🏗️ Project Architecture

```
JSearch API
    ↓
scraper/fetchjobs.py     →   scraper/data/joblens.db  (jobs_raw table)
    ↓
analysis/clean.data.py   →   scraper/data/joblens.db  (jobs_clean table)
    ↓
app/streamlit_app.py     →   reads jobs_clean → interactive dashboard
    ↓
Streamlit Cloud          →   live on internet via GitHub
```

---

## 📁 Project Structure

```
joblens-india/
├── scraper/
│   ├── fetchjobs.py          # Fetches jobs from JSearch API
│   └── data/
│       └── joblens.db        # SQLite database
├── analysis/
│   └── clean.data.py         # Cleans and transforms raw data
├── app/
│   └── streamlit_app.py      # Streamlit dashboard
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas | Data cleaning and transformation |
| SQLite | Local database storage |
| Streamlit | Interactive web dashboard |
| Plotly | Data visualizations |
| Requests | REST API calls |
| Git + GitHub | Version control and deployment |
| Streamlit Cloud | Free cloud hosting |

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Khushirajput123/joblens-india.git
cd joblens-india
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Fetch job data
```bash
python scraper/fetchjobs.py
```

### 4. Clean the data
```bash
python analysis/clean.data.py
```

### 5. Run the dashboard
```bash
streamlit run app/streamlit_app.py
```

Open **http://localhost:8501** in your browser.

---

## 📊 Data Pipeline

### Step 1 — Fetch (fetchjobs.py)
- Calls JSearch RapidAPI for 6 role categories
- Fetches 5 pages per role (50 jobs per role)
- Saves raw JSON data to `jobs_raw` table in SQLite
- Handles rate limiting with 1.5s delay between calls

### Step 2 — Clean (clean.data.py)
- Removes duplicate job listings by `job_id`
- Filters India-only jobs (`job_country == "IN"`)
- Converts date strings to datetime format
- Categorizes roles: Data Analyst, Data Scientist, ML Engineer, Data Engineer, Business Analyst, AI Engineer
- Saves cleaned data to `jobs_clean` table

### Step 3 — Visualize (streamlit_app.py)
- Reads from `jobs_clean` table
- Sidebar filters for role and city
- Metric cards, bar charts, company rankings, job listings table

---

## 📈 Role Categories Tracked

- Data Analyst
- Data Scientist
- Data Engineer
- ML Engineer
- Business Analyst
- AI Engineer

---

## 🏙️ Top Cities Covered

Bengaluru · Hyderabad · Pune · Gurugram · Mumbai · Chennai · New Delhi · Kolkata

---

## 🔮 Future Improvements

- [ ] Salary insights chart using `job_min_salary` data
- [ ] GitHub Actions for daily auto-fetch
- [ ] Job description keyword/skills extractor
- [ ] Email alerts for new job listings
- [ ] Trend over time — weekly hiring patterns
- [ ] Expand to US, UK, Canada markets
- [ ] Migrate from SQLite to PostgreSQL

---

## 💡 Key Learnings

- Building end-to-end ETL pipelines from scratch
- REST API integration with pagination and rate limiting
- Data cleaning and transformation with Pandas
- SQLite database management
- Interactive dashboard development with Streamlit
- Cloud deployment with GitHub CI/CD

---

## 👤 Author

**Khushirajput123**
- GitHub: [@Khushirajput123](https://github.com/Khushirajput123)

---

## 📄 License

This project is open source under the [MIT License](LICENSE).
