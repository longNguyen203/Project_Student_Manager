with open("data.txt", 'r') as file:
    students = file.read()
    
# listStudent = students.split("\n")
dictionary = {}

listStudent = list(map(lambda x: x.split("-"), students.split("\n")))
for student1, student2 in zip(listStudent, students.split("\n")):
    dictionary[student1[0]] = student2
    
print(listStudent)