
board = [[0 for x in range(0,3)] for x in range(0,3)]
players = ["X", "O"]

def game(answer,player):

    while True:
        if board[int(answer[0]) - 1][int(answer[1]) - 1] == 0:
            board[int(answer[0]) - 1][int(answer[1]) - 1] = "{}".format(player)
            break
        else:
            print "PlaceHolder taken"
            answer = getAnswer(player)


def getAnswer(player):
    answer = raw_input("Cordinates for player {}".format(player))
    answer = answer.split(",")
    return answer


while True:
    for player in players:
        print board
        game(getAnswer(player),player)













