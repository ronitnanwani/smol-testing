from flask import Flask, render_template, request, jsonify,json
# from gameboard import GameBoard
# from computer_player import computerMove
# from human_player import human_move
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/make_move', methods=['POST'])
# def make_move():
#     data = request.get_json()
#     row = data['row']
#     col = data['col']
#     player = data['player']
#     game_board = GameBoard()
#     game_board.make_move(row, col, player)
#     return jsonify(game_board.check_winner())

@app.route('/computer_move', methods=['GET','POST'])
def computer_move():
    # print("Reached")
    requestt=json.loads(request.data)
    game_board=requestt['gameBoardState']
    print(game_board)
    # game_board = GameBoard()
    # computer_player = ComputerPlayer(game_board)
    # move = computer_player.computer_move()
    return ({"row":1,"column":2})

# @app.route('/update_leaderboard', methods=['POST'])
# def update_leaderboard():
#     data = request.get_json()
#     winner = data['winner']
#     conn = sqlite3.connect('leaderboard.db')
#     cursor = conn.cursor()
#     if winner == 'human':
#         cursor.execute("UPDATE leaderboard SET human_wins = human_wins + 1 WHERE id = 1")
#     elif winner == 'computer':
#         cursor.execute("UPDATE leaderboard SET computer_wins = computer_wins + 1 WHERE id = 1")
#     conn.commit()
#     conn.close()
#     return jsonify({'status': 'success'})

# @app.route('/get_leaderboard', methods=['GET'])
# def get_leaderboard():
#     conn = sqlite3.connect('leaderboard.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT human_wins, computer_wins FROM leaderboard WHERE id = 1")
#     result = cursor.fetchone()
#     conn.close()
#     return jsonify({'human_wins': result[0], 'computer_wins': result[1]})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)