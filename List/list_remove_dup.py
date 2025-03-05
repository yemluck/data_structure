"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
element appears only once. The relative order of the elements should be kept the same. Then return the number
of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they
were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""

def remove_duplicates(nums):
    length = len(nums)

    # Edge case
    if length<2:
        return length

    # two pointers
    l=0
    r=0

    while r<length:
        if nums[l] == nums[r]:  # if it is not a distinct val
            r += 1 #keep looping till you find a distinct val
        else:
            l += 1 # if distinct, move the left pointer and assign it the new distinct value
            nums[l] = nums[r]

    # since l is an index pointer, return l+1 for number of distinct val in the list
    return l+1