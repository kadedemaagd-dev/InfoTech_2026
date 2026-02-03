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