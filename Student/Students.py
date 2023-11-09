from People import People


class Students(People):
    
    total_Student = 0
    
    def __init__(self, ID: str="", ten: str="", tuoi: int=9, gioiTinh: str="", address: str="", major: str="") -> None:
        super().__init__(ID, ten, tuoi, gioiTinh, address)
        
        self.major = major
        
    def findStudent(self) -> None:
        pass
    
    @classmethod    
    def addStudent(self) -> None:
        print("*** Them Sinh Vien ***")
        
        try:
            ID: str = input(str("ID: "))
            Ten: str = input(str("Ten: "))
            Tuoi: int = input(str("Tuoi: "))
            GioiTinh: str = input(str("GioiTinh: "))
            Address: str = input(str("Address: "))
            Major: str = input(str("Major: "))
        
            with open("data.txt", "a") as file:
                file.write(f"{ID}-{Ten}-{Tuoi}-{GioiTinh}-{Address}-{Major}\n")
                
        except ValueError:
            print("Loi Gia trị")
            
        finally:
            print("Them thanh cong")
            
    @classmethod
    def deleteStudent(self, ID: str):
        
        
            
            
