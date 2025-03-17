"""
Find the longest subarray with a sum less than a given amount


"""


def longest_sub_array(arr, val):

    l, cur, best = 0,0, 0

    for r in range(len(arr)):
        cur += arr[r]
        while cur >= val:
            cur -= arr[l]
            l += 1
        best = max(best, r-l+1)

    return best


print(longest_sub_array([19,5,2,0,1,8,12,3,6,9], 15))