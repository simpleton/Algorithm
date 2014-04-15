import sys

def read_input():
   num = int(sys.stdin.readline().strip())
   Naomi = [float(x) for x in sys.stdin.readline().strip().split()]
   Ken = [float(x) for x in sys.stdin.readline().strip().split()]
   return sorted(Naomi), sorted(Ken)

def print_result(result, index):
   yield

def calc(Naomi, Ken):
   socore = 0
   j = 0
   for i in xrange(len(Naomi)):
      if j == len(Ken):
         break
      while j < len(Ken) and Naomi[i] > Ken[j]:
         j += 1
         socore += 1
      j += 1
   return socore

def deceitful_calc(Naomi, Ken):
   lose_socore = 0
   j = 0
   for i in xrange(len(Naomi)):
      if (Naomi[i] < Ken[j]):
         lose_socore += 1
         continue
      j += 1
   return len(Naomi) - lose_socore
         

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for r in xrange(T):
       Naomi, Ken = read_input()
       print "Case #%d: %d %d" % (r+1,deceitful_calc(Naomi, Ken), calc(Naomi, Ken))
