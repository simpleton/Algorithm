import sys
import math

def check_palind(n):

    if (str(n) == str(n)[::-1]):
        return True
    else:
        return False

def check_square(n):
    tmp = int(math.sqrt(n))
    if (tmp * tmp == n and check_palind(tmp)):
        return True
    else:
        return False
    
if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    
    for r in xrange(T):
        A, B = map (int, sys.stdin.readline().strip().split(' '))
        result = 0
        for x in xrange(A,B+1):
            if (check_palind(x) and check_square(x)):
                result = result + 1
        print "Case #%d: %s" % (r + 1, result)
