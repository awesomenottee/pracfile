# Kush Peter
# 202103103510506
# B.Tech CSE

n=int(input("enter number of input: "))
list1=[]
for i in range(n):
    num=int(input("enter number: "))
    list1.append(num)
print(list1)

def minmax(list1):
    max=0
    for i in range(len(list1)):
    
      if list1[i]>max:
        max=list1[i]
    
    min=list1[0]
    for i in range(len(list1)):
        if list1[i]<min:
            min=list1[i]

    return min,max

x,y=minmax(list1)
print("min is %d and max is %d"%(x,y))