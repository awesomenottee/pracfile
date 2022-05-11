# Kush Peter
# 202103103510506
# B.Tech CSE

while(True):
	try:
		number=input("This program will throw exception and quit while entering anything other than integer: ")
		int(number)
	except ValueError:
		print("Enter a valid number, Press ctrl+c to quit the loop")
		break