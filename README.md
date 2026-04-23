# KA Automation Labs – Karnataka Weather Bot 🌧️☀️

**Fully automated, non-commercial public utility** that delivers **hourly weather & climate updates** for **all 31 districts of Karnataka** on X (Twitter).

- **Schedule**: Hourly updates between **6 AM and 9 PM IST**
- **API**: Twitter POST `/2/tweets` (write-only)
- **Status**: Running live and reliably for over **1 month** with zero manual intervention

This bot is built as a free public service for Karnataka residents.  
**No scraping, no bulk data analysis, no automated following or messaging.**

## Features
- Covers all 31 districts of Karnataka
- Provides current temperature, weather condition, humidity, wind, and short forecast
- Clean, emoji-rich, readable tweet format
- Robust error handling and logging
- Lightweight and easy to maintain

## Project Structure (File Directory)

```bash
ka_automation_labs/
├── main.py                    # Main entry point
├── config.py                  # Configuration (districts, API settings, schedule)
├── modules/                   # Core logic
│   ├── __init__.py
│   ├── weather_fetcher.py     # Fetches weather data
│   ├── tweet_formatter.py     # Builds nice tweet text
│   ├── twitter_poster.py      # Handles posting to X
│   └── scheduler.py           # (or uses GitHub Actions / cron)
├── .github/
│   └── workflows/             # CI/CD workflows (if any)
├── .gitignore
├── requirements.txt           # Python dependencies
├── .env.example               # Environment variables template
├── LICENSE
└── CLAUDE.md                  # (optional) Guidelines for Claude Code
