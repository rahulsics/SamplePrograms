my_array = [2,5,0,4,2,7,0,0,1,9,4]
test_array_0 = []
test_array_non0 = []
for i in my_array:
    if i!=0:
        test_array_non0.append(i)
    else:
        test_array_0.append(i)
print(test_array_non0+test_array_0)
