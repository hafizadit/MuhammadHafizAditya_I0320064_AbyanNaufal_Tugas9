import array

A = array.array('i')

A.append(50)
A.append(-20)
A.append(30)
A.insert(1,40)
A.remove(-20)

# Menggunakan perintah for
for nilai in A:
    print("%d"%nilai, end=' ')

# Menggunakan perintah While
i = 0
while i < len(A):
    print("%d"%A[i],end=' ')
    i += 1

print('\n',A.index(30))