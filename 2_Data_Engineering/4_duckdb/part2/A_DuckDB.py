import duckdb
con = duckdb.connect()

# Show 10 rows
df_preview = con.execute("SELECT * FROM 'sakila_insights.csv' LIMIT 10").df()
df_preview.head(10)
