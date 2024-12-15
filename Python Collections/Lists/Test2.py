# web = ["web app", "website", "w3school"]

# i = 0
# while i < len(web):
#     print(web[i])
#     i = i + 1

# newWeb = []

# for i in web:
#     print(f"this is the i {i}")
#     if "e" in i:
#         newWeb.append(i)

# print(newWeb)


# print("---------------------------")
# newListWeb = [ x for x in newWeb if "a" in x]

# print(newListWeb)

# names = ["jak", "bbw", "reds"]
# userID = input("Input user id: ") #Expected output joenel
# GenerateId = [f"{userID.lower()}_{x}" for x in range(3, 24, 3)] #range have (start, stop, step)
# print(GenerateId)

# GenerateIds = [f"{userID.lower()}_{x}" for x in names]
# print(GenerateIds)

# airlines = ["vcda caroline", "Jake lam", "bsme", "KLerry"]
# airlinesCount = [3,8,2,5,10,2,4]
# airlines.sort(key = str.lower) #must use key func to not make an error of ASCII values
# airlinesCount.sort()
# print(airlines)
# print(airlinesCount)

# airlines.reverse()
# print(airlines)

# newList = list(airlines)
# print(f"copy only: {newList}")

# newAirlines = ["newtobi", "newAir"]
# airlines.extend(newAirlines) #merge 2 lists
# print(airlines)



# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list