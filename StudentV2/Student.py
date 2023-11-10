class Student:
    
    def __init__(self, id: str, ten: str, namSinh: int, khoa: int, major: str, GPA: float) -> None:
        self.id = id
        self.ten = ten
        self.namSinh = namSinh
        self.khoa = khoa
        self.major = major
        self.GPA = GPA
        
    def setId(self, id: str) -> None:
        self.id = id
        
    def setTen(self, ten: str) -> None:
        self.ten = ten
        
    def setNamSinh(self, namSinh: int) -> None:
        self.namSinh = namSinh
        
    def setKhoa(self, khoa: int) -> None:
        self.khoa = khoa
        
    def setMajor(self, major: str) -> None:
        self.major = major
        
    def setGPA(self, GPA: float) -> None:
        self.GPA = GPA
        
    def getId(self) -> str:
        return self.id
    
    def getTen(self) -> str:
        return self.ten
    
    def getNamSinh(self) -> int:
        return self.namSinh
    
    def getKhoa(self) -> int:
        return self.khoa
    
    def getMajor(self) -> str:
        return self.major
    
    def getGPA(self) -> float:
        return self.GPA
    
    def showProfile(self) -> None:
        print("{:<8}{:<25}{:<9}{:<6}{:<25}{:<10}".format(self.getId(), self.getTen(), self.getNamSinh(), self.getKhoa(), self.getMajor(), self.getGPA()))
        
