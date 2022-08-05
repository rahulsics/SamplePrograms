n = int(input("Enter the Vertices:"))
for i in range(0, n):
    for j in range(0, i+1):
        print("* ", end = "")
    print(" ")
for i in range(0, n):
    for j in range(i, n-1):
        print("* ", end = "")
    print(" ")
k = int(input("Enter the Vertices:"))
for l in range(k):
    for m in range(k):
        if(m==0 or m==k-1 or l==0 or l==k-1):
            print("* ", end="")
        else:
            print("  ", end ="")
    print(" ")