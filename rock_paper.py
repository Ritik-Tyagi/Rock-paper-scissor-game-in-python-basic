import random
def rock_paper_scissor( value):
  computer_moves = random.choice(["rock", "paper", "scissor"])
  print("Computer_move ->", dic[computer_moves])
  if player1 == 1 and computer_moves == "scissor":
    print("Player_Win ->", dic["rock"])
    return "rock"

  elif player1 == 2 and computer_moves == "rock":
    print("Player_win ->", dic["paper"])

    return "paper"
  elif player1 == 3 and computer_moves == "paper":
    print("Player_win ->",dic["scissor"])
    
    return "scissor"
  elif player1 == 1 and computer_moves == "paper":
    print("Computer_Win ->", dic["paper"])

    return "paper"
  elif player1 == 2 and computer_moves == "scissor":
    print("Computer_Win ->", dic["scissor"])

    return "scissor"
  elif player1 == 3 and computer_moves == "rock":
    print("Computer_Win ->", dic["rock"])

    return "rock"
  elif player1 == 1 and computer_moves == "rock" or player1 == 2 and computer_moves == "paper" or player1 == 3 and computer_moves == "scissor":
    print("Tie")

    return "Tie"


dic = {"rock": "🪨", "scissor": "✂️", "paper": "📄"}

Player1_wins = 0
Computer_wins = 0
Draw = 0
while True:
  print("Do you want to play please press -> 1")
  print("Do you want to exit in the game please press -> 2")
  quari = int(input())
  if quari == 1:
    print("if you want to chose rock 🪨  -> press 1")
    print("if you want to chose paper📄  -> press 2")
    print("if you want to chose scissor ✂️  -> press 3")
    
    player1 = int(input())
    if player1 == 1:
      print("Player_move ->", dic["rock"])
      a = rock_paper_scissor( "rock")
      if a == "rock":
        Player1_wins+= 1
      elif a == "Tie":
        Draw+= 1
      else:
        Computer_wins+= 1
    elif player1 == 2:
      print("Player_move ->",dic["paper"])
      a = rock_paper_scissor( "paper")
      if a == "paper":
        Player1_wins += 1
      elif a == "Tie":
        Draw+= 1
      else:
        Computer_wins += 1

    elif player1 == 3:
      print("Player_move ->",dic["scissor"])
      a = rock_paper_scissor( "scissor")
      if a == "scissor":
        Player1_wins += 1
      elif a == "Tie":
        Draw+= 1
      else:
        Computer_wins += 1
    else:
      print("⚠️  plese provide me valid input")
  else:
    print("Your Game Score")
    print("Player: ", Player1_wins, "Computer: ", Computer_wins, "Tie_Match: ",
          Draw)

    break
