print("Welcome to Quiz Game")

playing = input("Do you want to play ? ")

if playing.lower() != "yes":
    quit()

print("**Okay! Let's Play** ")
score = 0

answer = input("What is CPU stand for ? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is GPU stand for ? ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is RAM stand for ? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 3) * 100) + "%.")
