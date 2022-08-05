s1 = input("Enter the First string:")
s2 = input("Enter the second string:")
s1sorted = ''.join(sorted(s1))
s2sorted = ''.join(sorted(s2))
s1len = len(s1sorted)
s2len = len(s2sorted)
s = 0
if s1len > s2len:
    for i, val in enumerate(s2sorted):
        if s1sorted[i] == s2sorted[i]:
            continue
        else:
            s = (s1len - (i + 1))
            break
else:
    for i, val in enumerate(s1sorted):
        if s1sorted[i] == s2sorted[i]:
            continue
        else:
            s = (s2len - (i + 1))
            break
print(s)
