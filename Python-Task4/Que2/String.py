def middleCharacter(string,length):
    middle=''
    if(length%2!=0):
        middle=string[length // 2]
    else:
        middle=string[(length-1) // 2]+string[length // 2]
    return(middle)
def length(string):
    length=0
    for i in string:
        length+=1
    return(length)
def vowels(string):
    count=0
    for i in string:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            count+=1
    return(count)
def words(string):
    word=1
    for i in string:
        if(i==" " or i=="," or i=="\t" or i=="\n"):
            word+=1
    return(word)
            
