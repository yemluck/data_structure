"""
Given a sorted array, create a new array containing squares of all the numbers of the input array in
the sorted order.

Example 1:
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
"""

# Solution
#1 Naive Solution/Brute force

def make_square1(arr):
    output = []
    for num in arr:
        output.append(num**2)
    output.sort()
    return output

# print(make_square1([2,4,-1]))


#2: Using two pointers
def make_square2(arr):
    output = [0 for _ in range(len(arr))]
    length = len(arr) - 1
    left, right = 0, length
    while left <= right:
        left_square = arr[left]**2
        right_square = arr[right]**2

        if left_square > right_square:
            output[length] = left_square
            left += 1
        else:
            output[length] = right_square
            right -= 1
        length -= 1
    return output


print(make_square2([-5,2,3, 4,5]))