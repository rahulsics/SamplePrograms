s = input("Enter the string:")
d = {}
for i in s:
    if i in d:
        d[i] +=1
    else:
        d[i]= 1
print(d)
res2 =""
res = ''.join(key + str(val) for key, val in d.items())
print(res)
res1 = ''.join(key + str(val) for key, val in sorted(d.items()))
print(res1)
for k in sorted(d, key=d.get, reverse=True):
    res2 = res2+ ''.join(k +str(d[k]))
print(res2)
