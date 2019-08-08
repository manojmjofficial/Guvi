#Program to print array elements with index
n=int(input())
arr=[]
b=0
for i in range(n):
	a=int(input())
	arr.append(a)
for i in arr:
	print(i," ",b)
	b+=1
