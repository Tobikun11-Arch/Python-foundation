List = ["Joenel", "Gab", "May-anne"]
print(len(List))

BooleanList = [True, False, True]
print(len(BooleanList))

randomList = ["string", True, 10]
print(randomList)

print(type(randomList))

print(randomList[0])


names = ["name1", "name2", "name3", "name4", "name5", "name6"]
print(names[1:])
print(names[:1])
print(names[-4]) #start from end of array and start to count from 1 instead of 0 because of negative, negative means backward and 1

if "name" in names:
    print("name2 existed")

else:
    print("not existing")


names[2:5] = ["name03", "name04", "name05"] #if 1 its started literally in 1 if its end in 5 it ends on 4
print(names)

names[1:2] = ["name02", "name002", "name0002"] #targeted the 1 only because it was close to 2 which is not counted
print(names)

#.append it will add to last of array
#.insert must put which index you want to add it
#.extend it will merge the new array list to a main list
#.remove is like add but dont need an index
#.pop will remove the specified index
#.pop() remove the last item

names.insert(0, "name00")
print(names)

names01 = ["Joenel", "gab"]

names.extend(names01)
print(names)


names.remove("gab")
names.pop(2)
print(names)
names.pop()
print(names)
names.clear()
print(names)
del names #delete literally the names while clear is the store data only

subjects = ["OOP", "IM", "Filipino"]
int = 0

while int < len(subjects): #while loop 
    print(subjects[int])
    int = int + 1

[print (x) for x in subjects]  #for loop



for i in subjects:
    print(f"subjects is {i}")
