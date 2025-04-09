import asyncio
from telegram import Bot
from datetime import datetime
import sqlite3
import pandas as pd
from graphs import generate_all_graphs
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

async def main():
    conn = sqlite3.connect('data/mercadolivre.db')
    df = pd.read_sql_query("SELECT * FROM notebooks", conn)
    conn.close()

    lowest_prices = df[df['new_price'] > 0].sort_values('new_price').head(5)

    message = f"🛍️ *Top 5 Menores Preços de Notebooks ({datetime.now().date()})*\n\n"
    for idx, row in lowest_prices.iterrows():
        message += f"• {row['brand']} - R$ {row['new_price']:.2f}\n"

    bot = Bot(token=BOT_TOKEN)
    
    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")

    graph_paths = generate_all_graphs()
    for path in graph_paths:
        with open(path, 'rb') as photo:
            await bot.send_photo(chat_id=CHAT_ID, photo=photo)

if __name__ == '__main__':
    asyncio.run(main())