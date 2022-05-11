# Kush Peter
# 202103103510506
# B.Tech CSE

src = input("Name of source file: ")
des = input("Name of destination file: ")

src_op = open(src, "r")
des_op = open(des, "r")

des_op.write(src.read())

src_op.close()
des_op.close()
print("Operation Successful !")