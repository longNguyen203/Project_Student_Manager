from StudentV2.Student import Student
import os


class StudentManager:
    
    def frameField(self) -> None:
        print("{:<8}{:<25}{:<9}{:<6}{:<25}{:<10}".format("ID", "Ten", "NamSinh", "Khoa", "Major", "GPA"))
        print("-"*82)
            
    def list_Student(self) -> dict:
        with open("StudentV2\data2.txt", 'r') as file:
            students = file.read()
            
        # listStudent = students.split("\n")
        dictionary = {}

        listStudent = list(map(lambda x: x.split("-"), students.split("\n")))
        for student in listStudent:
            dictionary[student[0]] = student
            
        return dictionary
    
    def addStudent(self) -> None:
        id = input("-->ID: ")
        if id not in self.list_Student().keys():
            
            try:
                ten = input("-->Ten: ")
                namSinh = int(input("-->NamSinh: "))
                khoa = int(input("-->Khoa: "))
                major = input("-->Major: ")
                GPA = float(input("-->GPA: "))
                
            except ValueError:
                print("Loi! Dau vao khong hop le!!!!")
                
            try:
                with open("StudentV2\data2.txt", "a") as file:
                    file.write(f"{id}-{ten}-{namSinh}-{khoa}-{major}-{GPA}\n")
                    
                os.system('cls')
                print("*** Them Sinh Vien Thanh Cong ***")  
                
            except FileNotFoundError:
                print("File data2.txt khong ton tai")
            except UnboundLocalError:
                print("Loi!!!")  
            
        else:
            os.system('cls')
            print("*** Sinh vien da có trong Danh sach ***")
            
    def printStudent(self) -> None:
        self.frameField()
        dict_Student = self.list_Student() # Dict
        list_value = [value for value in dict_Student.values()] # List
        for index in range(len(list_value)-1):
            student = list_value[index]
            print("{:<8}{:<25}{:<9}{:<6}{:<25}{:<10}".format(student[0], student[1], student[2], student[3], student[4], student[5]))
        
                
    def deleteStudent(self) -> None:
        id = input("-->ID: ")
        if id in self.list_Student().keys():
            try:
                dict_Student = self.list_Student()
                with open("StudentV2\data2.txt", 'w') as file:
                    for key, value in dict_Student.copy().items():
                        if id != key: dict_Student[key] = "-".join(str(item) for item in value)
                        
                        else: dict_Student.pop(key)
                    file.writelines("\n".join(str(item) for item in dict_Student.values()))
                            
                os.system('cls')
                print("*** Xoa Thanh Cong ***")
                                
            except FileNotFoundError:
                print("File data2.txt khong ton tai")
                
        else: 
            os.system('cls')
            print("*** Khong ton tai Sinh Vien nay ***")
        
    def editStudent(self) -> None:
        id = input("-->ID: ")
        dict_Student = self.list_Student()
        if id in dict_Student.keys():
            try:
                ten = input("-->Ten: ")
                namSinh = int(input("-->NamSinh: "))
                khoa = int(input("-->Khoa: "))
                major = input("-->Major: ")
                GPA = float(input("-->GPA: "))
                
                dict_Student[id] = [id, ten, namSinh, khoa, major, GPA]
                
            except ValueError:
                print("Loi! Dau vao khong hop le!!!!")
            
            try:
                with open("StudentV2\data2.txt", 'w') as file:
                    for key, value in dict_Student.copy().items():
                        dict_Student[key] = "-".join(str(item) for item in value)
                    file.writelines("\n".join(str(item) for item in dict_Student.values()))
                    
                os.system('cls')
                print("*** Sua Thanh Cong ***")
            
            except FileNotFoundError:
                print("File data2.txt khong ton tai")
                
        else: 
            os.system('cls')
            print("*** Khong ton tai Sinh Vien nay ***")
    
    def findStudent(self) -> None:
        id = input("-->ID: ")
        if id in self.list_Student().keys():
            student = self.list_Student()[id]
            os.system('cls')
            self.frameField()
            print("{:<8}{:<25}{:<9}{:<6}{:<25}{:<10}".format(student[0], student[1], student[2], student[3], student[4], student[5]))
        else: 
            os.system('cls')
            print("*** Khong ton tai Sinh Vien nay ***")