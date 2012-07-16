

if __name__=="__main__":
    sum = 1
    for i in range(0,1000):
        sum *= 2
    str_sum = str(sum)
    result_sum = 0
    for i in range(0,len(str(sum))):
        result_sum += int(str_sum[i])
    print result_sum
