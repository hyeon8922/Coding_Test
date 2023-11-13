 

#10809

S = input()
abc ='abcdefghijklmnopqrstuvwxyz'
for i in abc:
    if i in S:
        print(S.index(i), end= ' ')
    else:
        print( -1, end =' ')

# print(*map(input().find,map(chr,range(97,123))),sep=" ") 다른방법
