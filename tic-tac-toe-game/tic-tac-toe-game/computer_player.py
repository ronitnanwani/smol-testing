import os
import requests

def computerMove(gameBoardState):
    print(gameBoardState)
    api_key = os.getenv("OPENAI_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "messages": [
        {"role": "system", "content": "You are a professional at playing Tic-Tac-Toe."},
        {"role": "user", "content": f"Given the three rows of the Tic-Tac-Toe game board: {gameBoardState}, what is the best possible move you can play? You are 'computer' and the opponent is 'human'. Best possible move is defined as the one which increases your chances of winning in the consequent steps while simultaneously not allowing the opponent to win. The row numbers and column numbers are based on zero-indexing. You can play a move only if the cell you select in the game board is not filled previously. Work through the explanantion of selecting the best possible move in less than 100 words. End your answer with the line 'Hence the best possible move is (<row number> , <column number>)."}
        ],
        "model":"gpt-4",
        "max_tokens": 200,
        "n": 1,
        "stop": None,
        "temperature": 0.5
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    response_json = response.json()
    print(response_json)
    best_move = response_json["choices"][0]["message"]["content"]
    n=len(best_move)
    ptr=n-1
    while(best_move[ptr] != ')'):
        ptr-=1
    r=ptr
    ptr-=1
    while(best_move[ptr] != '('):
        ptr-=1
    l=ptr
    bestmove = best_move[l+1:r]
    bestmove=bestmove.split(',')
    row=int(bestmove[0].strip())
    column=int(bestmove[1].strip())
    return (row,column)