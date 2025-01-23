import tkinter as tk
import random

def shift_text(text, shift_by):
    """Mã hóa văn bản bằng cách shift ký tự sang phải và xen thêm ký tự đặc biệt."""
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    shifted_text = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr(start + (ord(char) - start + shift_by) % 26)
            shifted_text += shifted_char
            # Xen phụ âm bất kỳ sau nguyên âm, nguyên âm bất kỳ sau phụ âm
            if shifted_char.lower() in vowels:
                shifted_text += random.choice(consonants)
            else:
                shifted_text += random.choice(vowels)
        else:
            shifted_text += char
    return shifted_text

def encode_text():
    """Lấy văn bản từ ô nhập và hiển thị văn bản mã hóa."""
    text = input_text.get()
    shift_by = int(shift_value.get())
    encoded = shift_text(text, shift_by)
    print(encoded)
    output_label.config(text=f"Kết quả mã hóa: {encoded}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ứng dụng Mã hóa Văn bản")
root.geometry("400x300")

# Nhãn và ô nhập văn bản
input_label = tk.Label(root, text="Nhập văn bản:", font=("Arial", 12))
input_label.pack(pady=5)
input_text = tk.Entry(root, font=("Arial", 12), width=30)
input_text.pack(pady=5)

# Nhãn và ô nhập giá trị shift
shift_label = tk.Label(root, text="Nhập giá trị shift:", font=("Arial", 12))
shift_label.pack(pady=5)
shift_value = tk.Entry(root, font=("Arial", 12), width=10)
shift_value.pack(pady=5)

# Nút mã hóa
encode_button = tk.Button(root, text="Mã hóa", command=encode_text, font=("Arial", 12))
encode_button.pack(pady=10)

# Nhãn hiển thị kết quả
output_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
output_label.pack(pady=20)

# Vòng lặp chính để chạy ứng dụng
root.mainloop()
