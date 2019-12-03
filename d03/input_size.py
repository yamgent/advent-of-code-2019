A = input().split(',')
B = input().split(',')

a = 0
for w in A:
    a += int(w[1:])

b = 0
for w in B:
    b += int(w[1:])

print('Length of wire A is: ' + str(a))
print('Length of wire B is: ' + str(b))
