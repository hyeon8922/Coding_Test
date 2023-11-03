#10101

x=int(input())
y=int(input())
z=int(input())
if (x+y+z)!=180:
    print('Error')
elif x==y==z==60:
    print('Equilateral')
elif x!=y and y!=z and x!=z:
    print('Scalene')
else:
    print('Isosceles')

# &(비트 연산자) 대신 and(논리연산 , =&&:python에 없음) 사용
