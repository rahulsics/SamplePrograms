s= [0,1,2,3,4,5,6,7,8]
s_odd = s[::2]
s_even = s[1::2]
print(s_odd)
print(s_even)
s_odd1 =[]
s_even1=[]
for i,v in enumerate(s):
    if i%2!=0:
        s_even1.append(i)
    else:
        s_odd1.append(i)
print(s_odd1)
print(s_even1)