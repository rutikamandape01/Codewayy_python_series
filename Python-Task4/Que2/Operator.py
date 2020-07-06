def andOperator(num1,num2):
    if(num1>1 and num2<5):
        sum=num1+num2
        return(sum)
    else:
        return(0)

def orOperator(num1,num2):
    if(num1>1 or num2<5):
        mul=num1*num2
        return(mul)
    else:
        return(0)
def notOperator(num1,num2):
    if(not(num1>3 and num2<8)):
        sub=num1-num2
        return(sub)
    else:
        return(0)
