# Kush Peter
# 202103103510506
# B.Tech CSE

class base:
    def display(self):
        print("i am base class")

class derive(base):
    def display(self):
        print("i am derive class")
        super().display()

ob=derive()
ob.display()
