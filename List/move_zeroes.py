"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Could you minimize the total number of operations done?
"""

def move_zeroes(nums):
    l = 0
    r = 0

    while r<len(nums):
        if nums[r] != 0:
            nums[l] = nums[r]
            r +=1
            l +=1
        else:
            while nums[r] == 0:
                r += 1
            nums[l] 
    return nums

print(move_zeroes([0,1,0,12]))