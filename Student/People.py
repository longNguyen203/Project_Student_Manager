class People:
    def __init__(self, ID: str, ten: str, tuoi: int, gioiTinh: str, address: str) -> None:
        self.ID = ID
        self.ten = ten
        self.tuoi = tuoi
        self.gioiTinh = gioiTinh
        self.address = address
        
    def __str__(self) -> str:
        return f"ID: {self.ID}, Ten: {self.ten}, Tuoi: {self.tuoi}, GioiTinh: {self.gioiTinh}, Address: {self.address}"
    
    