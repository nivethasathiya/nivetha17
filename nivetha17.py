c=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    c.append(b)
c.sort()
print("Largest element is:",c[n-1])
