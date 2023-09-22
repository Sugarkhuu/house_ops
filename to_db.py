import pandas as pd
import psycopg2
from sqlalchemy import create_engine


df = pd.read_csv("results/unegui.csv")
engine = create_engine('postgresql://postgres:postgres@localhost:5432/housing')
table_name = 'housenew'

# Using the direct psycopg2 connection
# df.to_sql(table_name, con=db_connection, if_exists='append', index=False)
df.to_sql(table_name, con=engine, if_exists='append', index=False)

