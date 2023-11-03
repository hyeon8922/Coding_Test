#5073

while True:
    x=list(map(int,input().split()))
    if x[0]==x[1]==x[2]==0:
        break
    if sum(x)-max(x)<=max(x):
        print('Invalid')
    elif x[0]==x[1]==x[2]:
        print('Equilateral')
    elif x[0]!=x[1] and x[1]!=x[2] and x[0]!=x[2]:
        print('Scalene')
    else:
        print('Isosceles')
