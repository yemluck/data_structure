"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.


Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

"""

# Naive solution

def fizzBuzz(n):
    stack = []
    for number in range(1, n + 1):
        if number % 3 == 0 and number % 5 == 0:
            stack.append("FizzBuzz")
        elif number % 3 == 0:
            stack.append("Fizz")
        elif number % 5 == 0:
            stack.append("Buzz")
        else:
            stack.append(str(number))
    return stack

# Bad solution. Worst case scenario is O(nxm)
def fizzBuzz2(n):
    stack = ["" for x in range(1,n+1)]
    for i in range(1, n+1):

        if i%3 == 0:
            stack[i-1] += "Fizz"
        if i%5 == 0:
            stack[i-1] += "Buzz"
        if stack[i-1] == "": stack[i-1] = str(i) # This loops through a second array

    return stack

# Optimal solution
def fizzBuzz3(n):
    stack = []
    for i in range(1, n+1):
        current = ""

        if i%3 ==0:
            current += "Fizz"
        if i%5 == 0:
            current += "Buzz"
        if current == "":
            current = str(i)
        stack.append(current)

    return stack



print(fizzBuzz(16))
print(fizzBuzz2(16))
print(fizzBuzz3(16))