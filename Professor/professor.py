from People import People


class Professor(People):
    def __init__(self, ID: str, ten: str, tuoi: int, gioiTinh: str, address: str, lecturer: str) -> None:
        super().__init__(ID, ten, tuoi, gioiTinh, address)
        
        self.lecturer = lecturer
        
    def addProfessor(self) -> None:
        print("*** Them Giang Vien")