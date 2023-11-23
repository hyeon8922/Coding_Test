num = input()
sum = 0 

for i in range(3):
    sum += int(num[ i*2+1 : i*2+3 ], 16)
avg = round(sum/3)

if len(hex(avg)[2:])<=1:
    color = '0'+hex(avg)[2:]
else:
    color = hex(avg)[2:]
print('#', color.upper()*3, sep='')
