s =[12,2,13,2,34,5,23,22]
for i in range(len(s)):
    for j in range(len(s)-i-1):
        if s[j]>s[j+1]:
            s[j], s[j+1]=s[j+1], s[j]
print(s)