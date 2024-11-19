import pandas as pd
import numpy as np

file_path =/Users/akashdeep/Desktop/listing.csv/
df=pd.read_csv(file_path)
df['host_since'] = pd.to_datetime(df['host_since'], errors='coerce')
numerical=df.select_dtypes(include=[np.number]).columns
df[numerical]=df[numerical].fillna(df[numerical].median())
categorical=df.select_dtypes(include=[object]).columns
df[categorical]=df[categorical].fillna(df[categorical].mode().iloc[0])
df.head()
