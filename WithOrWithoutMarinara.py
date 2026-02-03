import random

# ==============================
# Gasoline Brach - Fake Phone App
# ==============================

print("📱 Gasoline Brach - Fake Phone App")
print("Scanning for nearby gas stations...\n")

# ------------------------------
# Fake gas stations database
# Each station has:
# - name: station name
# - distance: miles away
# - price: gas price per gallon
# - open: whether the station is open
# - coke_slushie: if they have Coke Slushies
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
# Assume full tank = 400 miles
# ------------------------------
miles_left = int((gas / 100) * 400)
print(f"Estimated Range: {miles_left} miles\n")

# ------------------------------
# Find nearest gas station
# ------------------------------
nearest = min(stations, key=lambda s: s["distance"])

# ------------------------------
# Find cheapest gas station
# ------------------------------
cheapest = min(stations, key=lambda s: s["price"])

# ------------------------------
# Display nearest station info
# ------------------------------
print("📍 Nearest Gas Station:")
print(f"  {nearest['name']} - {nearest['distance']} miles away")
print(f"  Status: {'OPEN' if nearest['open'] else 'CLOSED'}")

# ------------------------------
# Display cheapest station info
# ------------------------------
print("\n💲 Cheapest Gas Station:")
print(f"  {cheapest['name']} - ${cheapest['price']:.2f} per gallon")
print(f"  Status: {'OPEN' if cheapest['open'] else 'CLOSED'}")

# ------------------------------
# Gas alarm logic
# ------------------------------
if gas <= 25:
    print("\n🔔 GAS ALARM: Fuel is low!")

    # Check if you can reach nearest station
    if miles_left < nearest["distance"]:
        print("⚠️ WARNING: You may NOT have enough fuel to reach the nearest station!")
    else:
        print("✅ You should be able to reach the nearest station.")

# ------------------------------
# Fake AI Suggestions section
# ------------------------------
print("\n🤖 AI Suggestions:")

if gas <= 10:
    print("- Fuel critically low. Stop at the NEAREST open station immediately.")
elif gas <= 25:
    # Decide between cheapest and nearest
    if cheapest["open"] and miles_left >= cheapest["distance"]:
        print("- Consider driving to the cheapest station to save money.")
    else:
        print("- Nearest station is recommended due to low fuel.")
else:
    print("- Fuel level is healthy. You can wait for a better price if desired.")

# ------------------------------
# Ask user if they want to check
# for Coke Slushies
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

# ------------------------------
# End of program
# ------------------------------
print("\nDone.")
