#Tuple is not immutable cannot change while list is immutable or can change

coordiantes = (10,20)
print(coordiantes)

tuple = ("joenel",) #if adding one item only put comma , to recognize its a tuple not str
print(type(tuple))

def get_user(name):
    return (name, "20 yrs old")

user_info = get_user("Joenel")
print(user_info)

number_list = (1,2,3,4)

for item in number_list:
    print(item)