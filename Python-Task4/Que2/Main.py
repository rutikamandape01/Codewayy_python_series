import functions
import String
import Operator
num=int(input("Enter the number"))
list1=[]

length=int(input("Enter the no. of elements in list1"))
for i in range (0,length):
             element=int(input("Enter elements in list"))
             list1.append(element)

square=functions.squareFunction(num)
print("square is ",square)

maximum=functions.maximumNum(list1,length)
print("maximum element is ",maximum)

minimum=functions.minimumNum(list1,length)
print("Minimum element is ",minimum)

Sum=functions.listSum(list1,length)
print("sum of elements is ",Sum)

print()

string1=input("Enter the string")
length=String.length(string1)
print("Length of string is",length)
print()

middle=String.middleCharacter(string1,length)
print(middle)
print()

vowelsCount=String.vowels(string1)
print(vowelsCount)
print()

words=String.words(string1)
print(words)
print()

num1=int(input("Enter the num1:"))
num2=int(input("Enter the num2:"))
sum=Operator.andOperator(num1,num2)
print(sum)

mul=Operator.orOperator(num1,num2)
print(mul)

sub=Operator.notOperator(num1,num2)
print(sub)







