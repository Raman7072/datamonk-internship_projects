import sqlite3
import pandas as pd
import time

def load_csv_to_sqlite(csv_path, table_name, conn):
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Loaded {csv_path} into table '{table_name}' with {len(df)} rows.")

def run_query(conn, query, description):
    start = time.time()
    result = pd.read_sql_query(query, conn)
    end = time.time()
    print(f"\n{description}")
    print(result.head(10))  # show first 10 rows
    print(f"Time taken: {end - start:.4f} seconds")
    return end - start

if __name__ == "__main__":
    conn = sqlite3.connect("people_case.db")

    # Load data

    print("=== Loading people small dataset ===")

    load_csv_to_sqlite("data/people_small.csv", "people_small", conn)
    print("=== Loading people large dataset ===")

    load_csv_to_sqlite("data/people_large.csv", "people_large", conn)
    print("=== Loading jobs large dataset ===")

    load_csv_to_sqlite("data/jobs_large.csv", "jobs_large", conn)

    timings = {}

    # Queries on people_small

    print("\n=== Queries on Small dataset ===")


    timings["small_count"] = run_query(conn, 
        "SELECT COUNT(*) FROM people_small;", 
        "Count rows (small)")

    timings["small_age50"] = run_query(conn, 
        "SELECT * FROM people_small WHERE `Date of birth` < '1973-01-01';", 
        "People older than 50 (small)")

    timings["small_avg_salary"] = run_query(conn, 
        "SELECT `Job Title`, AVG(j.salary) as avg_salary "
        "FROM people_small p JOIN jobs_large j ON p.`User Id` = j.person_id "
        "GROUP BY `Job Title`;", 
        "Average salary by Job Title (small JOIN)")

    # Same queries on people_large
    print("\n=== Queries on Large dataset ===")

    timings["large_count"] = run_query(conn, 
        "SELECT COUNT(*) FROM people_large;", 
        "Count rows (large)")

    timings["large_age50"] = run_query(conn, 
        "SELECT * FROM people_large WHERE `Date of birth` < '1973-01-01';", 
        "People older than 50 (large)")

    timings["large_avg_salary"] = run_query(conn, 
        "SELECT `Job Title`, AVG(j.salary) as avg_salary "
        "FROM people_large p JOIN jobs_large j ON p.`User Id` = j.person_id "
        "GROUP BY `Job Title`;", 
        "Average salary by Job Title (large JOIN)")

    # Top 5 highest paid people

    print("\n=== Top 5 highest paid People ===")

    timings["top5_paid"] = run_query(conn, 
        "SELECT p.`First Name`, p.`Last Name`, j.salary "
        "FROM people_large p JOIN jobs_large j "
        "ON p.`User Id` = j.person_id "
        "ORDER BY j.salary DESC LIMIT 5;", 
        "Top 5 highest-paid people")

    conn.close()

    print("\n=== Query Timings Summary ===")
    for k, v in timings.items():
        print(f"{k}: {v:.4f} sec")
