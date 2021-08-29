def findPair(A, diff):
    # list is unsorted
    # take an empty set
    s = set()
    # do for every element in the list
    for i in A:
        # check if pair with the given difference `(i, i-diff)` exists
        if i - diff in s:
            print((i, i - diff))
        # check if pair with the given difference `(i + diff, i)` exists
        if i + diff in s:
            print((i + diff, i))
        # insert the current element into the set
        s.add(i)


A = [2, 5, 1, 2, 2, 5, 5, 4]
diff = 3
findPair(A, diff)