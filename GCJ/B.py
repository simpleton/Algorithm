import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    
    for r in xrange(T):
        x,y = sys.stdin.readline().strip().split(' ')
        x = int(x)
        y = int(y)

        mmap = [([0] * (int(y))) for i in xrange(int(x))]
        for row in xrange(x):
            mmap[row] = map(int ,sys.stdin.readline().strip().split(' '))
            
        column_max = [0] * y;
        row_max = [0] * x;
        for row in xrange(x):
            for column in xrange(y):
                if (mmap[row][column] > column_max[column]):
                    column_max[column] = mmap[row][column]
                if (mmap[row][column] > row_max[row]):
                    row_max[row] = mmap[row][column]
        result = "YES"
        for row in xrange(x):
            for column in xrange(y):
                if (mmap[row][column] < min(row_max[row], column_max[column])):
                    result = "NO"

        print "Case #%d: %s" % (r + 1, result)
