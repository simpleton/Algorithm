import string
if __name__ == "__main__":
    f = open("./data/p8.txt", 'r')
    str = f.read()
    num = []
    index = 0
    print str.strip("\n\r")
    for x in range(0,len(str)):

        if ((str[x]>='0') & (str[x]<='9')):
            num.append(str[x])
            index += 1


    m_max = 0
    for x in range(0,len(num)-4):
        tmp = 1
        for y in range (x,x+5):
            tmp *= int(num[y])
        if (m_max < tmp):
            m_max = tmp
            for y in range (x,x+5):
                print num[y]
            print "\n"

    print m_max
        
