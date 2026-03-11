import bisect

def validTriplet(b):
    n = len(b)

    if n < 3:
        return False

    # Step 1: Build prefix minimum array
    p = [0] * n
    p[0] = b[0]
    for i in range(1, n):
        p[i] = min(b[i], p[i-1])

    # Step 2: Maintain sorted list using bisect
    sorted_list = [b[n-1]]

    for j in range(n-2, 0, -1):
        bj = b[j]
        bi = p[j-1]

        idx = bisect.bisect_right(sorted_list, bi)

        if idx < len(sorted_list):
            bk = sorted_list[idx]
            if bj > bk and bk > bi:
                print("Triplet found: bi={}, bj={}, bk={}".format(bi, bj, bk))
                return True

        bisect.insort(sorted_list, b[j])

    return False


# Test cases
print(validTriplet([2, 1, 5, 3, 4]))   # True  → bi=1, bj=5, bk=3
print(validTriplet([5, 4, 3, 2, 1]))   # False → strictly decreasing
print(validTriplet([1, 2, 3]))         # False → need b[j]>b[k]>b[i], here b[k]>b[j]
print(validTriplet([3, 1, 4, 2]))      # True  → bi=1, bj=4, bk=2
print(validTriplet([1, 2]))            # False → n < 3