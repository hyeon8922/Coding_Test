txt = input()
txt = txt.upper()
if len(set(txt)) == 26:
    print('YES')    
else:
    print('NO')
