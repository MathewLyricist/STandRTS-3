import random
import string

def generate_password(length=12):
    letters = string.ascii_letters
    digits = string.digits
    special_characters = "@#%_^!)(*?"

    all_characters = letters + digits + special_characters

    password = ''.join(random.sample(all_characters, length))

    return password

if __name__ == "__main__":
    generated_password = generate_password()
    print("Сгенерированный пароль:", generated_password)
