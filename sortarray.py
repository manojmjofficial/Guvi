#Program to find sort elements in an array
n=int(input())
arr=[]
for i in range(n):
	a=int(input())
	arr.append(a)
arr.sort()
print(arr)
