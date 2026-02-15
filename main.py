import tweepy
import os
import datetime
from modules import weather

def main():
    # IST Time Check (GitHub uses UTC)
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    ist_hour = (now_utc.hour + 5) + (1 if now_utc.minute >= 30 else 0)
    ist_hour %= 24

    if 6 <= ist_hour <= 21:
        # Pull keys from GitHub Secrets (NOT .env)
        client = tweepy.Client(
            consumer_key=os.getenv("API_KEY"),
            consumer_secret=os.getenv("API_SECRET"),
            access_token=os.getenv("ACCESS_TOKEN"),
            access_token_secret=os.getenv("ACCESS_SECRET")
        )

        weather_key = os.getenv("OPENWEATHER_KEY")
        tweet_text = weather.get_full_karnataka_weather(weather_key)
        
        try:
            client.create_tweet(text=tweet_text)
            print(f"✅ Posted weather for {ist_hour}:00 IST")
        except Exception as e:
            print(f"❌ Error: {e}")
    else:
        print(f"💤 Sleeping. Current IST hour: {ist_hour}")

if __name__ == "__main__":
    main()