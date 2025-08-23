from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import sqlite3, boto3, os
from datetime import datetime, timezone
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

S3_BUCKET = os.getenv("S3_BUCKET")
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")

s3 = boto3.client("s3")

def db():
    conn = sqlite3.connect("drive.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/files")
def list_files():
    rows = db().execute("SELECT * FROM files ORDER BY uploaded_at DESC").fetchall()
    return jsonify([dict(r) for r in rows])

@app.route("/api/upload", methods=["POST"])
def upload():
    f = request.files["file"]
    filename = secure_filename(f.filename)
    key = f"KAKAROT/{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}-{filename}"
    s3.upload_fileobj(f, S3_BUCKET, key, ExtraArgs={"ACL": "private", "ContentType": f.mimetype})

    size = request.content_length or 0
    con = db()
    cur = con.execute("INSERT INTO files(name, size, content_type, s3_path, uploaded_at) VALUES (?,?,?,?,?)",
                      (filename, size, f.mimetype, key, datetime.utcnow().isoformat()))
    con.commit()
    return {"id": cur.lastrowid}, 201

@app.route("/api/files/<int:file_id>/delete", methods=["DELETE"])
def delete_file(file_id):
    con = db()
    row = con.execute("SELECT s3_path FROM files WHERE id=?", (file_id,)).fetchone()
    if not row: return {"error": "Not found"}, 404
    s3.delete_object(Bucket=S3_BUCKET, Key=row["s3_path"])
    con.execute("DELETE FROM files WHERE id=?", (file_id,))
    con.commit()
    return {"ok": True}

@app.route("/api/files/<int:file_id>/download")
def download(file_id):
    row = db().execute("SELECT name, s3_path FROM files WHERE id=?", (file_id,)).fetchone()
    if not row: return {"error": "Not found"}, 404
    url = s3.generate_presigned_url("get_object", Params={"Bucket": S3_BUCKET, "Key": row["s3_path"],
                                                         "ResponseContentDisposition": f'attachment; filename="{row["name"]}"'}, ExpiresIn=300)
    return {"url": url}

@app.route("/api/files/<int:file_id>/preview")
def preview(file_id):
    row = db().execute("SELECT s3_path FROM files WHERE id=?", (file_id,)).fetchone()
    if not row: return {"error": "Not found"}, 404
    url = s3.generate_presigned_url("get_object", Params={"Bucket": S3_BUCKET, "Key": row["s3_path"]}, ExpiresIn=300)
    return {"url": url}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
