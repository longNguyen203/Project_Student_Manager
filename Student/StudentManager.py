from Student.Student import Student


class StudentManager:
    
    list_Student: list[Student] = []
    
    def frameField(self) -> None:
        print("{:<8}{:<25}{:<9}{:<6}{:<25}{:<10}".format("ID", "Ten", "NamSinh", "Khoa", "Major", "GPA"))
    
    def addStudent(self) -> None:
        
        print("*** Them Sinh Vien ***")
        
        try:
            id = input("-->ID: ")
            ten = input("-->Ten: ")
            namSinh = int(input("-->NamSinh: "))
            khoa = int(input("-->Khoa: "))
            major = input("-->Major: ")
            GPA = float(input("-->GPA: "))
        except ValueError:
            print("Loi! Dau vao khong hop le!!!!")
        
        StudentManager.list_Student.append(Student(id, ten, namSinh, khoa, major, GPA))
        
    def printStudent(self) -> None:
        self.frameField()
        for student in StudentManager.list_Student:
            print(student.showProfile())
            
    def deleteStudent(self) -> None:
        id = input("-->ID: ")
        for student in StudentManager.list_Student:
            if id == student.getId():
                StudentManager.list_Student.remove(student)
                print("*** Xoa Thanh Cong ***")
                return 
        print("*** Khong Ton Tai Sinh Vien Nay ***")
        
    def editStudent(self) -> None:
        id = input("-->ID: ")
        for student in StudentManager.list_Student:
            if id == student.getId():
                try:
                    student.setTen(input("-->Sua Ten: "))
                    student.setNamSinh(int(input("-->Sua NamSinh: ")))
                    student.setKhoa(int(input("-->Sua Khoa: ")))
                    student.setMajor(input("-->Sua Major: "))
                    student.setGPA(float(input("-->Sua GPA: ")))
                    print("*** Sua Thanh Cong ***")
                     
                except ValueError:
                    print("Loi! Dau vao khong hop le!!!!")
                else:
                    return
        print("*** Khong Ton Tai Sinh Vien Nay ***")
        
    def findStudent(self) -> None:
        id = input("-->ID: ")
        for student in StudentManager.list_Student:
            if id == student.getId():
                self.frameField()
                student.showProfile()
                return 
        print("*** Khong Ton Tai Sinh Vien Nay ***")
                
                
            

    