"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000
"""

def max_sub_array(nums, k):
    max_avg = float("-inf")
    l = 0
    total = 0
    for r in range(k):
        total += nums[r]
    max_avg = max(total/k, max_avg)

    for r in range(k, len(nums)):
        total = total + nums[r] - nums[l]
        l += 1
        max_avg = max(total/k, max_avg)

    return max_avg

print(max_sub_array([1, 12, -5, -6, 50, 3], 4))