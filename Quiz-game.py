print("Welcome to Quiz Game")

playing = input("Do you want to play ? ")

if playing.lower() != "yes":
    quit()

print("**Okay! Let's Play** ")
score = 0

answer = input("What is the biggest island in the World?")
if answer.lower() == "Greenland":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the largest tropical rain forest in the world? ")
if answer.lower() == "Amazon":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Spain? ")
if answer.lower() == "Madrid":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 3) * 100) + "%.")
