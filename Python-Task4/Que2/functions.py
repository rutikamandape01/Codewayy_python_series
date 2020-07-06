def squareFunction(num):
    sq=num*num
    return(sq)
def maximumNum(list1,length):
    maximum=list1[0]
    for i in range (1,length):
        if(list1[i]>maximum):
            maximum=list1[i]
    return(maximum)
def minimumNum(list1,length):
    minimum=list1[0]
    for i in range (1,length):
        if(list1[i]<minimum):
            minimum=list1[i]
    return(minimum)
def listSum(list1,length):
    Sum=0;
    for i in range (0,length):
        Sum=Sum+list1[i]
    return(Sum)
