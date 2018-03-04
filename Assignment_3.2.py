string1 = 'ACADGILD'
string = 'xyz'
integers = '1234'
list1 = ['x','y','z']
list2 = [1,2,2,4]

print([x for x in string1])
print([string[i]*j for i in range(0,len(string)) for j in range(1,5)])
print([i*j for i in list2 for j in list1])
print([[i+j] for i in range(1,4) for j in range(1,4)])
print([[i+j,i+j+1,i+j+2,i+j+3] for i in range(1,5) for j in range(1,2)])
print([(j+1,i) for i in range(1,4) for j in range(0,3)])