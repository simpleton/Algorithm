from math import sqrt
def check(aNum):
    div = 0
    for i in range(1,int(sqrt(aNum))+1):
        if (aNum % i == 0):
            div += 1
    if (aNum == int(sqrt(aNum))* int(sqrt(aNum))):
        div = div * 2 - 1
    else:
        div *= 2
    return div


if __name__ == "__main__":
    
    index = 2
    m_sum = 1
    while (1):
        m_sum += index
        index += 1
        if (check(m_sum) > 500):
            break;
    print m_sum
