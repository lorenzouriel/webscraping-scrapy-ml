import schedule
import time
import subprocess

def run_bot():
    subprocess.run(["python", "bot/bot.py"])

schedule.every().day.at("08:00").do(run_bot)

while True:
    schedule.run_pending()
    time.sleep(60)