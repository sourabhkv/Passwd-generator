import random
import string
import pyperclip  # Install this library using: pip install pyperclip

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_to_file(passwords):
    filename = input("Enter a filename to save passwords (press Enter to skip): ")
    if filename:
        with open(filename, 'w') as file:
            file.write("\n".join(passwords))
        print(f"Passwords saved to {filename}")

def main():
    print("🔐 Welcome to the Password Generator! 🔐")

    try:
        password_length = int(input("How long do you want your password to be? (default is 12): ") or 12)
        num_passwords = int(input("How many passwords do you want to generate? (default is 1): ") or 1)

        if password_length <= 0 or num_passwords <= 0:
            print("Please enter valid values for password length and number of passwords.")
            return

        print("\nGenerating Passwords...\n")

        passwords = []
        for _ in range(num_passwords):
            password = generate_password(password_length)
            passwords.append(password)
            print(f"🔒 Password: {password}")

        save_to_file(passwords)

        copy_to_clipboard = input("Do you want to copy a password to the clipboard? (yes/no): ").lower()
        if copy_to_clipboard == 'yes':
            index = int(input("Enter the index of the password you want to copy (1, 2, ...): ")) - 1
            if 0 <= index < num_passwords:
                pyperclip.copy(passwords[index])
                print("Password copied to clipboard!")
            else:
                print("Invalid index. Clipboard operation aborted.")

    except ValueError:
        print("Invalid input. Please enter valid numerical values.")

if __name__ == "__main__":
    main()
