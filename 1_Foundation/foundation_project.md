# Google Drive Clone – Foundation Project

## Features
- Upload files (stored in S3)
- View all files (fetched from SQLite)
- Delete files (removes from S3 and DB)

## Technologies
- Flask
- AWS S3
- SQLite
- Docker
- EC2 Ubuntu

## Setup
1. Clone repo
2. Set environment variables in `docker-compose.yml`
3. Run `docker-compose up --build -d`
4. Access app at `http://<EC2-IP>:5000`

## Screenshots
- File upload
- File listing
- S3 view
- EC2 container
