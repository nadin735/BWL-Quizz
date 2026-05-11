print("Welcome to my BWL Quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

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

# Question 6
answer = input("What is the main goal of a company? ")

if answer.lower() == "profit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 7
answer = input("What does HR stand for? ")

if answer.lower() == "human resources":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 8
answer = input("Which department manages company money? ")

if answer.lower() == "finance":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 9
answer = input("What does SWOT stand for? ")

if answer.lower() == "strengths weaknesses opportunities threats":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 10
answer = input("What is marketing used for? ")

if answer.lower() == "promoting products":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 11
answer = input("What does KPI stand for? ")

if answer.lower() == "key performance indicator":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 12
answer = input("What is revenue? ")

if answer.lower() == "income from sales":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Final Score
print("You got " + str(score) + " questions correct!")

percentage = (score / 12) * 100

print("You achieved " + str(percentage) + "%")

# Rating
if percentage == 100:
    print("Excellent! Perfect score!")
elif percentage >= 70:
    print("Very Good!")
elif percentage >= 50:
    print("Good effort!")
else:
    print("Keep practicing!")