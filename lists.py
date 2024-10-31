myList = [1, 2, 3, 4, "tiger", "cow", True, "lion", ["kite", 91]]

# in, it tells if an element exists in list
output = 4 in myList
output = "wolf" in myList
output = True in myList
output = ["kite", 91] in myList

# list comprehensions
# populating list with elements 0 - 15
output = [x for x in range(0, 15)]
# populating list with elements 0 - 20 even numbers
output = [x for x in range(0, 20) if x % 2 == 0]
# getting elements which starts with a only
tempList = ["cow", "apple", "pink", "zebra", "hen", "Air", "swim", "angle"]
output = [x for x in tempList if (x.startswith("a") or x.startswith("A"))]
# making list by incrementing each element by 10
output = [x + 10 for x in [1, 2, 3, 4, 5]]
# making list by taking square of each element
output = [x**2 for x in [1, 2, 3, 4]]
# making list by only including even numbers
output = [x for x in [1, 2, 3, 4, 5, 6] if x % 2 == 0]
# making list by adding 100 to even numbers and adding 10 to odd numbers
output = [x + 100 if x % 2 == 0 else x + 10 for x in [1, 2, 3, 4, 5, 6, 7]]

# list methods
# append, used for appending element at last of list
myList.append("last")
# sort, used for sorting list
myList = [23, 55, 1, 23, 12, 91, 44]
# sorting in desc order
myList.sort()
myList = ["kite", "ant", "hen", "apple"]
myList.sort(reverse=True)
# reverse, it reverses a list
myList = [1, 2, 3, 4, 5, 6]
myList.reverse()
# index, it returns index of first occurence of target element
myList = [1, 2, 3, 4, 5, 6]
output = myList.index(3)
# count, it tells count of element in list
myList = [1, 2, 3, 1, 1, 5]
output = myList.count(1)
# copy, creats deep copy of given list
output = myList.copy()
# insert, it inserts elements in provided index
myList = [1, 2, 3, 4, 5, 6]
myList.insert(1, 991)
# extend, it takes list as input and inserts its elements into target list
myList = [1, 2, 3, 4, 5, 6]
myList.extend([7, 8, 9])
# remove, it removes the target element
myList.remove(1)
# pop, it removes element at provided index
myList = [1, 2, 3, 4, 5, 6]
myList.pop(4)

# min and max, these gives min and max elements
output = min(myList)
myList = ["gate", "zebra", "king", "lion"]
output = max(myList)
# sum, it gives sum of all the list elements
myList = [1, 2, 3, 4, 5, 6]
output = sum(myList)
# any, it checks if any element satisfies the provided condition and returns boolean
myList = [1, 2, 3, 4, 5, 6]
output = any(i == 4 for i in myList)
# all, it checks if all elements satisfies the provided condition and returns boolean
output = all(i >= 1 for i in myList)
# filter, it returns a list of elements which satisfies provided condition, it must be wrapped in list() to get output in form of list
myList = [10, 16, 7, 79, 84, 96]
# filtering even elements
output = list(filter(lambda input: input % 2 == 0, myList))
# filtering elements which start with "P" or "p"
myList = ["Pakistan", "India", "22", "Parrot", "pipe", "Lion"]


def isStartingWithP(input):
    if input[0] == "P" or input[0] == "p":
        return True
    else:
        return False


output = list(filter(isStartingWithP, myList))

# map, it modifes the elements of list and returns a new list
myList = ["Pakistan", "India", "22", "Parrot", "pipe", "Lion"]
output = list(map(lambda input: input.upper(), myList))

myList = [1, 2, 3, 4, 5, 6]
# inserting multiple elements at target index
# [index1:index2], it grabs the slice of list from index1 to index2, (index2 excluded) and replaces it with provided elements
myList[0:0] = [101, 102]
myList[len(myList) : 0] = [551, 552]
myList[3:3] = [6651]
myList = [1, 2, 3, 4, 5, 6]
myList[1:4] = [99, 100]
