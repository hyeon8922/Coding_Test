#2501
lst=[] 
a,b=map(int,input().split()) 
for i in range(10000): 
    try: 
        if a%i==0: 
            lst.append(i) 
    except: 
        pass 
try: 
    print(lst[b-1]) 
except IndexError: 
    print(0)
