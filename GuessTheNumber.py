import random

loop = True
guess = 0
number = 0

number = random.randint(1, 10)
print(number)
print("The PC have selected a number between 1 - 10")
while loop:
    try:
        guess = int(input("Your guess: "))
        if guess > number:
            print("Aw too bad that's the wrong number, it's too high! :(")
        elif guess < number:
            print("Aw too bad that's the wrong number, it's to low! :(")
        elif guess == number:
            print("Congrats you did it! :D")
            loop = False
        else:
            print("Oops something went wrong and the code didn't crash for some reason....")
    except:
        print("Please enter a number between 1 and 10")