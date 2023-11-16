#2588

x=int(input())
y=int(input())
a=y%10
c=y//100
b=(y-(c*100))//10
three=x*a
four=x*b
five=x*c
six=x*y
print(three,four,five,six,sep='\n')
