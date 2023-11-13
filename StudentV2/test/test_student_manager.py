import pytest
from unittest.mock import patch, mock_open
from StudentV2.StudentManager import StudentManager

def test_addStudent_write_to_file():
    manager = StudentManager()

    # Sử dụng patch để giả mạo hàm input và mở file
    with patch('builtins.input', side_effect=['1', 'John Doe', 1990, 1, 'Computer Science', 3.5]), \
        patch('builtins.open', mock_open()) as mock_file:
        manager.addStudent()

    # Kiểm tra xem file đã được mở và ghi đúng dữ liệu không
    mock_file.assert_called_once_with("StudentV2\data2.txt", "a")
    mock_file().write.assert_called_once_with("1-John Doe-1990-1-Computer Science-3.5\n")

# Thêm các bài kiểm thử khác nếu cần thiết