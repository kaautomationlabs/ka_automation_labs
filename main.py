import tweepy
import os
import datetime
from modules import weather

def main():
    # Because of TZ env var, this is now naturally IST
    now = datetime.datetime.now()
    hour = now.hour
    
    print(f"🕒 Current IST Time: {now.strftime('%I:%M %p')}")

    # Operating window: 6 AM to 9 PM
    if 6 <= hour <= 21:
        client = tweepy.Client(
            consumer_key=os.getenv("API_KEY"),
            consumer_secret=os.getenv("API_SECRET"),
            access_token=os.getenv("ACCESS_TOKEN"),
            access_token_secret=os.getenv("ACCESS_SECRET")
        )

        weather_key = os.getenv("OPENWEATHER_KEY")
        tweet_text = weather.get_full_karnataka_weather(weather_key)
        
        if tweet_text:
            try:
                client.create_tweet(text=tweet_text)
                print("✅ Tweet sent successfully.")
            except Exception as e:
                print(f"❌ X API Error: {e}")
    else:
        print(f"💤 Sleeping. Bot only active 6AM-9PM IST.")

if __name__ == "__main__":
    main()