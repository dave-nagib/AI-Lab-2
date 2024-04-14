## Overview
Connect 4 is a two-player game in which the players first choose a color and then take turns. dropping their colored discs from the top into a grid. The pieces fall straight down, occupying. the next available space within the column. The objective of the game is to connect-four of one’s own discs of the same color next to each other vertically, horizontally, or diagonally. The two players keep playing until the board is full. The winner in this version of the game is the player having greater number of connected fours.

## Algorithm
The AI player is implemented using the Minimax & Minimax with pruning algorithms which traverse the game K steps ahead, maximizing/minimizing the reward (objective function) under the assumption that the opponent is playing optimally and picking the next move with highest reward. Since the minimax tree grows exponentially big in size as depth can reach 6*7 = 42, we use a heuristic of the actual utility function after depth = k, which is a user-determined parameter.

## Heuristic
We store chains of 2, 3, and 4 for each player in a list and keep track of it in the game state object. The chain count is updated on each move such that we account for proponent chains that grew (smaller chains replaced by bigger chains) and subtract the opponent's chains that have been blocked off to value defensiveness as well.
The heuristic is desgined such as it equals the `weighted sum of chains built by player 1 - weighted sum of chains built by player 2` (assuming player 1 is a maximizer and player 2 is a minimzer), where longer chains mean greater weight.

## Project Report
The detailed report of the project can be found included in the repository [here](https://github.com/dave-nagib/AI-Lab-2/blob/e9df07af189b716e9b28cd0016846f94d0f88616/Ai_lab_2_report_final.pdf).
