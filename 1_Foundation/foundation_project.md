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
- File upload ![](https://github.com/Raman7072/datamonk-internship_projects/blob/main/1_Foundation/google-drive-clone/GCC2.png)
- File listing ![](https://github.com/Raman7072/datamonk-internship_projects/blob/main/1_Foundation/google-drive-clone/GCC3.png)
- S3 view ![](https://github.com/Raman7072/datamonk-internship_projects/blob/main/1_Foundation/google-drive-clone/GCC1.png)
- EC2 container 
