

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