import sys
import copy
MAX_LIMIT = 4

def read_input():
    first_row = int(sys.stdin.readline().strip())
    map_before = []
    for n in xrange(MAX_LIMIT):
        map_before.append(sys.stdin.readline().strip().split())
    second_row = int(sys.stdin.readline().strip())
    map_after = []
    for n in xrange(MAX_LIMIT):
        map_after.append(sys.stdin.readline().strip().split())
    return first_row-1, map_before, second_row-1, map_after
       
def print_result(result, index):
    if len(result) > 1:
        print "Case #%d: Bad magician!" % (index + 1)
    elif len(result) == 0:
        print "Case #%d: Volunteer cheated!" % (index + 1)
    else:
        print "Case #%d: %s" % (index+1, result.pop())
if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for r in xrange(T):
       first_row, map_before, second_row, map_after = read_input()
       result = set(map_before[first_row]) & set(map_after[second_row])
       print_result(result, r)
       
        


    
