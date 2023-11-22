import sys
n = input()
k = input()
lst1, lst2=[],[]

for i in n:
    lst1.append(int(i))
for i in k:
    lst2.append(int(i))
    
n= sorted(lst1)
k= sorted(lst2)

if n == k:
    print('YES')
else:
    print('NO')
        
