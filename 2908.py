#2908

x=input()
lstX=""
lstY=""
for i in range(len(x)):
    lstX+=x[len(x)-i-1]
    if x[len(x)-i-1]==" ":
        x=x[0:len(x)-i-1]
        break
for i in range(len(x)):
    lstY+=x[len(x)-i-1]
if lstX > lstY:
    print(lstX)
else:
    print(lstY)
