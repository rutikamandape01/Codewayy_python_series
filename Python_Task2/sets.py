#set methods

colors={'pink','orange','green'}
print(colors)

#add method use to add elements in the set
colors.add('red')
print(colors)

#copy method use to copy the set into another
copyColors=colors.copy()
print(copyColors)

#difference method shows the different element between sets
myColors={'pink','black'}
difference=myColors.difference(colors)
print(difference)

#intersection method shows similarity betn sets
similarColors=myColors.intersection(colors)
print(similarColors)

#union method combines the two sets
unionColors=myColors.union(colors)
print(unionColors)

#remove method use to remove specific element from set
removeColor=colors.remove('green')
print(colors)

#clear method use to remove all the elements from set
clearColors=colors.clear()
print(colors)
