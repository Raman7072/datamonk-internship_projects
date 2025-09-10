import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

SCREENSHOT_DIR = "screenshots"
DB_PATH = "sakila.db"

conn = sqlite3.connect(DB_PATH)


# ==============================
# 5. Rentals by Day of the Week (Bar Chart)
# ==============================
def Rentals_by_Day():
   
    query = """
    SELECT strftime('%w', rental_date) AS weekday, COUNT(*) AS rentals
        FROM rental
        GROUP BY weekday
        ORDER BY weekday;
    """
    df = pd.read_sql_query(query, conn)

    weekday_map = {
        "0": "Sunday", "1": "Monday", "2": "Tuesday",
        "3": "Wednesday", "4": "Thursday", "5": "Friday", "6": "Saturday"
    }
    df['weekday'] = df['weekday'].map(weekday_map)

    plt.figure(figsize=(8,5))
    plt.bar(df['weekday'], df['rentals'], color='purple')
    plt.title("Rentals by Day of the Week")
    plt.xlabel("Day")
    plt.ylabel("Number of Rentals")
    plt.tight_layout()
    plt.savefig(f"{SCREENSHOT_DIR}/dv5.png")
    plt.close()

    conn.close()