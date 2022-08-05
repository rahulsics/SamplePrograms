s = input("Enter the Sentence:")
rev = ""
for i in s.split():
    rev = i + " "+rev
print(rev)
print(s[::-1])
r = ""
for i in s.split():
    for t in i:
        r = t+r
print(r)
start=0
end = len(s)-1
ls= list(s)
while start<end:
    if ls[start]==' ':
        start=start+1
    elif ls[end]==' ':
        end=end-1
    else:
        ls[start], ls[end]=ls[end], ls[start]
        start = start + 1
        end = end - 1
print(''.join(ls))