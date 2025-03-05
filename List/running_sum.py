"""
1480. Running Sum of 1D array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0] ... nums[i]

Example1:
Input: nums = [3, 1, 2, 10, 1]
Output: nums = [3, 4, 6, 16, 17]
"""

def running_sum(arr):
    total = 0
    result = []
    for i in range(len(arr)):
        total += arr[i]
        result.append(total)

    print(f"this is the result: {result}")
    return result


running_sum([3,1,2,10,1])
