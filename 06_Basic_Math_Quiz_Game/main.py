# Basic Math Quiz Game
# Description: A simple math quiz game that asks the user to solve basic arithmetic problems.

import random

# Step  1 : Defining the Math Question Function
def generate_question():
    '''Generate a random math question and return the question and answer.'''

    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Randomly choose an operator
    operator = random.choice(['+', '-', '*'])

    # Perform the operation based on the operator
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    # Create the question string
    question = f"What is {num1} {operator} {num2}?"

    # Return the question and answer
    return question, answer


# Step 2 : Function for Feedback and Improvement
def feedback(score, rounds):
    '''Provide feedback based on the score.'''
    print("\n-----Feedback-----\n")
    print(f"You answered {score} out of {rounds} questions correctly.\n")
    # Provide feedback based on the score
    if score == rounds:
        print("Excellent! You got all questions right! 🌟\n")
    elif score >= rounds // 2:
        print("Good job! You did well! 👍\n")
    else:
        print("Don't worry! Keep practicing and you'll improve! 💪\n")


# Step 3: Main Quiz Function
def math_quiz():
    score = 0
    rounds = 5
    print("Welcome to the Math Quiz Game! 🎉\n")
    print(f"You will be asked {rounds} questions. Try to answer them correctly! 🧠\n")
    for i in range(rounds):
        question, answer = generate_question()
        print(f"Question {i + 1}: {question}")
        user_answer = int(input("Your answer: "))

        if user_answer == answer:
            print("Correct! 🎉\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}. ❌\n")
    print("Quiz Over! Thank you for playing! 🎮\n")

    # Provide feedback based on the score
    feedback(score, rounds)
    


# Step 4: Run the Quiz
if __name__ == "__main__":
    math_quiz()