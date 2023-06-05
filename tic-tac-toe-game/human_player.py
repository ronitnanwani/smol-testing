def human_move(game_board_state, row, column):
    if game_board_state[row][column] == "":
        game_board_state[row][column] = "X"
        return True
    else:
        return False