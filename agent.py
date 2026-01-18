print("🤖 Intelligent Multimodal Travel Planning Agent Started")

import adbutils
import time

# =============================
# CONNECT TO ANDROID DEVICE
# =============================
adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
devices = adb.device_list()

if not devices:
    print("❌ No Android device connected")
    exit()

device = devices[0]
print("📱 Connected to device:", device.serial)

# =============================
# WAKE DEVICE
# =============================
device.shell("input keyevent KEYCODE_WAKEUP")
device.shell("input keyevent KEYCODE_HOME")
time.sleep(1)

# ==================================================
# STEP 1: GOOGLE MAPS — EXPLORE POPULAR PLACES
# ==================================================
device.shell(
    "monkey -p com.google.android.apps.maps "
    "-c android.intent.category.LAUNCHER 1"
)
time.sleep(5)

# Search popular places
device.shell("input tap 540 200")
time.sleep(1)
device.shell('input text "Top places to visit in Goa"')
device.shell("input keyevent KEYCODE_ENTER")
time.sleep(5)

# Open first visible place (demo recommendation)
device.shell("input tap 540 800")
time.sleep(4)

print("🗺️ Explored popular places in Goa using Google Maps")

# ==================================================
# STEP 2: BOOKING.COM — FIND CHEAP STAYS
# ==================================================
device.shell("input keyevent KEYCODE_HOME")
time.sleep(1)

device.shell(
    "monkey -p com.booking -c android.intent.category.LAUNCHER 1"
)
time.sleep(6)

# Switch to Stays tab
device.shell("input tap 200 2200")
time.sleep(2)

# Search destination
device.shell("input tap 540 500")
time.sleep(1)
device.shell('input text "Goa"')
time.sleep(2)
device.shell("input tap 540 750")
time.sleep(4)

print("📍 Destination selected: Goa")

# ==================================================
# STEP 3: FLEXIBLE WEEKEND FLOW (SAFE & STABLE)
# ==================================================
# Booking shows "I'm flexible" → Weekend → Month
time.sleep(2)

# Confirm flexible dates
device.shell("input tap 540 2250")   # "Select dates"
time.sleep(5)

# Re-trigger search (Booking requires this)
device.shell("input tap 540 1800")   # "Show stays"
time.sleep(6)

print("📅 Weekend trip selected (flexible dates)")

# ==================================================
# STEP 4: PRICE OPTIMIZATION (ROBUST)
# ==================================================
# Sort by lowest price
device.shell("input tap 900 350")    # Sort
time.sleep(2)

device.shell("input tap 540 750")    # Lowest price first
time.sleep(5)

print("💰 Sorted stays by lowest price")

# ==================================================
# STEP 5: RECOMMENDATION (SAFE STOP)
# ==================================================
# Open one recommended affordable stay
device.shell("input tap 540 900")
time.sleep(4)

print("🏨 Recommended affordable stay opened")
print("✅ Travel plan generated successfully")
print("ℹ️ Final booking left to user confirmation")
