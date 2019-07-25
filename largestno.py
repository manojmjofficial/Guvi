a = float(input())
b = float(input())
c = float(input())
if ((a > b) and (a > c)):
   l = a
elif ((b > a) and (b > c)):
   l = b
else:
   l = c
print(l)
