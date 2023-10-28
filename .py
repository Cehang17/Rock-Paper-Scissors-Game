import random,time

possibleMoves = ["rock","paper","scissors"]

print("welcome to Rock Paper Scissors Game")
print("")
time.sleep(0.5)
time.sleep(2)
print("Rules:")
time.sleep(1)
print("There is no tour limit. You just have to reach 5 points before the computer.")
time.sleep(4)
print("Leave the move blank, if you want to end the game.")
time.sleep(2)
print("")
print("Let's start!")
print("")
time.sleep(2)

yourPoint = 0
computersPoint = 0
drawPoint = 0

while yourPoint != 5 and computersPoint != 5:
    print(possibleMoves)
    print("Choose your move: ",end="")
    computersMove = random.choice(possibleMoves)
    yourMove = input("").lower()
    if yourMove in possibleMoves:
        if yourMove == computersMove:
            print("Draw")
            print("")
            time.sleep(0.5)
            drawPoint = drawPoint + 1
        elif yourMove == "paper" and computersMove == "scissors":
            print("Computer won the tour")
            print("")
            time.sleep(0.5)
            computersPoint = computersPoint + 1
        elif yourMove == "rock" and computersMove == "paper":
            print("Computer won the tour")
            print("")
            time.sleep(0.5)
            computersPoint = computersPoint + 1
        elif yourMove == "scissors" and computersMove == "rock":
            print("Computer won the tour")
            print("")
            time.sleep(0.5)
            computersPoint = computersPoint + 1
        else:
            print("You won the tour")
            print("")
            time.sleep(0.5)
            yourPoint = yourPoint + 1
    else:
        if yourMove == "":
            print("Game over")
            break
        else:
            print("Please choose legal move! ")
            print("")
            time.sleep(0.5)
if yourPoint > computersPoint:
    print(f"Your Point {yourPoint} - {computersPoint} Computer's Point")
    print(f"You drew {drawPoint} times")
    print("you won the game, Congratulations! ")
elif yourPoint < computersPoint:
    print(f"Your Point {yourPoint} - {computersPoint} Computer's Point")
    print(f"You drew {drawPoint} times")
    print("you lost the game ")
else:
    print(f"Your Point {yourPoint} - {computersPoint} Computer's Point")
    print(f"You drew {drawPoint} times")
    print("Draw")
