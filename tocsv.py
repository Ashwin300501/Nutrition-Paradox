import sqlite3
import pandas as pd

conn = sqlite3.connect('nutrition_paradox.db')

df_obesity=pd.read_sql_query("""SELECT * FROM obesity""",conn)
df_malnutrition=pd.read_sql_query("""SELECT * FROM malnutrition""",conn)

df_obesity.to_csv("obesity_data.csv",index=False)
df_malnutrition.to_csv("malnutrition_data.csv",index=False)

conn.close()