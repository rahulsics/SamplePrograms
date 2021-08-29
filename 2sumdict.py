def printPairs(arr, sum):
    # Create an empty hash set
    d={}
    for i, val in enumerate(arr):
        diff = sum- val
        if diff in d:
            return [d[diff], i]
        d[val] =i
    return []


# driver code
A = [1, 4, 45, 6, 10, 8]
n = 16
li = printPairs(A, n)
print(li)
s = set()
# do for every element in the list
for i in A:
    # check if pair with the given difference `(i, i-diff)` exists
    if n-i in s:
        n1 = A.index(i)
        n2 = A.index(n-i)
        print((n1, n2))
    # check if pair with the given difference `(i + diff, i)` exists
    s.add(i)