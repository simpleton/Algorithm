import string 




if __name__ == "__main__":
    f = open("./data/p13","r")
    tmp = f.read()
    
    list =  tmp.split()
    sum = 0
    for i in list:
        sum = sum + int(i[:12])
    print sum
        
    
