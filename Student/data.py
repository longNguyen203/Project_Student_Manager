with open("data.txt", "r") as file:
    students = file.read()
    
# listStudent = students.split("\n")
dictionary = {}

listStudent = list(map(lambda x: x.split("-"), students.split("\n")))
for student in listStudent:
    dictionary[student[0]] = student
    
print(dictionary)