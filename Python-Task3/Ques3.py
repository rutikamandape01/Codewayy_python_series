#printing numbers from 1 to 10 except 3 and 7 using for loop        
for number in range(1,11):
    if(number==3 or number==7):
        continue
    else:
        print(number)

#printing numbers from 1 to 10 except 3 and 7 using while loop        
num=1
while(num<11):
    if(num==3 or num==7):
        num+=1
    else:
        print(num)
        num+=1
        
