import string 

def get_max(a,b,c,d):
    if (b > a):
        a = b
    if (c > a):
        a = c
    if (d > a):
        a = d
    return a

def calc(list):
    mmax = 0
    for i in range(0,17):
        for j in range(0,17):
            tmp = 1
            tmp1 = 1
            tmp2 = 1
            for k in range(0,4):
                tmp *= int(list[i*20+j+k])
                tmp1 *= int(list[i*20+j+k*20])
                tmp2 *= int(list[i*20+j+k*20+k])
            mmax = get_max(mmax,tmp,tmp1,tmp2)
    for i in range (0,17):
        for j in range(3,20):
            tmp = 1
            for k in range(0,4):
                tmp *= int(list[i*20+j+k*20-k])
            print tmp      
            mmax = max(mmax, tmp)
    return mmax

if __name__ == "__main__":
    f = open("./data/p11.txt",'r')
    str = f.read()
    mlist =  str.split()
    print calc(mlist)
    
