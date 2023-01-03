"""
11. Rock Paper Scissors!
    Let's play! You have to return which player won! In case of a draw return Draw!.
    Examples(Input1, Input2 --> Output):
    "scissors", "paper" --> "Player 1 won!"
    "scissors", "rock" --> "Player 2 won!"
    "paper", "paper" --> "Draw!"

"""

def game(input1,input2):
    if input1 == input2:
        return "Draw"
    elif ((input1 == "rock") and (input2 == "scissors")) or ((input1 == "paper") and (input2 == "rock")) or((input1 == "scissors") and (input2 == "paper")):
        return "Player 1 Won!"
    else:
        return "Player 2 Won" 


if __name__ == '__main__':
    print(game("scissors", "paper"))
    print(game("scissors", "rock"))
    print(game("paper", "paper"))
    