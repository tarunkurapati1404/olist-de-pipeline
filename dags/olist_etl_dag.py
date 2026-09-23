# 1. Import the necessary tools from Airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# 2. Define default arguments for our pipeline
# These settings apply to every task in this DAG
default_args = {
    'owner': 'tarun',                # Who owns this pipeline
    'depends_on_past': False,        # Don't wait for yesterday's run to finish
    'email_on_failure': False,       # Set to True in real jobs to get alerts
    'retries': 1,                    # If a task fails, retry it 1 time
    'retry_delay': timedelta(minutes=5), # Wait 5 minutes before retrying
}

# 3. Define the DAG itself
# This is the main container for our pipeline
with DAG(
    dag_id='olist_etl_pipeline',     # The unique name of our DAG
    default_args=default_args,       # Apply the settings we defined above
    description='ETL pipeline for Olist E-commerce data',
    schedule_interval='@daily',      # Run this pipeline every day at midnight
    start_date=datetime(2026, 9, 23),# When the pipeline starts (today!)
    catchup=False,                   # Don't run past dates (very important!)
    tags=['olist', 'ecommerce', 'de_project'], # Tags for easy searching in UI
) as dag:

    # --- TASK 1: Extract Data (Simulated) ---
    # In a real job, this would use an S3 Operator to check if new files arrived.
    # For now, we use a BashOperator to just print a message.
    extract_data = BashOperator(
        task_id='extract_data_from_s3',
        bash_command='echo "Checking S3 for new raw Olist data..."'
    )

    # --- TASK 2: Transform Data (Run our Python Script) ---
    # This task runs the exact Python validation script we wrote on Day 2!
    # Note: In a real setup, this path would be inside the Airflow server.
    transform_data = BashOperator(
        task_id='validate_and_transform_data',
        bash_command='python D:/Data_Engineering/de-projects/olist-de-pipeline/validate_data.py'
    )

    # --- TASK 3: Load Data (Simulated Databricks Job) ---
    # In a real company, we would use the 'DatabricksSubmitRunOperator' here.
    # It would tell Databricks: "Hey, run the PySpark notebook we wrote on Day 3!"
    load_data = BashOperator(
        task_id='run_databricks_pyspark_job',
        bash_command='echo "Triggering Databricks PySpark job to clean data and save to S3..."'
    )

    # --- DEFINE THE ORDER OF TASKS (The Arrows!) ---
    # This tells Airflow: Extract -> Transform -> Load
    extract_data >> transform_data >> load_data