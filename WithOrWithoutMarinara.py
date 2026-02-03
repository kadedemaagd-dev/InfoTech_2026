
#BetaTestDev

# Welcome Branch
# Libraries imported here
# sys  -> allows writing to the same console line
# time -> used to control delays for animation
import sys
import time

# ANSI escape codes for terminal colors and formatting
CYAN = "\033[36m"     # Cyan text
GREEN = "\033[32m"    # Green text
YELLOW = "\033[33m"   # Yellow text
BRIGHT = "\033[1m"    # Bright / bold text
RESET = "\033[0m"     # Reset to default formatting

# Display startup information
print(CYAN + "\nWelcome Branch - Developer: Kade DeMaagd" + RESET)
print(GREEN + "\nWelcome to InfoTechCenter V.1.0" + RESET)

# Counter to control how long the boot animation runs
x = 0

# Controls how many dots appear after "Booting"
ellipsis = 0

# Loop runs until x reaches 20 (boot animation length)
while x != 20:
    # Increment loop counter
    x += 1

    # Create the boot message with animated dots
    ellipsisMessage = (
        YELLOW
        + "InfoTechCenter OS Booting"
        + "." * ellipsis
        + RESET
    )

    # Increase dot count for the next frame
    ellipsis += 1

    # Write message to the same console line
    sys.stdout.write("\r" + ellipsisMessage + "   ")
    sys.stdout.flush()

    # Pause to control animation speed
    time.sleep(.5)

    # Reset dots after reaching 3
    if ellipsis == 4:
        ellipsis = 0

    # Display final success message once boot completes
    if x == 20:
        print(
            GREEN
            + BRIGHT
            + "\nOperating System Booted Up - Retina Scanned - Access Granted"
            + RESET
        )


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


import random
import time

# ==============================
# Gasoline Brach - Fake Phone App
# ==============================

print("📱 Gasoline Brach - Fake Phone App")
print("Scanning for nearby gas stations...\n")

# ------------------------------
# Fake gas stations database
# ------------------------------
stations = [
    {"name": "Marathon", "distance": 0.8, "price": 3.45, "open": True,  "coke_slushie": True},
    {"name": "Speedway", "distance": 1.5, "price": 3.29, "open": True,  "coke_slushie": False},
    {"name": "Circle K", "distance": 2.1, "price": 3.39, "open": False, "coke_slushie": True},
    {"name": "Meijer Express", "distance": 4.3, "price": 3.19, "open": True,  "coke_slushie": True},
    {"name": "Shell", "distance": 3.0, "price": 3.49, "open": True,  "coke_slushie": False}
]

# ------------------------------
# Fake gas level (0 to 100%)
# ------------------------------
gas = random.randint(0, 100)
print(f"Gas Level: {gas}%\n")

# ------------------------------
# Fake range estimate
# ------------------------------
miles_left = int((gas / 100) * 400)
print(f"Estimated Range: {miles_left} miles\n")

# ------------------------------
# Show distance to ALL stations
# ------------------------------
print("🗺️ Distances to Nearby Gas Stations:")
for s in stations:
    print(f"  {s['name']}: {s['distance']} miles away")

# ------------------------------
# Find nearest and cheapest
# ------------------------------
nearest = min(stations, key=lambda s: s["distance"])
cheapest = min(stations, key=lambda s: s["price"])

print("\n📍 Nearest Gas Station:")
print(f"  {nearest['name']} - {nearest['distance']} miles away")
print(f"  Status: {'OPEN' if nearest['open'] else 'CLOSED'}")

print("\n💲 Cheapest Gas Station:")
print(f"  {cheapest['name']} - ${cheapest['price']:.2f} per gallon")
print(f"  Status: {'OPEN' if cheapest['open'] else 'CLOSED'}")

# ------------------------------
# Gas alarm logic
# ------------------------------
low_gas = False

if gas <= 25:
    low_gas = True
    print("\n🔔 GAS ALARM: Fuel is low!")

    if miles_left < nearest["distance"]:
        print("⚠️ WARNING: You may NOT have enough fuel to reach the nearest station!")
    else:
        print("✅ You should be able to reach the nearest station.")

# ------------------------------
# Fake AI Suggestions
# ------------------------------
print("\n🤖 AI Suggestions:")

if gas <= 10:
    print("- Fuel critically low. Stop at the NEAREST open station immediately.")
elif gas <= 25:
    if cheapest["open"] and miles_left >= cheapest["distance"]:
        print("- Consider driving to the cheapest station to save money.")
    else:
        print("- Nearest station is recommended due to low fuel.")
else:
    print("- Fuel level is healthy. You can wait for a better price if desired.")

# ------------------------------
# FAKE Wake-Up Alarm Feature
# ------------------------------
if low_gas:
    print("\n⏰ WAKE-UP ALARM SET!")
    print("Because gas is low, an earlier wake-up alarm is scheduled.")
    print("Alarm time moved earlier to remind you to get gas.")

    # Simulate alarm going off (fake)
    print("\n⏰ ALARM RINGING EARLY!")
    for i in range(3):
        print("🔊 BEEP! WAKE UP! GET GAS!")
        time.sleep(1)
else:
    print("\n⏰ No early alarm needed. Gas level is okay.")

# ------------------------------
# Coke Slushie check
# ------------------------------
answer = input("\nDo you want to check for Coke Slushies? (yes/no): ").strip().lower()

if answer == "yes":
    print("\n🥤 Coke Slushie Availability (Open Stations Only):")
    for s in stations:
        if s["open"]:
            if s["coke_slushie"]:
                print(f"  {s['name']}: ✅ Has Coke Slushie")
            else:
                print(f"  {s['name']}: ❌ No Coke Slushie")
else:
    print("\nSlushie check skipped.")

print("\nDone.")

