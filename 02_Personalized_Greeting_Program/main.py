# Personalized Greeting Program
# Description: This program asks the user for their name, age, and favorite color, then generates a personalized greeting message.

# Step 1: Ask for User Details
Name = input("What's your Name? :  ").title()
Age = int(input("What's your Age? : "))
color = input("What's your Favorite color? : ").title()

# Step 2: Generate a Personalized Greeting Message
print("\n 🙏🏼 -----Personalized Greeting----- 🙏🏼 \n")
print(f"Hello {Name}! 👋🏻 \n")
print(f"You are {Age} years old, and {color} is a beautiful color! 🎨 \n")
print("You're now ready to embark on an exciting journey with Python! 🚀 \n")