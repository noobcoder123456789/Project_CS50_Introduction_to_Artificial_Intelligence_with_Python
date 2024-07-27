# Understanding
There are two main files in this project: runner.py and tictactoe.py. tictactoe.py contains all of the logic for playing the game, and for making optimal moves. runner.py has been implemented for you, and contains all of the code to run the graphical interface for the game. Once you’ve completed all the required functions in tictactoe.py, you should be able to run python runner.py to play against your AI!

Let’s open up tictactoe.py to get an understanding for what’s provided. First, we define three variables: X, O, and EMPTY, to represent possible moves of the board.

The function initial_state returns the starting state of the board. For this problem, we’ve chosen to represent the board as a list of three lists (representing the three rows of the board), where each internal list contains three values that are either X, O, or EMPTY. What follows are functions that we’ve left up to you to implement!

# Specification
Complete the implementations of player, actions, result, winner, terminal, utility, and minimax.

* The player function should take a board state as input, and return which player’s turn it is (either X or O).
  * In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
  * Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).
