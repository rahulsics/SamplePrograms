s = int(input("enter the number of rows:"))
count = 1
for i in range(1, s + 1):
    for j in range(1, i + 1):
        if j == i:
            print(str(count) + " ", end="")
        else:
            print(str(count) + " ", end="")
            count = count + 1
    print(" ")
