# Write a program that asks the user for two inputs. First, ask for a string of words, for example, "hello world python". Then, ask for a string of numbers separated by commas, like "12, 45, -8, 0, 23". Your program should analyze both inputs. For the string of words, count how many words are in the input and create a new string by combining all the words (removing spaces) and converting it to uppercase. For the list of numbers, split the numbers, convert them into integers, and then calculate the sum of the numbers. From the same list, find and display the largest number and the smallest number. Finally, display the results for both the word analysis and the number analysis in a clear and readable format.



string_words = input("Input a string words: ")
string_numbers = input("Input a number words (please seperate it with comma): ")

#String words
string_split = string_words.split(" ")
string_wordsLength = len(string_split)
combined_words = ""
for x in string_split:
    combined_words += x

Upper_words = combined_words.upper()


#String numbers
split_numbers = string_numbers.split(",")
convert_int = [int(num) for num in split_numbers]
convert_int.sort()
Sum_of_numbers = 0
largest_numbers = 0
smallest_numbers = convert_int[0]
for x in convert_int:
    Sum_of_numbers += x
    largest_numbers = x

print(f"String for words is {Upper_words}")
print(f"Sum of numbers is {Sum_of_numbers}")
print(f"Largest numbers is {largest_numbers}")
print(f"Smallest numbers is {smallest_numbers}")