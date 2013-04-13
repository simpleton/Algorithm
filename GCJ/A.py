import sys
import copy

MAX_LIMIT = 4
def calc(data):
    complete = False;
    cdata = copy.copy(data)

    for x in xrange(MAX_LIMIT):
        data[x] = data[x].replace("T", "X")
        if (data[x] == "XXXX"):
            return "X won"
          
        if (data[0][x] == 'X' and data[1][x] == 'X' \
                and data[2][x] == 'X' and data[3][x] == 'X') :
            return "X won"

        cdata[x] = cdata[x].replace("T", "O")
        if (data[x] == "OOOO"):
            return "O won"
        if (cdata[0][x] == 'O' and cdata[1][x] == 'O' and  \
                cdata[2][x] == 'O' and cdata[3][x] == 'O'):
            return "O won"
        for y in xrange(MAX_LIMIT):
            if (cdata[x][y] == '.'):
                complete = True;

    if (data[0][0] == 'X' and data[1][1] == 'X' and \
            data[2][2] == 'X' and data[3][3] == 'X'):
        return "X won"
    if (data[3][0] == 'X' and data[2][1] == 'X' and \
            data[1][2] == 'X' and data[0][3] == 'X'):
        return "X won"

    if (cdata[0][0] == 'O' and cdata[1][1] == 'O' and \
            cdata[2][2] == 'O' and cdata[3][3] == 'O'):
        return "O won"
    if (cdata[3][0] == 'O' and cdata[2][1] == 'O' and \
            cdata[1][2] == 'O' and cdata[0][3] == 'O'):
        return "O won"

    if (complete):
        return "Game has not completed"
    else:
        return "Draw"
    
if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    map = [([0] * (MAX_LIMIT)) for i in xrange(T)]

    for r in xrange(T):
        for n in xrange(MAX_LIMIT):
            map[r][n] = str(sys.stdin.readline().strip())
        sys.stdin.readline().strip()

        result = calc(map[r])
        print "Case #%d: %s" % (r + 1, result)


    
