# Kush Peter
# 202103103510506
# B.Tech CSE

file = input("Enter Filename: ")
file = open(file, "r")
lines = file.readlines()

opr = input("Enter Number of lines to be printed: ")

for i in range(int(opr)+1):
	print(lines[i])