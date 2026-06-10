# import pandas as pd
# import sqlite3
# import json
#
# import os
#
#
# conn = sqlite3.connect(r"C:\Users\sumit\PycharmProjects\PythonProject1\data\joblens.db")
# # DB_PATH = r"C:\Users\sumit\PycharmProjects\PythonProject1\data\joblens.db"
# #
# #
# # conn = sqlite3.connect(DB_PATH)
#
# cur=conn.cursor()
# cur.execute('SELECT name FROM sqlite_master')
# print(cur.fetchall())
# cur.close()
# # Show all tables
# tables = pd.read_sql(
#     "SELECT name FROM sqlite_master WHERE type='table';",
#     conn
# )
#
# print("Tables in database:")
# print(tables)
#
# # Check if jobs_raw exists
# if "jobs_raw" not in tables["name"].values:
#     print("❌ Table 'jobs_raw' does not exist!")
#     conn.close()
#     exit()
#
# # Existing code
# df = pd.read_sql("SELECT * FROM jobs_raw", conn)
# # df = pd.read_sql("SELECT * FROM jobs_raw", conn)
# print(f"Raw rows: {len(df)}")
#
# # Keep useful columns
# keep_cols = [
#     "job_id", "job_title", "employer_name", "job_city", "job_state",
#     "job_country", "job_employment_type", "job_posted_at_datetime_utc",
#     "job_min_salary", "job_max_salary", "job_salary_period",
#     "job_description", "job_apply_link", "job_is_remote",
#     "job_latitude", "job_longitude", "job_salary_string"
# ]
# available = [c for c in keep_cols if c in df.columns]
# df = df[available]
#
# # Clean steps
# df = df.drop_duplicates(subset=["job_id"])
# df["job_posted_at_datetime_utc"] = pd.to_datetime(
#     df["job_posted_at_datetime_utc"], errors="coerce"
# )
# df["job_title"] = df["job_title"].str.strip()
# df["employer_name"] = df["employer_name"].str.strip()
#
# # Filter India only
# if "job_country" in df.columns:
#     df = df[df["job_country"].str.upper() == "IN"]
#
# # Categorize role
# def categorize(title):
#     title = str(title).lower()
#     if "data analyst" in title:                              return "Data Analyst"
#     if "data scientist" in title:                            return "Data Scientist"
#     if "ml engineer" in title or "machine learning" in title: return "ML Engineer"
#     if "data engineer" in title:                             return "Data Engineer"
#     if "business analyst" in title:                          return "Business Analyst"
#     if "ai engineer" in title or "artificial intelligence" in title: return "AI Engineer"
#     return "Other"
#
# df["role_category"] = df["job_title"].apply(categorize)
#
# # Save
# df.to_sql("jobs_clean", conn, if_exists="replace", index=False)
# conn.close()
#
# print(f"✅ Clean rows saved: {len(df)}")
# print(f"\nRole breakdown:\n{df['role_category'].value_counts()}")
# print(f"\nTop Cities:\n{df['job_city'].value_counts().head(10)}")
# print(f"\nRemote jobs: {df['job_is_remote'].sum()}")






import pandas as pd
import sqlite3
import os

BASE_DIR = r"C:\Users\sumit\PycharmProjects\PythonProject1"
DB_PATH = os.path.join(BASE_DIR,"scraper", "data", "joblens.db")

conn = sqlite3.connect(DB_PATH)

# Show all tables
tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

print("Tables in database:")
print(tables)

# Check if jobs_raw exists
if "jobs_raw" not in tables["name"].values:
    print("❌ Table 'jobs_raw' does not exist!")
    conn.close()
    exit()

# Load raw data
df = pd.read_sql("SELECT * FROM jobs_raw", conn)
print(f"Raw rows: {len(df)}")

# Keep useful columns
keep_cols = [
    "job_id", "job_title", "employer_name", "job_city", "job_state",
    "job_country", "job_employment_type", "job_posted_at_datetime_utc",
    "job_min_salary", "job_max_salary", "job_salary_period",
    "job_description", "job_apply_link", "job_is_remote",
    "job_latitude", "job_longitude", "job_salary_string"
]
available = [c for c in keep_cols if c in df.columns]
df = df[available]
print(f"Columns kept: {available}")

# Clean steps
df = df.drop_duplicates(subset=["job_id"])
df["job_posted_at_datetime_utc"] = pd.to_datetime(
    df["job_posted_at_datetime_utc"], errors="coerce"
)
df["job_title"] = df["job_title"].str.strip()
df["employer_name"] = df["employer_name"].str.strip()

# Filter India only
if "job_country" in df.columns:
    before = len(df)
    df = df[df["job_country"].str.upper() == "IN"]
    print(f"India filter: {before} → {len(df)} rows")

# Categorize role
def categorize(title):
    title = str(title).lower()
    if "data analyst" in title:                               return "Data Analyst"
    if "data scientist" in title:                             return "Data Scientist"
    if "ml engineer" in title or "machine learning" in title: return "ML Engineer"
    if "data engineer" in title:                              return "Data Engineer"
    if "business analyst" in title:                           return "Business Analyst"
    if "ai engineer" in title or "artificial intelligence" in title: return "AI Engineer"
    return "Other"

df["role_category"] = df["job_title"].apply(categorize)

# Save cleaned data
df.to_sql("jobs_clean", conn, if_exists="replace", index=False)
conn.close()

print(f"\n✅ Clean rows saved: {len(df)}")
print(f"\nRole breakdown:\n{df['role_category'].value_counts()}")
print(f"\nTop Cities:\n{df['job_city'].value_counts().head(10)}")
print(f"\nRemote jobs: {df['job_is_remote'].sum()}")