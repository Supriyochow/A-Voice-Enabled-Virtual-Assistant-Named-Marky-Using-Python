x=int(input("Enter a number "))
k=0
n=x
while n!=0:
	r=n%10
	k=k+r
	n=n//10
	
print("The sum of the digits of ",x," is ",k)