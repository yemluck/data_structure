"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should
be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit
Zgvb in nums1.
"""

def merge(nums1, m, nums2, n):
    # Initialize the pointers
    x,y = m-1, n-1
    # Let the third pointer be z. We will loop from the end of nums1

    for z in range(len(nums1)-1, -1, -1):
        # if we get to the end of list nums1
        if x<0:
            nums1[z] = nums2[y]
            y-=1
        elif y<0:
            # nums1[z] = nums1[x]
            # Just break instead of overwriting same numbers in array nums 1
            break
        elif nums1[x] > nums2[y]:
            nums1[z] = nums1[x]
            x-=1
        else:
            nums1[z] = nums2[y]
            y-=1

merge([1,2,3,0,0,0], 3, [-2,5,6], 3)