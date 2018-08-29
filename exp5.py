#input a range where u get the 2nd value as square of 1st value

"""l_range = int(input("enter a number"))
u_range = int(input("enter a number"))
a=[(x,x*x) for x in range (l_range, u_range)]
print(a)"""""

#to fetch the whole square number in arange


"""l_range = int(input("enter a number"))
u_range = int(input("enter a number"))
a=[x for x in range(l_range,u_range) if (int(x**0.5))**2==x and sum(list(map(int,str(x))))]
print(a)"""

# find the sum of the consecutive numbers

a=[1,2,3,4,5]
#b=[sum(a[0:x+1]) for x in range(0,len(a))]
b=[sum(a[0:x+1])  for x in  range(0,len(a))]
print(a)
print(b)


