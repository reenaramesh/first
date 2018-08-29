# merge to list sort n display in other list

a=[1,3,5,7]
b=['a','b','c']
data_list = []
new1_list=[]
new_list = []
n_list = []
a_list=[]
#for i in a:
#data_list.append(a)
#for j in b:
#data_list.append(b)
#print("new list",new)
data_list=a+b
print("data_list", data_list)
while data_list:
    minimum = data_list[0]  # arbitrary number in list
    for x in data_list:
        if x < minimum:
            minimum = x

    new_list.append(minimum)
    data_list.remove(minimum)
print("new_list",new_list)

  #  for x in data_list:
      # if x not in new_list:
       #   new_list.append(x)


"""new_list=[21,22,12,12]
new1_list=[]


[new1_list.append(x) for x in new_list if x not in new1_list]


print (new1_list)"""

"""string = "uwdhwdl23hjk3h24hjk"
count = 0;
count1 = 0;
for i in string:

    if(i.isdigit()):
        count=count+1
    count1=count1+1
print(count,count1)

for i in new_list:
  if i > a:
    a_list.append(i)
print a_list

temp=a
for i in a:
    for j in b:
        if a[i]>b[i]:
            temp=a[i]
        else:
            temp == b[i]
            n_list.append(temp)
            print n_lis



def oddswap(a):
    s = list(a)
    for c in range(0,len(s),2):
        t=s[c]
        s[c]=s[c+1]
        s[c+1]=t

    return "".join(s)




oddswap(a)"""


lst = [
    ("a", ['8', '0']),
    ("a", ['7', '0b']),
    ("a", ['7', '0']),
    ("a", ['6', '0b']),
    ("a", ['6', '01']),
]

def keyfunc(t):
    a = [chr(ord(c) - 48) if 'a' <= c <= 'i' else c for c in ''.join(t[1])]
    return int(''.join(a))

new_lst = sorted(lst, key=keyfunc)
for row in new_lst:
    print(row)