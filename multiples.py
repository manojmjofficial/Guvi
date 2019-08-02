#print multiples of a number
m =int(input())
n =int(input())
a = range(m, (n * m)+1, m) 
print(*a) 
