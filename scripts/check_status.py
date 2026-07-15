import urllib.request
import json
import os
import datetime

API_URL = "https://api.mcsrvstat.us/2/tumo07.io.vn"
LOG_FILE = "status_log.json"

def fetch_status():
    try:
        req = urllib.request.Request(API_URL, headers={'User-Agent': 'StatusChecker/1.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            return {
                "online": data.get("online", False),
                "players": data.get("players", {}).get("online", 0)
            }
    except Exception as e:
        print(f"Error fetching status: {e}")
        return {"online": False, "players": 0}

def main():
    status = fetch_status()
    now = datetime.datetime.utcnow()
    
    # Format: YYYY-MM-DD HH:MM UTC
    timestamp = now.strftime("%Y-%m-%d %H:%M UTC")
    
    entry = {
        "timestamp": timestamp,
        "online": status["online"],
        "players": status["players"]
    }
    
    logs = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
        except Exception:
            pass
            
    # Add new entry at the beginning
    logs.insert(0, entry)
    
    # Keep only the last 200 logs to prevent file bloating
    logs = logs[:200]
    
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)
        
    print(f"Logged status: {entry}")

if __name__ == "__main__":
    main()
