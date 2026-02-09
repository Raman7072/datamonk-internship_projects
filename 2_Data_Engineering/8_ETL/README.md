# Rebuilding Our Weather ETL Project Using Apache Airflow 🌦️

This guide walks through converting a **Python-based Weather ETL pipeline** into a **fully automated Apache Airflow workflow**.

Previously, our ETL pipeline:
- Extracted hourly weather data for **500+ Indian cities**
- Transformed it into **daily** and **global summaries**
- Loaded results into **SQLite** and visualized them using **Matplotlib**

Now, we orchestrate the same logic using **Apache Airflow**, making it:
- Automated
- Scalable
- Production-ready

---

## Why Use Apache Airflow?

Airflow turns one-off scripts into **reliable workflows** by providing:
- Scheduling
- Task dependencies
- Retry mechanisms
- Logging & monitoring
- Visual DAG representation

Think of Airflow as the **control plane** for your data pipelines.

---

## Step 1: Install Apache Airflow

Follow the official documentation:  
🔗 *Installing from PyPI – Apache Airflow Docs*

### Key Setup Steps

1. Create a virtual environment:
```bash
python -m venv airflow_venv
source airflow_venv/bin/activate
```

2. Install Airflow:
```bash
pip install apache-airflow
```

3. Set Airflow home:
```bash
export AIRFLOW_HOME=~/airflow
```

4. Initialize metadata DB:
```bash
airflow db migrate
```

5. Start Airflow:
```bash
airflow standalone
```

📍 Access the UI at: [http://localhost:8080](http://localhost:8080)
