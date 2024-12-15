empty_set = set()

empty_set.add(2)
print(empty_set)

data_set = {"Joenel", 20, "CVSU"}
data_set.discard(20) #use discard instead of remove to avoid runtime
#error if it was not exist on set

print(data_set) 

#Also we have set operations called in Sets 
#set1 | set2  # Union
#set1 & set2  # Intersection
#set1 - set2  # Difference

#For Union we well combine 2 sets 
set_1 = {1,2,3,4,5}
set_2 = {6,7,8,9,5}
result = set_1 | set_2 #just add 2 sets using pipe "|" but will not add the same data
print(f"Union: {result}")

#for Intersection which is &, it was printing the similar data only from set 1 and set 2
intersection_result = set_1 & set_2
print(f"Intersection: {intersection_result}")

#for Difference "-" this will print the data that not same from set 1, not included the set 2 like just removing the data in set_1 that have same value or data in set_2
difference_result = set_1 - set_2
print(f"Difference results: {difference_result}")



