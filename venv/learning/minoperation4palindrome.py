st = input("Enter the string:")
s = list(st)
n = len(s)
# To store the number of replacement operations
cc = 0
for i in range(n // 2):
    # If the characters at location
    # i and n-i-1 are same then
    # no change is required
    if s[i] == s[n - i - 1]:
        continue
    # Counting one change operation
    cc += 1
    # Changing the character with higher
    # ascii value with lower ascii value
    if (s[i] < s[n - i - 1]):
       s[n - i - 1] = s[i]
    else:
        s[i] = s[n - i - 1]
print("Minimum characters to be replaced = ", str(cc))