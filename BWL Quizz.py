print("Welcome to my BWL Quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets play :)")

score = 0

# Question 1
answer = input("What does BWL stand for? ")

if answer.lower() == "betriebswirtschaftslehre":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 2
answer = input("What is profit? ")

if answer.lower() == "revenue minus costs":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 3
answer = input("What does ROI stand for? ")

if answer.lower() == "return on investment":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 4
answer = input("Which department is responsible for advertising? ")

if answer.lower() == "marketing":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 5
answer = input("What does CEO stand for? ")

if answer.lower() == "chief executive officer":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Final Score
print("You got " + str(score) + " questions correct!")

percentage = (score / 5) * 100

print("You achieved " + str(percentage) + "%")