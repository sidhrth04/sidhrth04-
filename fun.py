"""
comment
"""
#print("Hello world")

#declaring variables

x = 5
y = "john"


"""
Casting:
If i want to specify the data type of a variable

x = str(3)
y = int(3)

to get the type of the variable
print(type(x))

multiple values assign 
x, y, z = 1, 2, 3
"""
#To create a global variable inside a function, you can use the global keyword.

"""
Built in Datatypes in Python

-Text Type:	str
-Numeric Types:	int, float, complex
-Sequence Types:	list, tuple, range
-Mapping Type:	dict
-Set Types:	set, frozenset
-Boolean Type:	bool
-Binary Types:	bytes, bytearray, memoryview
-None Type:	NoneType

"""

# List : x =["apple", "Banana", "Cherry"]
# tuple : x = ("apple", "Banana", "Cherry")

#Strings
"""
1.To get the length of a string, use the len() function.
2.To check if a certain phrase or character is present in a string, we can use the keyword in.
"""

#Slicing Strings

"""
-Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])

-Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])

-Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])
"""

#Modify Strings
"""
-The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())

-The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())

- strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

--Create an f-string:

age = 36
txt = f"My name is John, I am {age}"
print(txt)
"""

#List
"""
Lists are used to store multiple items in a single variable.

When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

List items can be of any data type:

A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]

Negative Indexing
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.

Example
Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


To append elements from another list to the current list, use the extend() method.
"""

#Tuples

"""
mytuple = ("apple", "banana", "cherry")
Tuples are used to store multiple items in a single variable.

Tuple ka order unchangeable hai

Tuples can have items with same value
"""


"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
"""
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

Example
Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
"""
#Set

"""
Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

To add items from another set into the current set, use the update() method.

Example
Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


To remove an item in a set, use the remove(), or the discard() method.

You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
.clear() //empties the set
del




There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""

#Dictionary

"""
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
x = thisdict.get("model")
x = thisdict.keys()
x = thisdict.values()
x = thisdict.items()
thisdict.update({"year": 2020})
The pop() method removes the item with the specified key name:
The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
The del keyword removes the item with the specified key name
The clear() method empties the dictionary

clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

"""

#Lambda Function

"""
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

"""
