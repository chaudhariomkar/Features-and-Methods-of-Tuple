""""""
"""
Features of Tuple
Syntax ()
1.Tuple is an important data types in python
2.It has same features as that of list
3.While giving elements in a tuple use a comma(,) as a seprator
4.Tuple is immutable data types
    Mutable - Values can be updated 
    Immutable - Values cannot be updated
5.Accepts all types of Data 
    Homogenous - Can only store single type of data 
    Hetrogenous - Can store more than one type of data
6.Background Data Structure of Tuple is - ARRAY
6.Sequence order is preserved
7.Indexing (To Fetch Single Element) is Supported
    Positive Indexing - LEFT to RIGHT
    Negative Indexing - RIGHT to LEFT
8.Slicing (To Fetch Multiple Element or Substring in a sequence) is Supported
9.Duplicates are allowed.
10.There are few methods in tuple like .....
"""
#Create an empty tuple
a = ()  #Method 1
print(a)
b = tuple() #Method 2
print(b)
x = (1,2,3,4,5) #Elements in a tuple are seperated by comma's
print(len(x)) #Checks total numbers of elements in a tuple
#Indexing - to fetch single element
print(x[0])  #(positive - left to right)
print(x[-1]) #(negative - right to left)
#Slicing - to fetch multiple elements
print(x[1:3])
#Only 2 Methods in Tuple
#1.Count - Counts the number of occurence of a specific element
t = (10,20,30,40,50,50,60,50)
print(t.count(50)) #If element not present (Output = 0)
#2.Index - Finds the first occurence of a specified element and return its index
print(t.index(50)) #If element not present (Value Error)
#------------------------------
#Packing & Unpacking
y = 1,2,3 #Comma Seperated value are tuple
print(y)
print(type(y))
#Packing - Collecting multiple values in single object
#Unpacking - Seperate combined elements into individual entities
print(y)
a,b,c = y #Unpacking (Ungroup) - Seperate grouped element
print(a)
print(b)
print(c)
y = a,b,c #Packing (Group) - Combine ungrouped element
print(y)

#How to Swap values
c = 10
d = 20
print(c)
print(d)
d,c = c,d #Swapped values
print(c)
print(d)

