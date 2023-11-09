#5597

lst=[i for i in range(1,31)]
for k in range(28):
    n=int(input())
    lst.remove(n)
print(min(lst),max(lst),sep='\n')

# i for i in range(1,31) list 한 번에 만들 수 있음.
