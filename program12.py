# Kush Peter
# 202103103510506
# B.Tech CSE

class student:
    std_name = None
    std_age = None
    std_branch = None
    std_city = None
    def get_data(self, name, age, branch, city):
        self.std_name = name
        self.std_age = age
        self.std_branch = branch
        self.std_city = city
    def display(self):
        print("Name:", self.std_name, "\nAge:", self.std_age, "\nBranch:", self.std_branch, "\nCity:", self.std_city)
        
std_obj = student()
std_obj.get_data("Kush Peter", "18", "B.tech CSE", "Surat")
std_obj.display()