num = input().split('-')
lst = ['0','1','2','3','4','5','6','7','8','9']
answer = 'valid'
        
if num[0] != '010':
    answer = 'invalid'
    
if len(num) != 3:
    answer='invalid'
else:
    for i in range(2):  
        
        if len(num[i+1]) != 4:
            answer = 'invalid'
            break

        for j in num[i+1]:
            if j not in lst:
                answer = 'invalid'
                break
print(answer)
