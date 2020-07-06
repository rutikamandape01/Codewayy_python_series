A=[]
row=int(input("Enter the size of matrix"))
col=int(input("Enter the size of matrix"))
print("Enter the elements is matrix")
for i in range(row):
    a=[]
    for j in range(col):
        a.append(int(input()))
    A.append(a)
for i in range(row):
    for j in range(col):
        print(A[i][j],end=" ")
    print()
print()

for i in range(row):
    for j in range(col):
        if(A[i][j]>1):
           for k in range (2,A[i][j]):
               if((A[i][j]%k) == 0):
                  break
           else:
               print(A[i][j])
                 
                 
   
    
