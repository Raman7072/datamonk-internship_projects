from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("crud.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS items (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL
                    )""")
    conn.commit()
    conn.close()

@app.route("/")
def index():
    conn = sqlite3.connect("crud.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    conn.close()
    return render_template("index.html", items=items)

@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name")
    if name:
        conn = sqlite3.connect("crud.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO items (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()
    return redirect(url_for("index"))

@app.route("/update/<int:item_id>", methods=["POST"])
def update(item_id):
    new_name = request.form.get("name")
    if new_name:
        conn = sqlite3.connect("crud.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE items SET name=? WHERE id=?", (new_name, item_id))
        conn.commit()
        conn.close()
    return redirect(url_for("index"))

@app.route("/delete/<int:item_id>", methods=["POST"])
def delete(item_id):
    conn = sqlite3.connect("crud.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id=?", (item_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", debug=True)
