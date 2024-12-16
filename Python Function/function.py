#Function is reusable code of block
#Functions help improve readability, reduce redundancy, and enhance maintainability.

'''
    1. Meaningful Names: Example: calculate_area() instead of func1().
    2. Keep It Short and Focused: Follow the Single Responsibility Principle.
    3. Use Type Hints: put the types like typrescript
        Example: def greet(name: str) -> str:
        but we can also put the other expected return value not just the same with parameters expected to get
    4. Document Your Function: example inside of func, a and b int will add etc..
    5. Default Arguments: def greet(name: str = "guest") -> str:
    6. Avoid Side Effects: Functions should not modify global variables or unexpected states unless explicitly required.
    7. Avoid Too Many Arguments: 3 limits only if its too much use dictionaries or custom classes
    8. Return Early: Use early return statements to make the logic clear and reduce nesting.   
        Example:
        def check_positive(num: int) -> str:
        if num < 0:
            return "Negative"
        return "Positive"
    9. Error Handling:     
        try:
        calculate_works = 10/0
        except ZeroDivisionError:
            print("You cannot divide by zero") #this will print the expected error you may encounter if
            you know what possible output if you dont know and catch generally use Exception as e

        try:
        calculate_works = 10/0
        except Exception as e: 
            print(f"You cannot divide by zero {e}") \
            
        #for raise its an custome error like throw new error on java

    Feature	                    Python
    Error Handling:             try, except, else, finally
    Custom Error:               raise Exception("msg")
    Finally Block:              Always runs
    Purpose:                    Handle and recover from runtime errors; prevent program crashes.
'''

try:
    calculate_works = 10/0
except ZeroDivisionError:
    print("You cannot divide by zero")


def get_user_score(score: int) -> str: #params expecting int value while the return value expecting string
    if score <= 0:
        raise ValueError("score must be positive!")
    elif score > 4:
        return f"you passed with score of {score}"

try:
    print( get_user_score(-5)) #Error, make this comment if want to test the 2nd print
    print( get_user_score(5)) #success

except Exception as e:  
    print(f"Error: {e}")