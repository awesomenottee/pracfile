# Kush Peter
# 202103103510506
# B.Tech CSE


def counting(combi):
    for i in range(len(combi)):
        n=combi.count(combi[i])
        

        print("The element ",combi[i],"repeats",n,"times")



l=[]
m=int(input("Enter the number in list 1: "))
for i in range(m):
    l.append(int(input("enter the value = ")))
print(l)

lst=[]
n=int(input("Enter the number in list 2: "))
for i in range(n):
    lst.append(int(input("enter the value = ")))
print(lst)

combi=l+lst
print(combi)
print(counting(combi))




