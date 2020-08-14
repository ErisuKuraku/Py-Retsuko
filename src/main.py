import os

print("********** Welcome to Py-Suko! ***********")
print("A Python version of Retsuko by Erisu Kuraku.")
print(" ")
print("Select your screensaver:")
print("1. ColourBars")
print("2. PlaceHolder")

selection = input("Please enter number (1-2):")

if selection == "1":
 print("Launching ColourBars....")
 os.system('cmd /c "start %appdata%\py-Retsuko/screensaver.scr /s"')

else:
 print("Placeholder")
