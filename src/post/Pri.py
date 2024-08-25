# Print even value
lst = [x for x in range(30) if x%2 == 0]
print(lst)

dic = {x:x*x for x in range(10) if x%2 != 0}
print(dic)

lst1 = []
for i in range(30):
    if i%2 == 0:
        lst1.append(i)
print('lst', lst1)

dic1 = {}
for i in range(10):
    if i%3 == 0:
        y = i*i
        dic1[i] = y
print('dic', dic1)

n = 5
for i in range(n):
    for j in range(n):
        if i+j==n-1 or i==n-1 or j==n-1:
            print("*",end=' ')
        else:
            print(' ', end=' ')
    print()
    
n = 5
for i in range(1,n+1):
    for j in range(1, n+1):
        if i+j==n+1 or i==n or j==n:
            print("*",end=' ')
        else:
            print(' ', end=' ')
    print()
print('\n')
    
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==n or i == 2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()