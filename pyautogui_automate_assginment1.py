import pyautogui
import time
from datetime import datetime
import pyperclip
import os

# ==================================================
# CONFIGURATION
# ==================================================

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

# EXACT folder
TARGET_FOLDER = r"E:\AI\Ai_Git_practice"

# EXACT filename
FILENAME = "daily_report.xlsx"

# Create folder
os.makedirs(TARGET_FOLDER, exist_ok=True)

# Complete path
FULL_PATH = os.path.join(TARGET_FOLDER, FILENAME)

print("Target folder :", TARGET_FOLDER)
print("Target file   :", FILENAME)
print("Full path     :", FULL_PATH)


# ==================================================
# FUNCTION: HANDLE EXCEL SAVE DIALOGS
# ==================================================

def handle_save_dialogs():
    """
    Automatically handles common Excel save dialogs.

    Possible dialogs:
    1. Confirm Save As / Replace existing file
    2. Excel format warning
    3. Save changes confirmation
    """

    print("Checking for Excel confirmation dialogs...")

    # Give Excel time to display the dialog
    time.sleep(2)

    # ----------------------------------------------
    # Dialog 1:
    # "Do you want to replace it?"
    # ----------------------------------------------

    # If dialog has Yes / No buttons, pressing
    # Alt+Y usually activates Yes.
    pyautogui.hotkey("alt", "y")
    time.sleep(2)

    # ----------------------------------------------
    # Dialog 2:
    # "This document may contain features..."
    #
    # Usually buttons:
    # Continue / Cancel
    # or
    # Use Excel Format / Use CSV Format
    # ----------------------------------------------

    # Try Enter for the default confirmation
    pyautogui.press("enter")
    time.sleep(2)


# ==================================================
# 1. OPEN CHROME
# ==================================================

print("\nOpening Chrome...")

pyautogui.hotkey("win", "r")
time.sleep(1)

pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(4)


# ==================================================
# 2. OPEN WEBSITE
# ==================================================

pyautogui.hotkey("ctrl", "l")

pyautogui.write("https://fcainfoweb.nic.in/")
pyautogui.press("enter")

time.sleep(6)


# ==================================================
# 3. FIND REQUIRED DATA
# ==================================================

print("Searching for All India Average Retail Price...")

pyautogui.hotkey("ctrl", "f")

pyautogui.write("All India Average Retail Price")

pyautogui.press("enter")
pyautogui.press("esc")

time.sleep(1)

# Move to found section
pyautogui.press("home")


# Select text
pyautogui.keyDown("shift")

for _ in range(30):
    pyautogui.press("down")

pyautogui.keyUp("shift")


# Copy
pyautogui.hotkey("ctrl", "c")

time.sleep(1)

# Read clipboard
data = pyperclip.paste()

print("\nFetched data:")
print("--------------------------------")
print(data)
print("--------------------------------")


# ==================================================
# 4. OPEN EXCEL
# ==================================================

print("\nOpening Excel...")

pyautogui.hotkey("win", "r")

time.sleep(1)

pyautogui.write("excel")
pyautogui.press("enter")

time.sleep(6)

# Open blank workbook if start screen appears
pyautogui.press("enter")

time.sleep(4)


# ==================================================
# 5. ENTER DATA
# ==================================================

print("Entering data into Excel...")

# Date & time
current_datetime = datetime.now().strftime(
    "%Y-%m-%d %H:%M:%S"
)

pyautogui.write(current_datetime)

# Next column
pyautogui.press("tab")

# Fetched data
pyperclip.copy(data)

pyautogui.hotkey("ctrl", "v")

# Next column
pyautogui.press("tab")

# Comment column
pyautogui.write("")

pyautogui.press("enter")

time.sleep(2)


# ==================================================
# 6. DELETE EXISTING FILE
# ==================================================

if os.path.exists(FULL_PATH):

    print("\nExisting file found.")

    try:

        os.remove(FULL_PATH)

        print("Existing file deleted.")

    except PermissionError:

        print(
            "\nERROR: File is currently open.\n"
            "Close the existing Excel file and "
            "run the script again."
        )

        pyautogui.hotkey("alt", "f4")

        raise SystemExit


# ==================================================
# 7. SAVE AS EXACT PATH
# ==================================================

print("\nOpening Excel Save As...")

pyautogui.hotkey("ctrl", "shift", "s")

#time.sleep(2)

#pyautogui.press("tab")
#pyautogui.press("tab")
#pyautogui.press("tab")
#pyautogui.press("enter")
#pyautogui.hotkey("alt","A")
#pyautogui.hotkey("alt","O")


# ==================================================
# ENTER COMPLETE PATH
# ==================================================

#print("Entering save path:")

#print(FULL_PATH)

#pyperclip.copy(FULL_PATH)

# Select current filename
#pyautogui.hotkey("ctrl", "a")

# Paste complete path
#pyautogui.hotkey("ctrl", "v")

#time.sleep(1)


# ==================================================
# PRESS SAVE
# ==================================================

#print("Pressing Save...")

#pyautogui.press("enter")

#time.sleep(4)


# ==================================================
# AUTOMATICALLY SELECT YES
# ==================================================

#print("Handling Save confirmation...")

# Try ALT + Y
# This activates a button containing Y,
# usually "Yes".
#pyautogui.hotkey("alt", "OK")
#pyautogui.press("tab")
#pyautogui.press("enter")

#time.sleep(3)


# If the dialog is still present, press Enter
#pyautogui.press("enter")

#time.sleep(4)


# ==================================================
# VERIFY FILE
# ==================================================

#print("\nChecking whether file exists...")

if os.path.exists(FULL_PATH):

    print("\n========================================")
    print("SUCCESS")
    print("========================================")

    print("File saved successfully:")
    print(FULL_PATH)

else:

    print("\nFile not found yet.")

    # Give Excel additional time
    time.sleep(3)

    if os.path.exists(FULL_PATH):

        print("\nSUCCESS")
        print("File saved:")
        print(FULL_PATH)

    else:

        print("\n========================================")
        print("ERROR")
        print("========================================")

        print("Excel did not create the file.")
        print("Expected path:")
        print(FULL_PATH)


# ==================================================
# 8. TAKE SCREENSHOT
# ==================================================

print("\nTaking screenshot...")

SCREENSHOT_PATH = os.path.join(
    TARGET_FOLDER,
    "screenshot.png"
)

pyautogui.screenshot().save(
    SCREENSHOT_PATH
)

print("Screenshot saved:")
print(SCREENSHOT_PATH)


# ==================================================
# 9. CLOSE EXCEL
# ==================================================

print("\nClosing Excel...")

pyautogui.hotkey("alt", "f4")

time.sleep(3)


# ==================================================
# 10. HANDLE FINAL SAVE CONFIRMATION
# ==================================================

# If Excel asks:
#
# "Do you want to save changes?"
#
# choose Yes / Save.
#
# Alt+Y normally selects Yes.

pyautogui.hotkey("alt", "y")

time.sleep(2)

# If dialog uses Save as default button
pyautogui.press("enter")

time.sleep(3)


# ==================================================
# COMPLETE
# ==================================================

print("\n========================================")
print("AUTOMATION COMPLETED")
print("========================================")

print("Excel file:")
print(FULL_PATH)

print("\nScreenshot:")
print(SCREENSHOT_PATH)
