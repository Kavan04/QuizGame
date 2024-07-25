print("Welcome To The Computer Trivia\n")
print("*" * 30)

playing = input("Are you playing? (yes/no): ")

score = 0
player_name = input("What is your name? ")
print("\n")

if playing.lower() != "yes":
  print("Alright, See you soon!")
  quit()

print(f'''Okay {player_name} let's start!!\n''')

answer = input("What does a CPU stand for? ").lower()

if answer == "central processing unit":
  score += 1
  print("Correct! +1 point")
else:
  print("Incorrect Answer!, Try again\n ")

answer = input("What does a GPU stand for? ").lower()

if answer == "graphics processing unit":
  score += 1
  print("Correct! +1 point")
else:
  print("Incorrect Answer!, Try again \n")

answer = input("What does a PSU stand for? ").lower()

if answer == "power supply":
  score += 1
  print("Correct! +1 point")
else:
  print("Incorrect Answer!, Try again \n")

answer = input("What does a RAM stand for? ").lower()

if answer == "random acess memory":
  score += 1
  print("Correct! +1 point")
else:
  print("Incorrect Answer!, Try again \n")

print(f'You got {score} correct')
print(f'You got {(score/4) * 100} percent correct')
