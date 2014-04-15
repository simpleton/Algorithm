import sys
import copy
SPEED = 2.0

def read_input():
   C, F, X = sys.stdin.readline().strip().split()
   return float(C),float(F),float(X)
       
def print_result(result, index):
    print "Case #%d: %.7f" % (index+1, result)

def calc_min_time(C, F, X):
    curr_speed = SPEED
    before_time = 0
    after_time = 0
    delat = 0
    while before_time >= after_time:
        before_time = X / curr_speed + delat
        after_time = C / curr_speed + X/(curr_speed+F) + delat
        delat += C / curr_speed
        curr_speed += F
    return before_time

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for r in xrange(T):
        C, F, X = read_input()
        result = calc_min_time(C,F,X)
        print_result(result, r)
    
