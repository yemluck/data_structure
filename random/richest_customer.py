"""
2D array


"""

def richest_customer(arr):
    richest = 0
    total = 0

    for row in arr:
        for num in row:
            total += num
        richest = max(richest, total)
        total = 0

    print("this is the richest:", richest)
    return richest


richest_customer([[7, 1, 3],
                  [2,8,7],
                  [1,9,5]
                  ])