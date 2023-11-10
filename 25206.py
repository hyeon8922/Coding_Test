#25206

rank=['A+','A0','B+','B0','C+','C0','D+','D0','F']
score=[4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]
result=0
cnt=0
for i in range(20):
    s=list(input().split())
    s[1]=float(s[1])
    if s[2]!='P':
        result+=s[1]*score[rank.index(s[2])]
        cnt+=s[1]
print('%.6f'%(result/cnt))

 
