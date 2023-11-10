from StudentV2.StudentManager import StudentManager
import os

def Menu():
    print("1. Them Sinh vien")
    print("2. Xem Danh sach Sinh vien")
    print("3. Xoa Sinh Vien")
    print("4. Sua Sinh Vien")
    print("5. Tim Sinh Vien")
    print("0. Return Home")

def main() -> None:
    student = StudentManager()
    Menu()
    while True:
        select = (input("Choose select: "))
        os.system('cls')
        if select == "1":
            student.addStudent()
        elif select == "2":
            student.printStudent()
        elif select == "3":
            student.deleteStudent()
        # elif select == 4:
        #     student.editStudent()
        # elif select == 5:
        #     student.findStudent()
        elif select == "0":
            Menu()
        else:
            print("Thoat Thành Cong")
            break

if __name__ == "__main__":
    main()