import random

# Weather data with safe speed limits (mph)
weather_conditions = {
    "Sunny ☀️": 70,
    "Cloudy ☁️": 65,
    "Rainy 🌧️": 50,
    "Foggy 🌫️": 45,
    "Thunderstorm ⛈️": 40,
    "Snowy ❄️": 30,
    "Hailstorm 🌨️": 25
}

# Pick random weather
current_weather = random.choice(list(weather_conditions.keys()))
safe_speed = weather_conditions[current_weather]

# Car "speaks"
print("🚗 Car System Online")
print(f"🌦️ Weather detected: {current_weather}")

if safe_speed < 60:
    print("⚠️ Warning: Poor driving conditions detected.")
    print(f"🔒 Speed limited to {safe_speed} mph for your safety.")
else:
    print("✅ Conditions are good.")
    print(f"🚀 Maximum speed set to {safe_speed} mph.")

print("🚗 Drive safe!")
