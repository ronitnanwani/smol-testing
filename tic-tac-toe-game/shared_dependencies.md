the app is: Tic-Tac-Toe game of Human vs Computer

the files we have decided to generate are: gameboard.html, gameboard.css, gameboard.js, computerplayer.js, humanplayer.js, script.js, server.py, database.sql

Shared dependencies:

1. Exported variables:
   - gameBoardState
   - currentPlayer
   - humanScore
   - computerScore

2. Data schemas:
   - leaderboard (id, human_wins, computer_wins)

3. ID names of DOM elements:
   - gameboard
   - cell-{row}-{column} (for each cell in the gameboard)
   - human-score
   - computer-score
   - game-status
   - restart-button

4. Message names:
   - GPT-4 API request and response for computer move

5. Function names:
   - makeMove
   - checkWinner
   - checkTie
   - computerMove
   - humanMove
   - updateLeaderboard
   - restartGame