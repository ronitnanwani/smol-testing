from gameboard import GameBoard, makeMove, checkWinner, checkTie
from computer_player import ComputerPlayer, computerMove
from human_player import HumanPlayer, humanMove
import sqlite3

def updateLeaderboard(human_wins, computer_wins):
    conn = sqlite3.connect('leaderboard.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO leaderboard (human_wins, computer_wins) VALUES (?, ?)", (human_wins, computer_wins))
    conn.commit()
    conn.close()

def restartGame():
    game_board = GameBoard()
    current_player = HumanPlayer()
    game_status = "Your Turn"

def game_logic():
    game_board = GameBoard()
    current_player = HumanPlayer()
    game_status = "Your Turn"

    while not checkWinner(game_board) and not checkTie(game_board):
        if isinstance(current_player, HumanPlayer):
            move = humanMove()
            makeMove(game_board, move, current_player)
            if checkWinner(game_board):
                game_status = "You Won!"
                updateLeaderboard(1, 0)
            elif checkTie(game_board):
                game_status = "Tie Game!"
                updateLeaderboard(0, 0)
            else:
                current_player = ComputerPlayer()
                game_status = "Computer Turn"
        else:
            move = computerMove(game_board)
            makeMove(game_board, move, current_player)
            if checkWinner(game_board):
                game_status = "Computer Won!"
                updateLeaderboard(0, 1)
            elif checkTie(game_board):
                game_status = "Tie Game!"
                updateLeaderboard(0, 0)
            else:
                current_player = HumanPlayer()
                game_status = "Your Turn"

if __name__ == "__main__":
    game_logic()