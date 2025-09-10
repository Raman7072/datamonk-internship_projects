import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

from Monthly_Rentals import Monthly_Rentals
from Most_Popular_Films import Most_Popular_Films
from Category_Distribution import Category_Distribution
from Revenue_by_Store import Revenue_by_Store
from Rentals_by_Day import Rentals_by_Day
from Customers_Rentals import Customers_Rentals
from Average_Rental import Average_Rental
from Film_Rental import Film_Rental

DB_PATH = "sakila.db"
SCREENSHOT_DIR = "screenshots"

# Create screenshots directory if not exists
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH)

# 1
Monthly_Rentals()

# 2
Most_Popular_Films()

# 3
Category_Distribution()

# 4
Revenue_by_Store()

# 5
Rentals_by_Day()

# 6
Customers_Rentals()

# 7
Average_Rental()

# 8
Film_Rental()

conn.close()

print("✅ All charts generated and saved in 'screenshots/' folder.")