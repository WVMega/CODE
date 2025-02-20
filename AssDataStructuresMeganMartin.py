#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# This is a program to demonstrate working with different data types.#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

myTuple = tuple(["Echo","Higgs","Andrew","Rolf","Sena","Vince","Moore","Maya","Sunny","Will"]) # initiates the original tuple. 
print("The Tuple in original order: \n", myTuple) # Prints the original tuple.
reverseTuple = myTuple[::-1] # Creates a new tuple in reverse order. 
print("The Tuple in reverse order: \n", reverseTuple) # Prints the tuple with reverse order.
print("The third name listed in the original tuple is:\n", myTuple[2]) # Prints the third value in the tuple at index 2.

randomOrderSet = set(myTuple) # Converts the tuple into a set which is unordered to randomize the data.
randomOrderTuple = tuple(randomOrderSet) # Converts the set back into a tuple so that it is immutable.
print("The Tuple in random order: \n",randomOrderTuple) # Prints the randomized tuple.

newName = tuple(["Frank"]) # Creates a new tuple which can be added to the original.
combinedTuple = myTuple + newName # Appends newName to the end of myTuple.
print("The Tuple plus the name Frank \n",combinedTuple) # Prints the new combined tuple.

namesList = list(combinedTuple) # Creates a new list version of the tuple with the addition.
namesList.pop(0) # Removes the first value in the list at index 0.
newNamesTuple = tuple(namesList) # Converts the list back to a tuple so that it is immutable.
print("The original Tuple minus the name Echo:\n",newNamesTuple) # Prints the newest version of the tuple.

myList = ["Echo","Higgs","Andrew","Rolf","Sena","Vince","Moore","Maya","Sunny","Will"] # Initiates the original list.
print("The original List is: \n",myList) # Prints original list.
reverseList = myList[::-1] # Creates a new list in reverse order of the original.
print("The reversed List is: \n", reverseList) # Prints the reversed list.

print("The third value in the list is: \n",myList[2]) # Prints the third value in the list at index 2.

myListSet = set(myList) # Creates an unordered set from the original list.
myListRandom = list(myListSet) # Converts the set back into a list.
print("The original list in random order: \n", myListRandom) # Prints the original list in random order.

myList.append("Frank") # Appends the name Frank to the end of the original list.
print("The original list plus Frank: \n", myList) # Prints the original list + Frank.

myList.pop(0) # Removes the first value of the list at index 0.
print("The updated list minus Echo \n", myList) # Prints the new list minus the name Echo.