# Countown Timer
# Description: A simple countdown timer that takes a number of seconds as input and counts down to zero.
import time
import datetime

print("\n 🙏🏼-----Countdown Timer----- 🙏🏼\n")
# Step 1: Take User Input for Countdown Time 
countdown_time = int(input("Enter the countdown time in seconds: "))

# Step 2: Countdown using a While Loop
print("\n----Countdown Begins ----\n")

while countdown_time > 0:
    print(countdown_time)
    time.sleep(1)  # Sleep for 1 second
    countdown_time -= 1

# Step 3: Print Final Message
print("\n----Countdown Finished ----\n")
print("Time's up! The countdown has reached zero.")


