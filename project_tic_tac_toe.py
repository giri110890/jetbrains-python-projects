# Author giri110890
# write your code here
game = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
game_set = ("X", "O")
turn = "X"
matrix = [[1, 3], [2, 3], [3, 3],
          [1, 2], [2, 2], [3, 2],
          [1, 1], [2, 1], [3, 1]]


def check_game():
    if game[0] == game[1] == game[2] and game[0] in game_set:
        print_game()
        print(game[0] + " wins")
        return True
    elif game[3] == game[4] == game[5] and game[3] in game_set:
        print_game()
        print(game[3] + " wins")
        return True
    elif game[6] == game[7] == game[8] and game[6] in game_set:
        print_game()
        print(game[6] + " wins")
        return True
    elif game[0] == game[3] == game[6] and game[0] in game_set:
        print_game()
        print(game[0] + " wins")
        return True
    elif game[1] == game[4] == game[7] and game[1] in game_set:
        print_game()
        print(game[1] + " wins")
        return True
    elif game[2] == game[5] == game[8] and game[2] in game_set:
        print_game()
        print(game[2] + " wins")
        return True
    elif game[0] == game[4] == game[8] and game[0] in game_set:
        print_game()
        print(game[4] + " wins")
        return True
    elif game[2] == game[4] == game[6] and game[2] in game_set:
        print_game()
        print(game[4] + " wins")
        return True
    elif " " not in game:
        print_game()
        print("Draw")
        return True


def print_game():
    print(f"""---------
| {game[0]} {game[1]} {game[2]} |
| {game[3]} {game[4]} {game[5]} |
| {game[6]} {game[7]} {game[8]} |
---------""")


while True:
    try:
        print_game()
        x, y = input("Enter the coordinates:").split()
        x = int(x)
        y = int(y)
        if not 1 <= x <= 3 or not 1 <= y <= 3:
            print("Coordinates should be from 1 to 3!")
        else:
            cell_number = matrix.index([x, y])
            if game[cell_number] == "X" or game[cell_number] == "O":
                print("This cell is occupied! Choose another one!")
            else:
                if turn == "X":
                    game[cell_number] = "X"
                    turn = "O"
                    if check_game():
                        break
                else:
                    game[cell_number] = "O"
                    turn = "X"
                    if check_game():
                        break
    except ValueError:
        print("You should enter number")
