# This is a main file where the project execution starts .
#Import the questions.py file into main file

from questions import questions
import random # random is a built-in python module

# we need 2 methods , 1.main and 2.random
# define a random function used to get question in a random way.
#random.choice--> is a selecting a random question from the list and printing it.
def show_random_question():
    q = random.choice(questions)
    print("Questions are: ",q)

# In main function we call the defined random function if condition is true.
def main():
    print("Welcome to Python Interview practice!")
    while True:
        show_random_question()
        user_input =input("Press Enter for next question or type exit to quit: ")
        if user_input.lower()=="exit":
            print("Thanks for practicing!See you soon bye 👋")
            break

# line ensures main will be executed only if file is executed directly.
if __name__ =="__main__":
    main()




