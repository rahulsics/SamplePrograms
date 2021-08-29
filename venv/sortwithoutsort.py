a = [5,6,7,32,56,2,9,4,2]
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j+1]<a[j]:
            a[j], a[j+1]= a[j+1], a[j]
print(a)