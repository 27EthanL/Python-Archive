# Python Library / Module
import random

# Input - Information
name = "Ethan"
question = "Will I be rich?"
answer = ""

# Random Integer Generator
random_number = random.randint(1,13)

# All the possible answers
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better now tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "No clue"
elif random_number == 11:
  answer = "Absolutely - NOT"
elif random_number == 12:
  answer = "Among Us?"
elif random_number == 13:
  answer = "Absolutely - Yes"
else:
  answer = "Error"

# Check for question and name
if question == "" or question == " ":
  print("There is no question you doofus")
else:
  if name == "" or name == " ":
    print("Question:", question)
  else:
    print(name, "asks:", question)
    print("Magic 8-Ball's answer:", answer)