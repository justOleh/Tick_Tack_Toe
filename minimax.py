huPlayer = "X"

aiPlayer = "O"


def emptyIndexies(board):
    return [x for x in board if isinstance(x,int)]


def winning(board, player):
    if (
            (board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player)):
        return True
    else:
        return False


def minimax(new_board, player):
    avail_spots = emptyIndexies(new_board)

    if winning(new_board, huPlayer):
        return {"score": -10}

    elif (winning(new_board, aiPlayer)):
        return {"score": 10}

    elif (len(avail_spots) == 0):
        return {"score": 0}

    moves = [];

    # loop through available spots
    for i in avail_spots:
        move = {}

        move['index'] = new_board[i]

        # set the empty spot to the current player
        new_board[i] = player;

        # collect the score resulted from calling minimax
        # on the opponent of the current player
        if player == aiPlayer:
            result = minimax(new_board, huPlayer)
            move['score'] = result['score']

        else:
            result = minimax(new_board, aiPlayer)
            move['score'] = result['score']

            # reset the spot to empty
        new_board[i] = move['index']

        # push the object to the array
        moves.append(move)

        bestMove = 0

        if player == aiPlayer:
            global bestScore
            bestScore = -10000
            for  i in range(len(moves)):
                if moves[i]['score'] > bestScore:
                    bestScore = moves[i]['score']
                    bestMove = i
        else:
            global bestScore2
            bestScore2 = 10000
            for  i in range(len(moves)):
                if (moves[i]['score'] < bestScore2):
                    bestScore2 = moves[i]['score'];
                    bestMove = i;

    return moves[bestMove]
