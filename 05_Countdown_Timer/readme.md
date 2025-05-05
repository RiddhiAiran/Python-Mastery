# ⏳ Countdown Timer

A simple and interactive Python program that functions as a countdown timer, counting down from a user-specified number of seconds to zero.

## 📝 Description

This script allows users to:

- Enter the countdown time in seconds.
- Watch the countdown happen in real-time.
- Get notified when the countdown is complete.

It utilizes Python's built-in `time` module for delays and a `while` loop to manage the countdown process.

---

## 💡 How It Works

1. **User Input**:
   - Asks the user to enter the number of seconds for the countdown.
2. **Countdown Logic**:
   - Uses a `while` loop to count down one second at a time.
   - `time.sleep(1)` pauses execution for one second between prints.
3. **Completion**:
   - When the countdown reaches zero, a final message is displayed.

---

## 🧪 Example

```bash
Enter the countdown time in seconds: 5
```

📤 Output:

```
🙏🏼-----Countdown Timer----- 🙏🏼

----Countdown Begins ----

5
4
3
2
1

----Countdown Finished ----

Time's up! The countdown has reached zero.
```

---

## 🚀 Getting Started

To run the program:

1. Ensure **Python 3** is installed.
2. Save the code in a file named `countdown_timer.py`.
3. Run the script using the command:

```bash
python countdown_timer.py
```

---

## 📧 Author

Created with ❤️ to help beginners explore real-time programming in Python.

---
