# src/transformations.py
import pandas as pd

def transform_data(raw_data: list) -> pd.DataFrame:
    """
    Cleans and transforms the raw JSON data using Pandas.
    """
    print("Transforming data...")
    df = pd.json_normalize(raw_data, sep='_')
    df = df[['id', 'name', 'username', 'email', 'address_city', 'company_name']]
    df = df.rename(columns={
        'address_city': 'city',
        'company_name': 'company'
    })
    print("Data transformed successfully.")
    return df