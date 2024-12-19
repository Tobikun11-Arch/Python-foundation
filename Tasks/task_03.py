from typing import List 
'''
    Two Sum Problem
Topics: Variables, Lists, If...Else, Loops.

Problem:
Given a list of integers nums and an integer target, return the indices of the two numbers that add up to target.
Assume there is exactly one solution, and you may not use the same element twice.

Example:
Output: [0, 1]
'''
target = 9

def search_case(nums: List[int])-> list[int]:
    nums_length = len(nums)
    index_lists = []
    while nums_length > 0:
        nums_dec = nums_length - 1
        print (nums[nums_dec])
        index_lists.append(nums[nums_dec])
        nums_length -= 1

search_case([2, 7, 11, 15])    
