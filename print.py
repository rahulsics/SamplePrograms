l= [5,7,9,4,2,3]
result = 9
a= set()
flag = True
for i in l:
    comp = result - i
    a.add(i)
    if a.__contains__(comp):
        print(flag)
    else:
        a.add(i)
        flag = False
if flag == False:
    print("Poda patti")

