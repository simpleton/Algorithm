def calc(num_list,step,curr_max,index):
    """calc all the path value for find the max value"""
    if (index >= len(num_list)-15):
        return curr_max
    
    tmp = curr_max + num_list[index + step]
    
    max1 = calc(num_list, step+1, tmp ,index + step)
    
    tmp1 = curr_max + num_list[index + step + 1]
    
    max2 = calc(num_list, step+1, tmp1 ,index + step + 1)
    return max(max1, max2)
    
        
if __name__ == "__main__":
    f = open("data/P18","r")
    str = f.read()
    mlist = str.split()
    num_list = []
    for iter in mlist:
        num_list.append(int(iter))
    print (len(num_list))
    print calc(num_list, 1, num_list[0], 0)

