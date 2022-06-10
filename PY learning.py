

## Learning py

## Lists

## string type list
from string import printable
from types import MethodDescriptorType


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
mytuple = ("Hi","My",2,True ,"5",False)
mylist = list(mytuple)
mylist[1] = "MyApple"
mytuple = tuple(mylist)
print(type(mytuple))
print(mytuple)
## add elements
mytuple = ("Hi","My",2,True ,"5",False)
mylist = list(mytuple)
mylist.append("MyApple")
mytuple = tuple(mylist)
print(type(mytuple))
print(mytuple)
## add tuple to tuple
mytuple = ("Hi","My",2,True ,"5",False)
mytuple1 = ("Go",2)
mytuple += mytuple1
print(mytuple)
## remove elements of tuple
mytuple = ("Hi","My",2,True ,"5",False)
mylist = list(mytuple)
mylist.remove("My")
mytuple = tuple(mylist)
print(type(mytuple))
print(mytuple)
## delete tuple
mytuple = ("Hi","My",2,True ,"5",False)
del mytuple
print(mytuple)

## pack tuple
mytuple = ("Hi","My","Cars")
print(mytuple)
## unpack tuple
(Hi,My,Cars) = mytuple
print(Hi)
print(My)
print(Cars)
## using asterisk *
mytuple = ("Hi","My","bmw","honda")
(Hi,My,*CarsList) = mytuple
print(Hi)
print(My)
print(CarsList)
## using asterisk * 
mytuple = ("Hi","My","bmw","honda")
(Hi,My,*CarsList,andAll) = mytuple
print(Hi)
print(My)
print(CarsList)
print(andAll)

## cycle across tuple
mytuple = ("Hi","My","bmw","honda")
for x in mytuple:
    print(x)
## cycle on index numbers
mytuple = ("Hi","My","bmw","honda")
for i in range(len(mytuple)):
    print(mytuple[i])
## use while
mytuple = ("Hi","My","bmw","honda")
i = 0
while i < len(mytuple):
    print(mytuple[i])
    i = i + 1

## join tuples
mytuple1 = ("1","2","3")
mytuple2 = (1,2,3)
mytuple3 = mytuple1 + mytuple2
print(mytuple3)
## multiply tuples *
mytuple = ("Hi","My","bmw","honda")
mytuple1 = mytuple * 2
print(mytuple1)

## tuples methods
##count()-Returns the number of times a specified value occurs in a 
# tuple
##index()-Searches the tuple for a specified value and returns the 
# position of where it was found


## Sets

## set
myset = {"string1", "string2", "string3"}
print(myset)
## duplicates not allowed - sets ignore duplicates
myset = {"string1", "string2", "string3", "string1"}
print(myset)
## length set
myset = {"string1", "string2", "string3"}
print(len(myset))
## set data types
myset1 = {"1", "2", "3", "4", "5"}
myset2 = {1, 2, 3, 4, 5}
myset3 = {True, False}
myset4 = {1.2, 1.3, 1.5, 5.5}
myset5 = {"2", "go", 22, 323, True, 2.4, 5.5}
print(myset1)
print(myset2)
print(myset3)
print(myset4)
print(myset5)
## set type
myset5 = {"2", "go", 22, 323, True, 2.4, 5.5}
print(type(myset1))
## use set constructor
myset = set(("2", "go", 22, 323, True, 2.4, 5.5))
print(myset)

## set elemnts acess - cycle
myset = {"2", "go", 22, 323, True, 2.4, 5.5}
for x in myset:
    print(myset)
## search element in set
myset = {"2", "go", 22, 323, True, 2.4, 5.5}
print("go" in myset)
## add element in set
myset = {"2", "go", 22, 323, True, 2.4, 5.5}
myset.add("rakamakafo")
print(myset)
## add set to set
myset = {"2", "go", 22, 323, True, 2.4, 5.5}
myset1 = {"333","bmw","plane"}
myset.update(myset1)
print(myset)
## add list to set
myset = {"2", "go", 22, 323, True, 2.4, 5.5}
mylist = ["333","bmw","plane"]
myset.update(mylist)
print(myset)
## remove item
myset = {"2", "go", 22, 323, True, 2.4, 5.5}
myset.remove("2")
print(myset)
## remove item
myset = {"2", "go", 22, 323, True, 2.4, 5.5}
myset.discard("2")
print(myset)
## remove end item
myset = {"2", "go", 22, 323, True, 2.4, 5.5}
x = myset.pop()
print(x)
print(myset)
## clear set
myset = {"2", "go", 22, 323, True, 2.4, 5.5}
myset.clear()
print(myset)
## delete set
myset = {"2", "go", 22, 323, True, 2.4, 5.5}
del myset
print(myset)

## set cycles
myset = {"2", "go", 22, 323, True, 2.4, 5.5}
for x in myset:
    print(x)

