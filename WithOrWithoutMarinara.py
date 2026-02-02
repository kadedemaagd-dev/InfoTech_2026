import random
from datetime import datetime, timedelta

# -----------------------------
# Weather data settings
# Each weather type has:
# - A safe driving speed limit
# - How many minutes earlier the alarm should go off
# -----------------------------
weather_data = {
    "Sunny ☀️":        {"speed": 70, "alarm": 0},
    "Cloudy ☁️":      {"speed": 65, "alarm": 5},
    "Rainy 🌧️":       {"speed": 50, "alarm": 15},
    "Foggy 🌫️":       {"speed": 45, "alarm": 20},
    "Thunderstorm ⛈️": {"speed": 40, "alarm": 25},
    "Snowy ❄️":       {"speed": 30, "alarm": 30},
    "Hailstorm 🌨️":   {"speed": 25, "alarm": 35}
}

# -----------------------------
# Pick a random weather condition
# -----------------------------
weather = random.choice(list(weather_data.keys()))

# Get safety values for that weather
safe_speed = weather_data[weather]["speed"]
alarm_early = weather_data[weather]["alarm"]

# -----------------------------
# Alarm system logic
# -----------------------------

# Original alarm time (7:00 AM)
original_alarm = datetime.strptime("07:00", "%H:%M")

# Subtract minutes if bad weather
new_alarm = original_alarm - timedelta(minutes=alarm_early)

# Phone system output
print("📱 Smart Alarm System")
print(f"🌦️ Weather forecast: {weather}")

# If weather is bad, set alarm earlier
if alarm_early > 0:
    print("⚠️ Extra travel time needed due to weather.")
    print(f"⏰ Alarm set earlier by {alarm_early} minutes.")
    print(f"🔔 New alarm time: {new_alarm.strftime('%H:%M')}")
else:
    print("✅ No weather delays expected.")
    print("⏰ Alarm time unchanged:", original_alarm.strftime('%H:%M'))

print("\n-----------------------------\n")

# -----------------------------
# Car safety system logic
# -----------------------------
print("🚗 Car Safety System Online")
print(f"🌦️ Current conditions: {weather}")

# If speed is low, conditions are unsafe
if safe_speed < 60:
    print("⚠️ Unsafe driving conditions detected.")
    print(f"🔒 Speed limited to {safe_speed} mph.")
    print("🧠 Stability control and traction assist enabled.")
else:
    print("✅ Driving conditions are good.")
    print(f"🚀 Max speed set to {safe_speed} mph.")

print("🚗 Drive safe!")
