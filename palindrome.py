#To check whether the number is Palindrome or not
N=int(input())
temp=N
rev=0
while(N>0):
    dig=N%10
    rev=rev*10+dig
    N=N//10
if(temp==rev):
    print("yes")
else:
    print("no")
