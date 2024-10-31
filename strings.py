myString = "My name is Python"
# string methods

# len function is used to get length of string
print(len(myString))
# upper, it converts string to uppercase
print(myString.upper())
# lower, it converts string to lowercase
print(myString.lower())
# rstring, it removes the trailing characters
print("python!!!!".rstrip("!"))
# replace, it replaces target string with given string
print("My name is Python".replace("Python", "Hashir"))
# split, it splits string based upon given string and returns an array
print(myString.split(" "))
# capitalize, it capitalizes the first letter of string
print("hello".capitalize())
# count, it counts the instances of target string
print("color is green and color is blue".count("color"))
# endswith, it tells if string ends with specific substring
print(myString.endswith("hon"))
# find, it finds and tells the index of given string
print(myString.find("name"))
# isalnum, it tells if string consists of A-Z, a-z and 0-9 only
print("Az01U?".isalnum())
# islower, it tells if string consists of all lower case characters
print(myString.islower())
# swapcase, it converts lowercase characters to uppercase and uppercase characters to lowercase
print("Pink RiBbOn".swapcase())
