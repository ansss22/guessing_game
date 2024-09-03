import random

def easy():
    global random_number
    attempts = 10 
    while attempts > 0 : 
        print(f"You have {attempts} remaining to guess the number. ")
        answer = int(input("make a guess : "))
        if answer > random_number :
            print("To hight")
        elif answer < random_number:
            print("To low")            
        elif answer == random_number:
            print(f"You got it! The answer was {random_number}")
            break       
        attempts -= 1
        if attempts > 0:
            print(f"Guess again. You have {attempts} attempts remaining.")
        else:
            print(f"You've run out of attempts. The correct number was {random_number}.")

def hard():
    global random_number
    attempts = 5 
    while attempts > 0 : 
        print(f"You have {attempts} attempts remaining to guess the number.  ")
        answer = int(input("make a guess : "))
        if answer > random_number :
            print("To hight")
        elif answer < random_number:
            print("To low") 
        elif answer == random_number:
            print(f"You got it! The answer was {random_number}")
            break       
        attempts -= 1
        if attempts > 0:
            print(f"Guess again. You have {attempts} remaining.")
        else:
            print(f"You've run out of attempts. The correct number was {random_number}.")


random_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard':")
if choice == "easy" :
    easy()
elif choice == "hard" :
    hard()

