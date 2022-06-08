

## Learning py

## Lists

## string type list
mylist = ["apple","banana","cherry"]
print(mylist)
## index print
mylist = ["apple","banana","cherry"]
print(mylist[0])
print(mylist[2])
## index print
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
print(mylist[1:3])
## index print
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
print(mylist[:3])
## index print
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
print(mylist[3:])
## -index print
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
print(mylist[-5:-3])
## index print
mylist = ["apple","banana","cherry"]
print(mylist[0])
print(mylist[-2])

## search string
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
if "apple" in mylist:
    print("Yes,this 'apple' in list")
## search string in list 
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
if "apple" in mylist:
    print("Yes,this 'apple' in list")

## lenght
mylist = ["apple","banana","cherry"]
print(len(mylist))
## type
mylist = ["apple","banana","cherry"]
print(type(mylist))
## types of list
list1 = ["string1","string2","string3"]
list2 = [1,2,3]
list3 = [True,False,False]
## more types
list1 = ["string1",1,True,33,"bogdan"]

## list constructor 
mylist = list(("string1","string2","string3"))
print(mylist)
## edit list
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
mylist[1] = "banana1"
print(mylist) 
## edit range lists elements
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
mylist[1:3] = ["minions","hubabuba"]
print(mylist) 
## edit range and add more new 
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
mylist[1:2] = ["minions","hubabuba"]
print(mylist) 
## delete element in range 
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
mylist[1:3] = ["hubabuba"]
print(mylist) 
## insert new element with index
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
mylist.insert(2,"coca-cola")
print(mylist) 
## add element to end of list
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
mylist.append("coca-cola")
print(mylist) 
## add in 1 list + 1 list
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
mylist1 = ["go","run","fast"]
mylist.extend(mylist1)
print(mylist) 
## remove elements
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
mylist.remove("banana")
print(mylist) 
## remove elements with index
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
mylist.pop(1)
print(mylist) 
## remove last element of list index 
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
mylist.pop()
print(mylist) 
## delete element list with index  
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
del mylist[0]
print(mylist) 
## delete list
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
del mylist
print(mylist) 
## clear list
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
mylist.clear()
print(mylist) 

## elements of list in cycle
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
for x in mylist:
    print(x) 
## cycle with numbers of index
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
for i in range(len(mylist)):
    print(mylist[i]) 
## use while
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1 
## list comrehension
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
[print(x) for x in mylist] 
## list comrehension - cycle with new elements old list at "b"
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
newlist = []
for x in mylist:
    if "b" in x:
        newlist.append(x)
print(newlist) 
## list comrehension - cycle with new elements old list at "a"
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
newlist = [x for x in mylist if "b" in x]
print(newlist)
## condition of filter elements
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
newlist = [x for x in mylist if x != "apple"]
print(newlist)
## without if
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
newlist = [x for x in mylist]
print(newlist)
## range function for iteration
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
newlist = [x for x in range(5)]
print(newlist)
## range function of iteration x < ...
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
newlist = [x for x in range(5) if x < 2]
print(newlist)
## expression - add upper register at all elements in list
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
newlist = [x.upper() for x in mylist]
print(newlist)
## add "hello" for all elements in list
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
newlist = ["hello" for x in mylist]
print(newlist)
## back "orange" without "banana"
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
newlist = [x if x != "banana" else "orange" for x in mylist]
print(newlist)

## sort list with register
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
mylist.sort()
print(mylist)
## sort list with numbers
mylist = [10,20,33,22,1,2,4,3]
mylist.sort()
print(mylist)
## sort descending
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
mylist.sort(reverse = True)
print(mylist)
## sort descending
mylist = [10,20,33,22,1,2,4,3]
mylist.sort(reverse = True)
print(mylist)
## customize sort function
def sortfunc(n):
    return abs(n - 20)
mylist = [10,20,33,22,1,2,4,3]
mylist.sort(key = sortfunc)
print(mylist)
## sort with register
mylist = ["Apple","banana","cherry","Orange","Kiwi","mango"]
mylist.sort()
print(mylist)
## sort without register
mylist = ["Apple","banana","cherry","Orange","Kiwi","mango"]
mylist.sort(key = str.lower)
print(mylist)
# revers sort without register
mylist = ["Apple","banana","cherry","Orange","Kiwi","mango"]
mylist.reverse()
print(mylist)

## copy lists
mylist = ["Apple","banana","cherry","Orange","Kiwi","mango"]
newlist = mylist.copy()
print(newlist)
print(mylist)
## copy lists
mylist = ["Apple","banana","cherry","Orange","Kiwi","mango"]
newlist = list(mylist)
print(newlist)
print(mylist)

## join two lists
mylist = ["Apple","banana","cherry","Orange","Kiwi","mango"]
mylist1 = [1,2,3,4,66,77]
newlist = mylist + mylist1
print(newlist)
## join two lists in one of joined
mylist = ["Apple","banana","cherry","Orange","Kiwi","mango"]
mylist1 = [1,2,3,4,66,77]
for x in mylist1:
    mylist.append(x)
print(mylist)
## extend method
mylist = ["Apple","banana","cherry","Orange","Kiwi","mango"]
mylist1 = [1,2,3,4,66,77]
mylist1.extend(mylist)
print(mylist1)

## methods
# append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list 


# Tuples

## tuple
mytuple = ("Apple","banana","cherry","Orange","Kiwi","mango")
print(mytuple)
## tuple lenghth
mytuple = ("Apple","banana","cherry","Orange","Kiwi","mango")
print(len(mytuple))
## create tuple with one element
mytuple = ("Apple",)
print(type(mytuple))
## tuple types: string, integer,boolean
mytuple1 = ("1","2","3")
mytuple2 = (1,2,3)
mytuple3 = (True, False, False)
print(mytuple1)
print(mytuple2)
print(mytuple3)
## different data tuples
mytupleDif = ("Hi","My",2,True ,"5",False)
print(mytupleDif)
## type of tuple
mytupleDif = ("Hi","My",2,True ,"5",False)
print(type(mytupleDif))
## tuple constructor
mytuple = tuple(("Hi","My",2,True ,"5",False))
print(mytuple) 
## acces to tuple elements
mytuple = ("Hi","My",2,True ,"5",False)
print(mytuple[0]) 
## negative tuple indexing
mytuple = ("Hi","My",2,True ,"5",False)
print(mytuple[-2]) 
## index range
mytuple = ("Hi","My",2,True ,"5",False)
print(mytuple[1:4]) 
## start index range
mytuple = ("Hi","My",2,True ,"5",False)
print(mytuple[:4]) 
## include index range
mytuple = ("Hi","My",2,True ,"5",False)
print(mytuple[4:])
## negative index range
mytuple = ("Hi","My",2,True ,"5",False)
print(mytuple[-4:-1])
## negative index include  
mytuple = ("Hi","My",2,True ,"5",False)
print(mytuple[:-4:-1])
## check element of tuple
mytuple = ("Hi","My",2,True ,"5",False)
if "Hi" in mytuple:
    print("Yes, Hi in tuple") 

## update tuples
