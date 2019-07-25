#sum of n natural numbers
num = int(input())
if num < 0:
   print(0)
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print(sum)
