import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os

def load_data():
    conn = sqlite3.connect('data/mercadolivre.db')
    df = pd.read_sql_query("SELECT * FROM notebooks", conn)
    conn.close()
    return df

def save_bar_chart(data, title, xlabel, ylabel, filename):
    os.makedirs('img', exist_ok=True)
    
    plt.figure(figsize=(10, 6))
    data.plot(kind='bar')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def generate_all_graphs():
    df = load_data()

    top_brands = df['brand'].value_counts()
    save_bar_chart(top_brands, 'Marcas Mais Encontradas', 'Marca', 'Quantidade', 'img/top_brands.png')

    df_prices = df[df['new_price'] > 0]
    avg_price = df_prices.groupby('brand')['new_price'].mean().sort_values(ascending=False)
    save_bar_chart(avg_price, 'Preço Médio por Marca', 'Marca', 'Preço Médio (R$)', 'img/avg_price.png')

    df_reviews = df[df['reviews_rating_number'] > 0]
    avg_rating = df_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
    save_bar_chart(avg_rating, 'Satisfação Média por Marca', 'Marca', 'Nota Média', 'img/avg_rating.png')

    return ['img/top_brands.png', 'img/avg_price.png', 'img/avg_rating.png']
