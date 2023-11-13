#5622

s=input()
result=0
dial=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
for i in s:
    for k in range(len(dial)):
        if i in dial[k]:
            result+=k+3
print(result)
