#Print sum of arithmetic progression till n terms given n,a,d
n = int(input())
a = int(input())
d = int(input())
sum = 0
i = 0
while i < n : 
	sum = sum + a 
	a = a + d 
	i = i + 1
print (sum)
