arr=[]
for _ in range(5):
    arr.append(int(input()))
arr.sort()
print(sum(arr)//5,arr[len(arr)//2+(len(arr)%2)-1],sep='\n')
