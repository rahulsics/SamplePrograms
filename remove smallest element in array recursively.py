lst = [1, 2, 3, 4, 5]

while lst:
    newlst = []
    i = min(lst)
    lst.remove(i)
    for j,x in enumerate(lst):
        b= lst[j]
        newlst.append(b - i)
    print(newlst)