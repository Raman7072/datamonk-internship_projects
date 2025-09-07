import sqlite3
from typing import Iterable, Dict, Any

EXPECTED_FIELDS = ["date","time","temperature","condition","humidity",
                   "location_name","region","country","latitude","longitude","local_time"]

def validate_record(rec: Dict[str, Any]) -> Dict[str, Any]:
    # Ensure only expected keys exist and missing keys are set to None
    out = {k: rec.get(k) for k in EXPECTED_FIELDS}
    return out

def insert_weather_data(records: Iterable[dict], db_path: str = "data.db") -> int:
    """Insert hourly weather records, ignoring duplicates. Returns inserted count (not including ignored)."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    rows = [tuple(validate_record(r)[k] for k in EXPECTED_FIELDS) for r in records]

    cur.executemany(f"""
        INSERT OR IGNORE INTO weather ({",".join(EXPECTED_FIELDS)})
        VALUES ({",".join(["?"]*len(EXPECTED_FIELDS))});
    """, rows)

    inserted = cur.rowcount if cur.rowcount is not None else 0
    conn.commit()
    conn.close()
    return inserted
