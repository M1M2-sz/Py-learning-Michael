

##learning py

##Lists
##String type list
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
##Edit list
mylist = ["apple","banana","cherry","orange","kiwi","mango"]
mylist[1] = "banana1"
print(mylist) 
##
