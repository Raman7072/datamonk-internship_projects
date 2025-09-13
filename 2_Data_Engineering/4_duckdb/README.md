# DuckDB Sakila Advanced Analytics Challenge

## 📌 Overview
This project explores advanced SQL analytics using the **Sakila DVD Rental Database** inside **DuckDB**.  
It demonstrates how to:
- Run complex multi-table joins and subqueries in DuckDB.
- Export enriched query results to **CSV**.
- Treat the exported CSV as a **standalone dataset** for further analysis.

The challenge simulates real-world data engineering workflows:
1. Start with a normalized relational schema (Sakila DB).
2. Create analytical views with joins and aggregations.
3. Export results to a flat file for downstream analysis.
4. Query the flat file directly in DuckDB (without re-importing).

---

## ⚙️ Setup

### 1. Download Sakila SQLite DB
```bash
wget https://github.com/ivanceras/sakila/raw/master/sqlite-sakila-db/sakila.db -O sakila.db
```

### 2. Start DuckDB Shell
```bash
duckdb
```

### 3. Install & Load SQLite Extension
```sql
INSTALL sqlite_scanner;
LOAD sqlite_scanner;
```

### 4. Attach Sakila DB
```sql
ATTACH 'sakila.db' AS sakila (TYPE sqlite);
USE sakila;
SHOW TABLES;
```

You’ll see tables like:
`actor, customer, film, rental, payment, store, category, inventory`, etc.

---

## 🧩 Part 1 – Complex Queries on Sakila

### 1. Rentals with Film & Customer Details
Joins across **film, category, customer, store, rental, payment**  
Includes a correlated subquery computing **total spend per customer per film**.

**Output fields:**
- Film title  
- Category name  
- Customer full name  
- Store city & country  
- Rental date  
- Customer’s total spend for that film  

📄 See: [`sql/part1_join_and_export.sql`](sql/part1_join_and_export.sql)

---

### 2. Top 3 Revenue Customers per Country
Two implementations provided:
- **Window function (ROW_NUMBER)**  
- **Correlated subquery**  

📄 See: [`sql/top3_customers_per_country.sql`](sql/top3_customers_per_country.sql)

---

### 3. Export Results
```sql
COPY (
  SELECT ...
) TO 'sakila_insights.csv' (HEADER, DELIMITER ',');
```

Generated file: **[`sakila_insights.csv`](sakila_insights.csv)**

---

## 📊 Part 2 – Querying the Exported CSV

DuckDB allows querying CSVs directly:

```python
import duckdb
con = duckdb.connect()
con.execute("SELECT * FROM 'sakila_insights.csv' LIMIT 10").df()
```

### Example Queries
1. **Top 5 films by revenue**
2. **Unique customers per category**
3. **Action films above category average revenue**
4. **Histogram buckets of total revenue (<$10, $10–$50, >$50)**

📄 See: [`notebooks/sakila_duckdb_analysis.ipynb`](notebooks/sakila_duckdb_analysis.ipynb)

---

## 📝 Write-up

Exporting to CSV **flattened the normalized schema** into a single denormalized dataset.  
This simplified downstream queries (no joins required), but required extra care to avoid **double-counting** revenues if multiple rentals existed.  

**Benefits:**  
- CSVs are portable, lightweight, and queryable directly in DuckDB.  
- No schema migration needed for quick analysis.  

**Limitations:**  
- CSV lacks strict typing and schema enforcement.  
- Not as efficient as Parquet for large analytical workloads.  
- Once flattened, relational detail is lost.  

---

## 📂 Project Structure
```
data_eng/
├── sql/
│   ├── part1_join_and_export.sql
│   ├── top3_customers_per_country.sql
├── sakila_insights.csv
├── notebooks/
│   └── sakila_duckdb_analysis.ipynb
└── README.md
```

---

## 🚀 How to Run
1. Clone this repository.
2. Follow **Setup** steps above to attach Sakila DB.
3. Run SQL scripts inside DuckDB shell.
4. Generate `sakila_insights.csv` using the `COPY` command.
5. Open the Jupyter notebook and run CSV-only queries.

---
