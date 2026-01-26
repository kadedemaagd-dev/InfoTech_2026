# ============================
# Welcome Branch
# ============================

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
    x += 1

    # Create the boot message with animated dots
    ellipsisMessage = (
        YELLOW
        + "InfoTechCenter OS Booting"
        + "." * ellipsis
        + RESET
    )

    # Write message to the same console line
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()

    # Increase dot count for next frame
    ellipsis += 1

    # Pause to control animation speed
    time.sleep(0.5)

    # Reset dots after reaching 3
    if ellipsis == 4:
        ellipsis = 0

# Display final success message once boot completes
print(
    GREEN
    + BRIGHT
    + "\nOperating System Booted Up - Retina Scanned - Access Granted"
    + RESET
)