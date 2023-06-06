import os
import requests
from gameboard import make_move

def computerMove(gameBoardState):
    print(gameBoardState)
    print("Hello World")
    api_key = os.getenv("OPENAI_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": f"Given the Tic-Tac-Toe game board state: {gameBoardState}, what is the best possible move for you can play. You are 'O' and the opponent is 'X'?",
        "max_tokens": 50,
        "n": 1,
        "stop": None,
        "temperature": 0.5
    }
    response = requests.post("https://api.openai.com/v1/engines/davinci-codex/completions", headers=headers, json=data)
    response_json = response.json()
    best_move = response_json["choices"][0]["text"].strip()

    row, column = map(int, best_move.split(','))
    make_move(gameBoardState, row, column, "O")

    return row, column