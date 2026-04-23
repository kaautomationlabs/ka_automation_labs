# KA Automation Labs – Karnataka Weather Bot 🌧️☀️

**Fully automated, non-commercial public utility** that delivers **hourly weather & climate updates** for **all 31 districts of Karnataka** on X (Twitter).

- **Schedule**: Hourly updates between **6 AM and 9 PM IST**
- **API Used**: Twitter POST `/2/tweets` (write-only)
- **Status**: Running live and reliably for over **1 month** with zero manual intervention

This bot is built as a free public service for Karnataka residents.  
**No scraping, no bulk data analysis, no automated following or messaging.**

## Features
- Covers all 31 districts of Karnataka
- Provides current temperature, weather condition, humidity, wind speed, and short forecast
- Clean, emoji-rich, readable tweet format
- Robust error handling and logging
- Lightweight and easy to maintain

## Project Structure

```bash
ka_automation_labs/
├── main.py                    # Main entry point
├── config.py                  # Configuration (districts, API settings, schedule)
├── modules/                   # Core logic
│   ├── __init__.py
│   ├── weather_fetcher.py     # Fetches weather data
│   ├── tweet_formatter.py     # Builds nice tweet text
│   ├── twitter_poster.py      # Handles posting to X
│   └── scheduler.py           # Scheduling logic
├── .github/
│   └── workflows/             # GitHub Actions (if any)
├── .gitignore
├── requirements.txt
├── .env.example
├── LICENSE
└── CLAUDE.md                  # Guidelines for Claude Code
How It Works (Flow)

Scheduler triggers the bot hourly (6 AM – 9 PM IST)
Weather Fetcher pulls latest data for all 31 districts
Tweet Formatter creates clean, engaging messages with emojis
Twitter Poster sends the update using write-only Twitter API
Logs are recorded for monitoring and debugging

Everything runs automatically — no manual steps required.
Deployment & Local Setup

Currently deployed on [Update: Your Hosting, e.g. VPS / Railway / AWS EC2 / etc.]
Scheduling handled via [Update: cron / GitHub Actions / systemd / etc.]

To run locally (for development):
Bashgit clone https://github.com/kaautomationlabs/ka_automation_labs.git
cd ka_automation_labs
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your Twitter and Weather API keys
python main.py
Important: Never commit real API keys. .env is already ignored by .gitignore.
Contributing
Contributions and suggestions are welcome!
You can help by:

Improving tweet formatting for better engagement
Adding severe weather alerts
Enhancing error handling
Suggesting new features for Karnataka residents
Improving documentation

Feel free to open Issues or Pull Requests.
License
This project is licensed under the MIT License.
See the LICENSE file for full details.
Maintainer
Built and maintained by kaautomationlabs
Follow project updates on X

⭐ If this bot helps you stay updated on Karnataka weather, please star the repository!
