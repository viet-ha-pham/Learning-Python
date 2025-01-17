import random

def get_computer_choice():
    """Lựa chọn ngẫu nhiên cho máy."""
    choices = ["kéo", "búa", "bao"]
    return random.choice(choices)

def get_user_choice():
    """Nhận lựa chọn từ người chơi."""
    while True:
        print("\nHãy chọn:")
        print("1 - Kéo")
        print("2 - Búa")
        print("3 - Bao")
        choice = input("Nhập số tương ứng (hoặc 'q' để thoát): ").strip().lower()
        if choice == '1':
            return "kéo"
        elif choice == '2':
            return "búa"
        elif choice == '3':
            return "bao"
        elif choice == 'q':
            return "thoát"
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")

def determine_winner(user, computer):
    """Xác định người chiến thắng."""
    if user == computer:
        return "Hòa!"
    elif (user == "kéo" and computer == "bao") or \
         (user == "búa" and computer == "kéo") or \
         (user == "bao" and computer == "búa"):
        return "Bạn thắng!"
    else:
        return "Máy thắng!"


if __name__ == "__main__":
    print("Chào mừng đến với trò chơi Oẳn Tù Tì!")
    while True:
        user_choice = get_user_choice()
        if user_choice == "thoát":
            print("Cảm ơn bạn đã chơi. Tạm biệt!")
            break
        computer_choice = get_computer_choice()
        print(f"\nBạn chọn: {user_choice}")
        print(f"Máy chọn: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(f"Kết quả: {result}")
