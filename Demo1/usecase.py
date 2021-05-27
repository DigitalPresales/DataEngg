
import pandas as pd
import numpy as np
import os


data = pd.read_csv('/home/data/airflow/dags/Test.csv',  encoding='utf-8')

Brand_Name = data['Brand Name'].str.upper()
print(Brand_Name.value_counts().head(10))

