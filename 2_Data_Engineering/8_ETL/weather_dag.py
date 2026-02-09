from airflow.decorators import dag, task
from datetime import datetime, timedelta
import sys

# Make ETL package discoverable
sys.path.append("/home/kakarot/Desktop/VSCode/datamonk-internship_projects/2_Data_Engineering/8_ETL")

from db import create_tables
from extract import fetch_and_store_weather
from transform import fetch_day_average, fetch_global_average


@dag(
    dag_id="weather_etl_dag",
    start_date=datetime(2025, 5, 22),
    schedule="0 0 * * *",
    catchup=False,
    default_args={
        "retries": 2,
        "retry_delay": timedelta(minutes=3)
    },
    tags=["weather", "etl"]
)
def weather_etl():

    @task
    def create_tables_task():
        create_tables()

    @task
    def fetch_weather_task(ds=None):
        fetch_and_store_weather(city="Dispur", date=ds)

    @task
    def daily_weather_task():
        fetch_day_average()

    @task
    def global_weather_task():
        fetch_global_average()

    create_tables_task() \
        >> fetch_weather_task() \
        >> daily_weather_task() \
        >> global_weather_task()


weather_etl()
