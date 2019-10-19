n=int(input("Enter the size of A you want to print : "))
for i in range(1,n+1):
    print("*"," "*(n-1) if i<n else "*"*(n),"*"*n if i==1 or i==n else "*",sep="")
for i in range(2,n+1):
    print(" "*n if i!=n else "*"*n,"*"," "*(n-1),"*",sep="")
