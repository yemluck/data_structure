"""
2D array


"""

def richest_customer(arr):
    richest = 0

    for row in arr:
        total = 0
        for num in row:
            total += num
        richest = max(richest, total)

    print("this is the richest:", richest)
    return richest


richest_customer([[7, 1, 37],
                  [2,8,7],
                  [1,9,15]
                  ])