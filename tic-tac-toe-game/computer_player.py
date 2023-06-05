import os
import requests
from gameboard import makeMove

def computerMove(gameBoardState):
    api_key = os.getenv("GPT_4_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": f"Given the Tic-Tac-Toe game board state: {gameBoardState}, what is the best possible move for the computer?",
        "max_tokens": 50,
        "n": 1,
        "stop": None,
        "temperature": 0.5
    }
    response = requests.post("https://api.openai.com/v1/engines/davinci-codex/completions", headers=headers, json=data)
    response_json = response.json()
    best_move = response_json["choices"][0]["text"].strip()

    row, column = map(int, best_move.split(','))
    makeMove(gameBoardState, row, column, "O")

    return row, column