#11653
n=int(input()) 
result=[] 
while n != 1: 
    for i in range(2,n+1): 
        if n % i==0: 
            n//=i 
            print(i) 
            break
