import random
import string

def generate_alphanumeric_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Введите длину пароля: "))
    new_password = generate_alphanumeric_password(password_length)
    print(f"Сгенерированный пароль: {new_password}")
