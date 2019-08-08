#Program to find median in an array
import statistics
n=int(input())
arr=[]
for i in range(n):
	a=int(input())
	arr.append(a)
print(statistics.median(arr))
