"""
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
"""

def third_max(nums):
    big = bigger = float("-inf")
    biggest = nums[0]

    for num in nums:
        if num > biggest:
            biggest, bigger, big = num, biggest, bigger
        elif biggest >num > bigger:
            bigger, big = num, bigger
        elif bigger > num > big:
            big = num

    if big > float("-inf"):
        return big
    else:
        return biggest

    # print(f"this is big  {big}, this is bigger  {bigger} and this is biggest  {biggest}")
    # print(f"this is big  {big}, this is bigger  {bigger} and this is biggest  {biggest}")


print(third_max([2,2,3,1]))
print(third_max([1,2]))
print(third_max([3,2,1]))
print(third_max([-1,2,3]))
