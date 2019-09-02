
def get_board(numbers=[0, 1, 2], rows=3):
    board = [numbers for _ in range(rows)]
    return board

def validate_board(board):
    if not (all(len(x)==3 for x in board) and len(board) == 3):
        return False

    d = {0:0, 1:0, 2:0}
    for i in board:
        for k in i:
            if not (k in [0, 1, 2]):
                return False
            d[k] = d[k] + 1
    if not(d[1] == d[2] or d[1] == (d[2] + 1)):
        return False
    return True

def game_finished(board):
    x, y, z = board

    if any((len(x)<3, len(y)<3, len(z)<3)):
        return False
    if board == [[0,0,0], [0,0,0], [0,0,0]]:
        return False

    if (x[0]==y[1]==z[2]) and x[0]!=0 :
        return x[0]
    if (z[0]==y[1]==x[2]) and z[0]!=0:
        return z[0]
    if x.count(1) == 3 or y.count(1) == 3 or z.count(1) == 3:
        return 1
    elif x.count(2) == 3 or y.count(2) == 3 or z.count(2) == 3:
        return 2

    for i in range(3):
       if [x[i], y[i], z[i]].count(1) == 3:
           return 1
       if [x[i], y[i], z[i]].count(2) == 3:
           return 2

    if (0 in x)  or (0 in y) or (0 in z):
        return 0
    return -1


def render_board(board):
    if not(len(board)==3) or (not all([len(i)==3 for i in board])):
        return False
    d = {1: 'X', 2: 'O', 0: '&nbsp;'}
    res = ''
    for i in range(3):
        res = res + '<tr>'
        for k in range(3):
            res = res + '<td>' + d.get(board[i][k], 'error') + '</td>'
        res = res + '</tr>'
    res = '<table>' + res + '</table>'
    if 'error' in res:
        return False
    return res
