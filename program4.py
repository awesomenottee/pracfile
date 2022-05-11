# Kush Peter
# 202103103510506
# B.Tech CSE

student={
    "name":"Kush",
    "age":18,
    "branch of student":"b tech"
}
updatestudent={
    "college":"uka"
}
print(student)
student.update(updatestudent)
print(student)

student.pop("name")
print(student)

student.copy()
print(student)

print(student.get("age"))

print(student.items())

print(student.keys())

print(student.values())

student.pop("age")
print(student)

student.clear()
print(student)
