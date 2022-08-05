s = input("Enter the String:")
test = ""
for i, val in enumerate(s):
    if (i % 2) != 0:
        test = test + "" + s[i]
print(test)
