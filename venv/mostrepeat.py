a = [1,2,2,1,3,4,2,1,2,1]
max =0
num  =0
for i in set(a):
    cont = a.count(i)
    if(max<cont):
        num = i
        max = cont
print(num, max)
d = {}
for j in a:
    if j in d:
        d[j]+=1
    else:
        d[j]= 1
nmax =0
for key, value in d.items():
    if value>nmax:
        nmax = key
print(nmax, d[nmax])
