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
