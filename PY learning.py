

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
## search string
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
## list constructor list
mylist = list(("string1","string2","string3"))
print(mylist)
## index print
mylist = ["apple","banana","cherry"]
print(mylist[0])
print(mylist[-2])
## search string in list 
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
if "apple" in mylist:
    print("Yes,this 'apple' in list")
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
## 