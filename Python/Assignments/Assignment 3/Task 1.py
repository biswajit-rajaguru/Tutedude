"""

Task 1: Calculate Factorial Using a Function 

Problem Statement: Write a Python program that:

    1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
    2.   Returns the calculated factorial.
    3.   Calls the function with a sample number and prints the output.
 
"""

# factorial function calculates the factorial of n using a loop
def factorial(n):
    
    """
    n: nonegative integer
    return: the factorial of n 
    
    Calculates factorial of n using a loop
    """
    # checks to make sure n is a nonnegative integer
    if not isinstance(n,int) or n < 0:
        #Error: the input should be a non-negative integer
        return "Error"
    
    factorial = 1 # initialize the variable to multiplicative unity

    # Using a for loop we multiply the numbers n,n-1,\ldots,1 
    # when n=0, we do not multiply anything, hence 0!=1. 
    
    while n > 0 :
        factorial *= n
        n -= 1

    return factorial


#test_values = ["something", -3,-1,0,1,5,1000]
#for n in test_values:
#    print(f"Factorial of {n} is: {factorial(n)}")

# Asking the user to enter a number 
n = int(input("Enter a number: "))
# Outputting the factorial of n in the required format
print(f"Factorial of {n} is: {factorial(n)}")





