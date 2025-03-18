"""
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

Example 1:
Input: nums = [1,0,1,1,0]
Output: 4
Explanation:
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The max number of consecutive ones is 4.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 4
Explanation:
- If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
The max number of consecutive ones is 4.
"""

# SLIDING WINDOW

def max_consecutive_ones(nums):
    longest_sequence = 0
    l, r = 0, 0
    num_zeroes = 0

    while r < len(nums): # while our window is in bound
        if nums[r] == 0: # Increase num_zeroes if the rightmost element is 0
            num_zeroes += 1

        while num_zeroes == 2: # If our window is invalid, contract our window
            if nums[l] == 0:
                num_zeroes -= 1
            l += 1

        longest_sequence = max(longest_sequence, r-l+1) # Update our longest sequence answer

        r += 1 # Expand our window

    return longest_sequence


# Using for loop

def max_consecutive_ones2(nums):
    longest_sequence = 0
    l = 0
    num_zeroes = 0

    for r in range(len(nums)):
        if nums[r] == 0:
            num_zeroes += 1

        while num_zeroes == 2:
            if nums[l] == 0:
                num_zeroes -= 1
            l += 1

        longest_sequence = max(longest_sequence, r-l+1)

    return longest_sequence

print(max_consecutive_ones([1,1,1,1,0]))
print(max_consecutive_ones([1,0,1,1,0,1]))
print(max_consecutive_ones2([1,1,1,1,0]))
print(max_consecutive_ones2([1,0,1,1,0,1]))
