# sort according to 2ndkey

"""a=[['z',10],['b',2],['c',25]]

for i in range(0, len(a)):
    for j in range(0,len(a)-i-1):
        if (a[j][1]> a[j+1][1]):
           temp=a[j]
           a[j]= a[j+1]
           a[j+1]= temp
print(a)"""

# sort according to 1st key

a=[[55,10],[2,22],[66,25]]

for i in range(0, len(a)):
    for j in range(0,len(a)-i-1):
        if (a[j][1] > a[j+1][1]):
           temp = a[j]
           a[j] = a[j+1]
           a[j+1] = temp
print(a)
