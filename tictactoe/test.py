from tictactoe import player, actions, result, winner, terminal, utility, minimax

X = "X"
O = "O"
EMPTY = None

board = [[X, X, X],
         [O, X, O],
         [O, X, X]]

print(terminal(board))
