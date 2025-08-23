import sqlite3

con = sqlite3.connect("drive.db")
con.execute("""
CREATE TABLE IF NOT EXISTS files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    size INTEGER,
    content_type TEXT,
    s3_path TEXT,
    uploaded_at TEXT
)
""")
con.commit()
con.close()
print("✅ Database initialized")
