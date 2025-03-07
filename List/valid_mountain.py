"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true
"""

# Naive solution
def valid_mountain(arr):
    if len(arr) < 3:
        return False

    left = 0
    right = len(arr)-1

    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            left +=1
        else:
            break
    for j in range(len(arr)-1, -1, -1):
        if arr[j] < arr[j-1]:
            right -= 1
        else:
            break

    if left ==0 or right == len(arr)-1: return False

    return left == right

print(valid_mountain([0,1,2,3,4,5,6,7,8,9]))