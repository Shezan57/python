# Guess the Number Game with Loops and Conditionals
# Step1: Import the random module to generate a random number between 1 and 100.
import random
random_number = random.randint(1,100)

# Step2: Ask the user to guess a number.

guess_number = int(input("Guess a number between 1 and 100: "))

# Step3: Use a while loop to continue the game until the user guesses the correct number.
while guess_number != random_number:
    if guess_number < random_number:       # Step4: Inside the while loop, use an if statement to compare the user's guess with the random number.
        print("Number is too low, try again")   # Step5:If the guess is too low, print a hint like "Too low, try again!"
    else:
        print("Number is too high, try again")     # If the guess is too high, print a hint like "Too high, try again!"

    guess_number = int(input("Guess again: "))
    
print("Congratulation!! you won the game")  # If the guess is correct, print a congratulatory message and break out of the loop.

