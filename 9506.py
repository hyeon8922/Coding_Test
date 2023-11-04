#9506
while True: 
    lst=[] 
    n=int(input()) 
    if n==-1: 
        break 
    for i in range(1,n): 
        if n%i==0: 
            lst.append(i) 
    if n==sum(lst): 
        print(n,'=',end=' ') 
        for i in lst[:-1]: 
            print(i,end=' + ') 
        print(lst[-1]) 
    else: 
        print(n,'is NOT perfect.')
# for문에 (1,n)이라고 0(나누기 오류 뜸 >> try except)과 n(출력방해)이 포함 되지 않고 append할 수 있음
