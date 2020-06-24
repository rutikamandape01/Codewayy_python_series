#list methods
numbers=[3,5,7,21]
print(numbers)

#append method is used to add element into list
numbers.append(23)
print(numbers)

#insert method inserts element into list at particular location
numbers.insert(0,1)
print(numbers)

#sum method calculates sum of all elements in list
print("sum of numbers in list is=",sum(numbers))

#count method count total occurrence of given element
print("count=",numbers.count(3))

#min mthod calculate minimum of all the elements in list
print("Minimum=",min(numbers))

#max method calcualte maximum of all the elements in list
print("maximum=",max(numbers))

#del  method delete element at particular location
del numbers[2]
print(numbers)

#slicing
temp=numbers[0:3]
print(temp)

