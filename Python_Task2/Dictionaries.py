#dictionaries methods

#get method gives the value of the specific item
dict1={"name":"Rutika","Age":"20","city":"Nagpur","state":"Maharashtra"}
print(dict1.get("name"))

#item method
items=dict1.items()
print(items)

#value method use to give all values in the dictionary
values=dict1.values()
print(values)

#pop method used to remove specific item from dictionary
pop=dict1.pop("Age")
print(dict1)

#popitem method use to remove last item from dictionary
popItem=dict1.popitem()
print(dict1)

#update method is use to add item into dictionary
updateDict=dict1.update({"country" : "India"})
print(dict1)

#clear method
clearDict=dict1.clear()
print(dict1)

 
