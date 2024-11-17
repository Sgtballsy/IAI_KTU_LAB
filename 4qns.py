col, posDiag, negDiag = [],[],[]
board = [['.']*4 for i in range(4)]

def bt(r):
    if r == 4:
        return True
    for c in range(4):
        if c in col or (r+c) in posDiag or (r-c) in negDiag:
            continue
        col.append(c)
        posDiag.append(r+c)
        negDiag.append(r-c)
        board[r][c] = 'Q'
        if bt(r+1):
            return True
        col.remove(c)
        posDiag.remove(r+c)
        negDiag.remove(r-c)
        board[r][c] = '.'
bt(0)
print("----------------------")
for i in board:
    for j in i:
        print(' | ',j,end='')
    print(' | ')
print("----------------------")