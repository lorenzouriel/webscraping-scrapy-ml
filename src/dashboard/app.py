# import
import streamlit as st
import pandas as pd
import sqlite3

# Connect to SQLite database 
conn = sqlite3.connect('data/mercadolivre.db')

# Load table with pandas    
df = pd.read_sql_query("SELECT * FROM notebooks", conn)

# Close connection 
conn.close()

# App Title
st.title('📊 Pesquisa de Mercado - Notebooks no Mercado Livre')

# Improve Layout with KPIs Columns
st.subheader('💡 KPIs principais')
col1, col2, col3 = st.columns(3)

# KPI 1: Total number of items
# Calculate total number of items
total_itens = df.shape[0]
col1.metric(label="🖥️ Total de Notebooks", value=total_itens)

# KPI 2: Total number of unique brands
# Calculate total number of unique brands
unique_brands = df['brand'].nunique()
col2.metric(label="🏷️ Marcas Únicas", value=unique_brands)

# KPI 3: Medium price in reais
# Calculate average new price
average_new_price = df['new_price'].mean()
col3.metric(label="💰 Preço Médio (R$)", value=f"{average_new_price:.2f}")

# Frequently brands
st.subheader('🏆 Marcas mais encontradas até a 10ª página')
col1, col2 = st.columns([4, 2])
top_brands = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_brands)
col2.write(top_brands)

# Medium price by brand
st.subheader('💵 Preço médio por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_prices = df[df['new_price'] > 0]
average_price_by_brand = df_non_zero_prices.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)

# Medium rating by brand
st.subheader('⭐ Satisfação média por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)