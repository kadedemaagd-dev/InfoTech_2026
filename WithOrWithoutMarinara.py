# Welcome Branch

# Libraries Imported Here
import sys
import time

# ANSI color codes
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BRIGHT = "\033[1m"
RESET = "\033[0m"

print(CYAN + "\nWelcome Branch - Developer: Kade DeMaagd" + RESET)
print(GREEN + "\nWelcome to InfoTechCenter V.1.0" + RESET)

x = 0
ellipsis = 0

while x != 20:
    x += 1

    ellipsisMessage = (
        YELLOW
        + "InfoTechCenter OS Booting"
        + "." * ellipsis
        + RESET
    )

    ellipsis += 1
    sys.stdout.write("\r" + ellipsisMessage + "   ")
    sys.stdout.flush()
    time.sleep(.5)

    if ellipsis == 4:
        ellipsis = 0

    if x == 20:
        print(
            GREEN
            + BRIGHT
            + "\nOperating System Booted Up - Retina Scanned - Access Granted"
            + RESET
        )