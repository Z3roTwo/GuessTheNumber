import random
import json

loop = True
guess = 0
number = 0
rounds = 0
name = 0
#q = 0

name = input("Display name: ")
number = random.randint(1, 10)
#try:
    #with open('Storage.json', 'r') as JSON:
        #data = json.load(JSON)
        #type(data)
        #print(data["name"])
        #q = data[rounds]
#except:
    #print("2qerrqwreasdf")

# Debug thingy
# print(number)
print(f"Ok {name} the PC have selected a number between 1 - 10")
while loop:
    try:
        guess = int(input("Your guess: "))
        rounds += 1
        if guess > number:
            print("Aw too bad that's the wrong number, it's too high! :(")
        elif guess < number:
            print("Aw too bad that's the wrong number, it's to low! :(")
        elif guess == number:
            print(f"Congrats you did it! The number was {number} and it only took you {rounds} rounds :D")
            loop = False
            #if rounds < int(q):
                #x = {"name": name, "rounds": rounds}
                # Sparar x i Storage.json
                #f = open('Storage.json', 'w')
                #json.dump(x, f)
                # Stänger filen
                #f.close()
        else:
            print("Oops something went wrong and the code didn't crash for some reason....")
    except:
        print("Please enter a number between 1 and 10")