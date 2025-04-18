# Web Scraping, Analysis and Notification System

A complete pipeline for scraping notebook data from Mercado Livre, analyzing it, and sending automated reports via Telegram.

## 📁 Project Structure
```sh
webscraping-scrapy-ml/
├── src/
│   ├── bot/                       # Telegram bot components
│   │   ├── graph.py               # Data visualization generation
│   │   ├── main_bot.py            # Main bot logic and messaging
│   │   └── schedule.py            # Scheduling for automated reports
│   │
│   ├── dashboard/                 # Streamlit data dashboard
│   │   └── app.py                 # Dashboard main application
│   │
│   ├── mercadolivre/             # Scrapy spider
│   │   ├── mercadolivre/         # Spider implementation
│   │   └── scrapy.cfg            # Scrapy configuration
│   │
│   └── transform_load/           # ETL processes
│       └── main.py               # Data transformation and SQLite loading
│
├── data/                         # Data storage
│   ├── data.jsonl                # Raw scraped data
│   └── mercadolivre.db           # Processed SQLite database
│
└── README.md                     # Docs
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Poetry (recommended) or pip
- Telegram bot token (get from @BotFather)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/webscraping-scrapy-ml.git
   cd webscraping-scrapy-ml
   ```

2. Install dependencies:
   ```bash
   poetry install  # If using Poetry
   # OR
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token
   TELEGRAM_CHAT_ID=your_chat_id
   ```

## 🛠️ Components

### 1. Scrapy Spider (mercadolivre/)
- Scrapes notebook data from Mercado Livre
- Run with:
  ```bash
  cd mercadolivre
  scrapy crawl notebooks -O ../data/data.jsonl
  ```

### 2. ETL Pipeline (transform_load/)
- Transforms raw JSONL data and loads to SQLite
- Run with:
  ```bash
  python transform_load/main.py
  ```

### 3. Telegram Bot (bot/)
- Sends automated reports with price analysis
- Visualizations generated in `graph.py`
- Scheduled via `schedule.py`
- Run main bot:
  ```bash
  python bot/main_bot.py
  ```

### 4. Streamlit Dashboard (dashboard/)
- Interactive data visualization
- Run with:
  ```bash
  streamlit run dashboard/app.py
  ```

## 🔄 Workflow
1. **Scrape**: Run the Scrapy spider to collect data
2. **Transform**: Process and clean the raw data
3. **Load**: Store processed data in SQLite
4. **Analyze**: Generate visualizations and insights
5. **Report**: Send automated Telegram reports
6. **Visualize**: Explore data in Streamlit dashboard

## 📅 Scheduling
Set up cron jobs or Windows Task Scheduler to run:
1. Scraper daily
2. Bot reports at preferred intervals