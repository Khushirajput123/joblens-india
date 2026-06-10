


import requests
import pandas as pd
import sqlite3
import time
import os

BASE_DIR = r"C:\Users\sumit\PycharmProjects\PythonProject1"
os.makedirs(os.path.join(BASE_DIR, "data"), exist_ok=True)
conn = sqlite3.connect(os.path.join(BASE_DIR, "scraper","data", "joblens.db"))


API_KEY = "693b588d2cmshe717d3ecbb4d05fp19162fjsnace3b1bef9ce"  # ← paste your key here

roles = [
    "Data Analyst India",
    "Data Scientist India",
    "ML Engineer India",
    "Business Analyst India",
    "Data Engineer India",
    "AI Engineer India"
]

all_jobs = []

for role in roles:
    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    # Fetch multiple pages per role
    for page in range(1, 6):  # 5 pages × 10 jobs = 50 per role
        params = {
            "query": role,
            "page": str(page),
            "num_pages": "1",
            "date_posted": "month"
        }
        try:
            response = requests.get(url, headers=headers, params=params)
            data = response.json()
            jobs = data.get("data", [])
            all_jobs.extend(jobs)
            print(f"✅ {role} | Page {page} → {len(jobs)} jobs")
            time.sleep(1.5)  # avoid rate limiting
        except Exception as e:
            print(f"❌ Failed: {role} page {page} → {e}")

# print(f"\n📊 Total raw jobs collected: {len(all_jobs)}")
#
# # Save raw to DB
# os.makedirs("data", exist_ok=True)
# df = pd.DataFrame(all_jobs)
# conn = sqlite3.connect("data/joblens.db")
# df.to_sql("jobs_raw", conn, if_exists="replace", index=False)
# conn.close()
# print("✅ Saved to joblens.db → table: jobs_raw")
# print(f"Columns available: {df.columns.tolist()}")


print(f"\n📊 Total raw jobs collected: {len(all_jobs)}")

# Save to database
os.makedirs("data", exist_ok=True)
df = pd.DataFrame(all_jobs)

# Fix: convert any list/dict columns to strings
for col in df.columns:
    df[col] = df[col].apply(lambda x: str(x) if isinstance(x, (list, dict)) else x)

conn = sqlite3.connect("data/joblens.db")
df.to_sql("jobs_raw", conn, if_exists="replace", index=False)
conn.close()
print("✅ Saved to joblens.db → table: jobs_raw")
print(f"Columns: {df.columns.tolist()}")




# import requests
#
# API_KEY = "693b588d2cmshe717d3ecbb4d05fp19162fjsnace3b1bef9ce"  # ← make sure this is your real key
#
# url = "https://jsearch.p.rapidapi.com/search"
# headers = {
#     "X-RapidAPI-Key": API_KEY,
#     "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
# }
# params = {
#     "query": "Data Analyst India",
#     "page": "1",
#     "num_pages": "1"
# }
#
# response = requests.get(url, headers=headers, params=params)
#
# print("Status Code:", response.status_code)
# print("Full Response:", response.json())