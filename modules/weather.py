import requests
import datetime

DISTRICTS = [
    "Bagalkote", "Ballari", "Belagavi", "Bengaluru Rural", "Bengaluru Urban", 
    "Bidar", "Chamarajanagara", "Chikkaballapura", "Chikkamagaluru", 
    "Chitradurga", "Dakshina Kannada", "Davanagere", "Dharwad", "Gadag", 
    "Hassan", "Haveri", "Kalaburagi", "Kodagu", "Kolar", "Koppal", "Mandya", 
    "Mysuru", "Raichur", "Ramanagara", "Shivamogga", "Tumakuru", "Udupi", 
    "Uttara Kannada", "Vijayanagara", "Vijayapura", "Yadgir"
]

def get_full_karnataka_weather(api_key):
    now = datetime.datetime.now()
    # Rotate districts based on the hour so all 31 get covered daily
    start_index = (now.hour % 10) * 3
    selected = DISTRICTS[start_index : start_index + 3]
    
    report = f"📍 KA District Weather | {now.strftime('%I:%M %p')}\n━━━━━━━━━━━━━━━━━━\n"
    
    for city in selected:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={api_key}&units=metric"
        try:
            res = requests.get(url).json()
            temp = res["main"]["temp"]
            desc = res["weather"][0]["description"].capitalize()
            report += f"🏙️ {city}: {temp}°C, {desc}\n"
        except:
            continue

    report += "\n#KarnatakaWeather #LiveUpdates"
    return report