# Task
# Write a Python program that does the following:

# Accepts a list of numbers from the user (as comma-separated values, e.g., 1,2,3,4).
# Checks if all the numbers in the list are positive integers.
# Calculates:
# The sum of the numbers.
# The average of the numbers.
# The largest number in the list.
# Display the results in a user-friendly format.
# Add comments to explain each part of your code.


numbers = input("Input any numbers: ")
number_split = numbers.split(",") #removing "," in list

convertstr = [int(num) for num in number_split] #converting str into int
convertstr.sort() #sorting the user input numbers to lowest to highest to catch the largest number in list

if all(num > 0 for num in convertstr):
    print("All numbers is positive")
    sum_of_numbers = 0
    largest_number = 0

    for x in convertstr:
            sum_of_numbers += x # sum = 0, sum = sum + 1, sum = sum(currently 1 value) + 2, sum = sum(3) + 3 = so on+
            if x > largest_number:
                largest_number = x

else:
    print("some numbers are negative")

#Display the sum, average and largest number in List
average = sum_of_numbers/len(convertstr)
print(f"sum of all numbers is {sum_of_numbers}")
print(f"the average is {average}")
print(f"the largest number in list is: {largest_number}")