## join sets
myset = {"2", "go", 22, 323, True, 2.4, 5.5}
myset1 = {"yes", "no", 33, 444} 
myset3 = myset1.union(myset2)
print(myset3)
## paste set element
myset = {"2", "go", 22, 323, True, 2.4, 5.5}
myset1 = {"yes", "no", 33, 444} 
myset.update(myset1)
print(myset)
## save only duplicates
myset = {"2", "go", 22, 323, True, 2.4, 5.5}
myset1 = {"2", "go", 33, 444} 
myset.intersection_update(myset1)
print(myset)
## return duplicates elements in set1 and set2 in new set
myset = {"2", "go", 22, 323, True, 2.4, 5.5}
myset1 = {"2", "go", 33, 444} 
myset2 = myset.intersection(myset1)
print(myset2)
## save all but not duplicates
myset = {"2", "go", 22, 323, True, 2.4, 5.5}
myset1 = {"2", "go", 33, 444} 
myset.symmetric_difference_update(myset1)
print(myset)
## save duplicates
myset = {"2", "go", 22, 323, True, 2.4, 5.5}
myset1 = {"2", "go", 33, 444} 
myset3 = myset.symmetric_difference(myset1)
print(myset3)
## set methods
#add()	Adds an element to the set
#clear()	Removes all the elements from the set
#copy()	Returns a copy of the set
#difference()	Returns a set containing the difference between two or more sets
#difference_update()	Removes the items in this set that are also included in another, specified set
#discard()	Remove the specified item
#intersection()	Returns a set, that is the intersection of two other sets
#intersection_update()	Removes the items in this set that are not present in other, specified set(s)
#isdisjoint()	Returns whether two sets have a intersection or not
#issubset()	Returns whether another set contains this set or not
#issuperset()	Returns whether this set contains another set or not
#pop()	Removes an element from the set
#remove()	Removes the specified element
#symmetric_difference()	Returns a set with the symmetric differences of two sets
#symmetric_difference_update()	inserts the symmetric differences from this set and another
#union()	Return a set containing the union of sets
#update()	Update the set with the union of this set and others


## Dictionaries 

## Dictionary
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
print(mydict)
## dictionary index
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
print(mydict["brand"])
## non duplicates
mydict = {"brand":"bbw", "brand":"bmw", "model":"530", "engine type":"diesel"}
print(mydict)
## lenth 
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
print(len(mydict))
## types
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
print(type(mydict))
## types
mydict = {"brand":False, "model":12, "engine type":2.5}
print(type(mydict))
print(mydict)
## access to elements
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
print(mydict["brand"])
## get
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
print(mydict.get("brand"))
## keys
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
print(mydict.keys())
## keys
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
x = mydict["brand"]
print(x)
## get keys
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
x = mydict.keys()
print(x)
## add element
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
x = mydict.get("brand")
print(x)
## adding elements & refresh keys
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
x = mydict.keys()
print(x)
mydict["model"] = "550"
print(mydict["model"])
## get values
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
x = mydict.values()
print(x)
## add changes
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
x = mydict.values()
print(x)
mydict["model"] = "540"
print(x)
## get items
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
x = mydict.items()
print(x)
## changes after get items
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
x = mydict.items()
print(x)
mydict["engine type"] = "cosmo"
print(x)
## adding element
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
x = mydict.items()
print(x)
mydict["space type"] = "cosmo"
print(x)
## key search
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
if "bmw" in mydict:
    print("yeah we have bmw")

## change dictionary elements
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
mydict["model"] = "550"
print(mydict)
## update dictionary
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
mydict.update({"model":"550"})
print(mydict)
## adding elements
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
mydict["color"] = "black"
print(mydict)
## removing items
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
mydict.pop("model")
print(mydict)
## remove last added elemtnt
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
mydict.popitem()
print(mydict)
## delete elem with key
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
del mydict["model"] 
print(mydict)
## delete dictionary
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
del mydict
print(mydict)
## clear dictionary
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
mydict.clear()
print(mydict)
## dictionary cycle
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
for x in mydict:
    print(x)
## dictionary cycle 
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
for x in mydict:
    print(mydict[x])
## check values in dictionary
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
for x in mydict.values():
    print(x)
## check keys in dictionary
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
for x in mydict.keys():
    print(x)
## check keys and items in items method
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
for x, y in mydict.items():
    print(x, y)

## copying dictionaries
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
mydict1 = mydict.copy()
print(mydict1)
## copy with method dict
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
mydict1 = dict(mydict)
print(mydict1)
## nested dictionaries
mydict = { "brand" : { "who" : "bmw" },
 "model" : { "what is?": "530" }, 
"engine type" : { "gasoline?" : "diesel" }
}
print(mydict)
## adding dictionaries to dictionaries
mydict = {"brand":"bmw", "model":"530", "engine type":"diesel"}
mydict1 = {"bran":"bm", "mode":"53", "engine typ":"diese"}
mydict2 = {"bra":"b", "mod":"5", "engine ty":"dies"}
mydict3 = { "1" : mydict, "2" : mydict1, "3" : mydict2}
print(mydict3)

## dictionary methods
#clear()	Removes all the elements from the dictionary
#copy()	Returns a copy of the dictionary
#fromkeys()	Returns a dictionary with the specified keys and value
#get()	Returns the value of the specified key
#items()	Returns a list containing a tuple for each key value pair
#keys()	Returns a list containing the dictionary's keys
#pop()	Removes the element with the specified key
#popitem()	Removes the last inserted key-value pair
#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()	Updates the dictionary with the specified key-value pairs
#values()	Returns a list of all the values in the dictionary

## If else
