#Tuple methods
tuple=('a','e','i','o','u','a')
print(tuple)

#count method is use to count no of times element appears
count=tuple.count('a')
print("count of a is =",count)

#index method is use to give inex of an element in tuple
index=tuple.index('o')
print("index of o is=",index)

#len method gives the count of number of object in tuple
length=len(tuple)
print("length=",length)

#ascii method escapes the non ascii characters in string
text='Hello W#orld'
print(ascii(text))

#sort method is use to sort the elements in specific order
print("sorted order=",sorted(tuple))

#slice metohd
sliceTuple=slice(3)
print(tuple[sliceTuple])

#enumerate method 
enumerateElements=enumerate(tuple)
print(list(enumerateElements))
