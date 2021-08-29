with open("sample.txt", 'r') as f:
    linecount = len(f.readlines())
    f.seek(0)
    letter = 0
    ld = {}
    wd = {}
    data = f.read()
    words = data.split()
    for i in words:
        letter = letter + len(i)
    print("The File has " + str(linecount) + " lines " + str(len(words)) + " words and " + str(letter) + " letters")
    for j in data:
        if j in ld and j != ('/\n/') and j != " ":
            ld[j] += 1
        else:
            ld[j] = 1
    for k in words:
        if k in wd:
            wd[k] += 1
        else:
            wd[k] = 1
    for key, value in ld.items():
        print(key + " appears " + str(value) + " times.")

    for key, value in ld.items():
        if value == max(ld.values()):
            print(key + " occurs the most number of times")

    for key, value in wd.items():
        print(key + " appears " + str(value) + " times.")

    for key, value in wd.items():
        if value == max(wd.values()):
            print(key + " occurs the most number of times which is " + str(value))

    maxi = 0
    for i in set(words):
        c = words.count(i)
        if maxi < c:
            maxi = c
            name = i
    print(name+" appears "+str(maxi)+" times")
