

game = [[2,2,1],[0,2,0],[0,0,1]]
players = [1, 2]


def check(list, player):
    if list.count(player) == 3:
        return True
    else:
        return False


for x in game:
    for player in players:
        if check(x,player):
            print "player {} won".format(player)

for b in range(0,len(game)):
    list = []

    list.append(game[0][b])
    list.append(game[1][b])
    list.append(game[2][b])
    for player in players:
        if check(list, player):
            print "player {} won".format(player)











