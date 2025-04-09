import pandas as pd
import sqlite3
from datetime import datetime

# Load data from JSON file
df = pd.read_json('data/data.jsonl', lines=True)

# Set pandas to show all columns
pd.options.display.max_columns = None

# Add column _source with a fixed value
df["_source"] = "https://lista.mercadolivre.com.br/notebook"

# Add column _data_coleta with the current date and time
df['_data_coleta'] = datetime.now()
print(df)

# Treat null data
df['old_price'] = df['old_price'].fillna('0')
df['new_price'] = df['new_price'].fillna('0')
df['reviews_rating_number'] = df['reviews_rating_number'].fillna('0')
df['reviews_amount'] = df['reviews_amount'].fillna('(0)')

# Guarantee that the columns are as strings before use .str
# Remove "." from old_price, new_price and reviews_amount
# Remove "(" and ")" from reviews_amount
df['old_price'] = df['old_price'].astype(str).str.replace('.', '', regex=False)
df['new_price'] = df['new_price'].astype(str).str.replace('.', '', regex=False)
df['reviews_amount'] = df['reviews_amount'].astype(str).str.replace('[\(\)]', '', regex=True)

# Convert to number treated data again
df['old_price'] = df['old_price'].astype(float)
df['new_price'] = df['new_price'].astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].astype(float)
df['reviews_amount'] = df['reviews_amount'].astype(int)

# Maintain only products with price between 1000 and 4000
df = df[
    (df['old_price'] >= 1000) & (df['old_price'] <= 10000) &
    (df['new_price'] >= 1000) & (df['new_price'] <= 10000)
]

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('data/mercadolivre.db')

# Save data to a new table in the SQLite database
df.to_sql('notebooks', conn, if_exists='replace', index=False)

# Close the database connection
conn.close()

print(df.head())
print("Data saved to SQLite database successfully.")