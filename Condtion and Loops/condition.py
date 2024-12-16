human_count = 9

if human_count > 10:
    print("human is greater than 10")
elif human_count < 10:
    print("human is less than 10")
else:
    print("no match value")


#for is good for iterating over a collection
#while loop is good when the condition is based on something that may change over time.
#list comprehensions

banana_lists = ["ban1", "ban2", "ban3", "ban4"]  #this is list because its [] //Sample data


#for loops in collections
for item in banana_lists: #only the for loop in list comprehensions can have a value first before "for"
    
    if item == "ban1":
        continue #skip the ban1 start the print to ban2
    print(item)
    if item == "ban3":
        print(f"{item} found!")
        break #break to stop the search



#while loops in that change over time.
banana_count = len(banana_lists) #4

while banana_count > 0:
    print(banana_count)
    banana_count -= 1

else: 
    print("While off!") #print after the while loop



#List Comprehensions for ( for loops )
numbers = [1,2,3,4,5, 6]
number_item = [ item * 2 / 5 for item in numbers ] #readable because is it in same list
print(number_item)

#Combining loop condition to a list comprehensions
number_condition = [ num for num in numbers if num % 2 != 0 ] #list comprehensiosn can't put a print and break
print(number_condition) #if 5 Modulo means divide and check the remainder, here in my code if num divide by 2 and check the remainder is not equal to (!=) it means the result in number condition is the 1,3,5 which is odds, if it was == 0 or equal zero the remainder it was even the result will be 2,4,6

    