print("Welcome to Quiz Game")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("**Okay! Let's PLay** ")

answer = input("What is CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What is GPU stand for? ")
if answer == "Graphical processing unit":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What is RAM stand for? ")
if answer == "Random access memory":
    print("Correct!")
else:
    print("Incorrect!")
