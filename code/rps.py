from random import randint

t = ["Rock","Paper","Scissors"]
computer = t[randint(0,2)]

player = input("Rock, Paper, Scissors? ")

if player == computer:
  print("we have a tie!")
elif player == "Rock":
  if computer == "Paper":
    print(f"Computer guessed {computer}. So sorry, you lose")
  else:
    print(f"Computer guessed {computer}. You win!")
elif player == "Paper":
  if computer == "Scissors":
    print(f"Computer guessed {computer}. So sorry, you lose")
  else:
    print(f"Computer guessed {computer}. You win!")
elif player == "Scissors":
  if computer == "Rock":
    print(f"Computer guessed {computer}. So sorry, you lose")
  else:
    print(f"Computer guessed {computer}. You win!")
else:
  print("Something went wrong. Try again")

computer = t[randint(0,2)]