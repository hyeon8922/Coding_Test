#10988

s=input()
s_i=list(s[:len(s)//2])
s_r=list(s[len(s)//2+1*(len(s)%2):])
s_r.reverse()
if s_i==s_r:
    print('1')
else:
    print('0')
