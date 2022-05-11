# Kush Peter
# 202103103510506
# B.Tech CSE

punc = [ "!", "]", "[", ".", ",", "{", "}", "(", ")" ]
fname = input("Enter filename: ")
f = open(fname, "r")
read = f.read()
for i in punc:
	read = read.replace(i, " ")

nowords = read.split(" ")
for i in range(nowords.count("")):
	nowords.remove("")
print(nowords)
print(len(nowords))
