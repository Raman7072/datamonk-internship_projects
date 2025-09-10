import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

SCREENSHOT_DIR = "screenshots"
DB_PATH = "sakila.db"

conn = sqlite3.connect(DB_PATH)


# ==============================
# 4. Revenue by Store (Bar Chart)
# ==============================
def Revenue_by_Store():
    
    query = """
    SELECT s.store_id, SUM(p.amount) AS revenue
        FROM payment p
        JOIN rental r ON p.rental_id = r.rental_id
        JOIN staff st ON r.staff_id = st.staff_id
        JOIN store s ON st.store_id = s.store_id
        GROUP BY s.store_id;
    """
    df = pd.read_sql_query(query, conn)

    plt.figure(figsize=(6,5))
    plt.bar(df['store_id'].astype(str), df['revenue'], color='green')
    plt.title("Revenue by Store")
    plt.xlabel("Store ID")
    plt.ylabel("Revenue ($)")
    plt.tight_layout()
    plt.savefig(f"{SCREENSHOT_DIR}/dv4.png")
    plt.close()

    conn.close()