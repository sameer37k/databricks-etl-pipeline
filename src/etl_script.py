# src/etl_script.py
import requests
from pyspark.sql import SparkSession
from transformations import transform_data # <-- This import is key!

# --- 1. Extraction ---
def fetch_data_from_api(api_url: str) -> list:
    print(f"Fetching data from {api_url}...")
    response = requests.get(api_url)
    response.raise_for_status()
    print("Data fetched successfully.")
    return response.json()

# --- 3. Loading ---
def load_data_to_delta(spark: SparkSession, df, table_name: str):
    print(f"Loading data into Delta table: {table_name}...")
    spark_df = spark.createDataFrame(df)
    spark_df.write.format("delta").mode("overwrite").saveAsTable(table_name)
    print("Data loaded successfully.")

# --- Main execution block ---
if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com/users"
    TABLE_NAME = "default.users_prod"

    spark = SparkSession.builder.appName("API_to_Delta_ETL").getOrCreate()

    raw_json_data = fetch_data_from_api(API_URL)
    transformed_pandas_df = transform_data(raw_json_data)
    load_data_to_delta(spark, transformed_pandas_df, TABLE_NAME)

    print("ETL job completed successfully!")