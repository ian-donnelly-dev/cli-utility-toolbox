import hashlib
import string
import secrets

def get_valid_input(prompt, validator):
    while True:
        try:
            user_input = input(prompt)
            return validator(user_input)
        except ValueError as e:
            print(f"{str(e)}\n(You can also press Ctrl+C to return to main menu)\n")

while True:
    print("\n=== CLI Utility Toolbox ===\n")
    print("1. Hash Generator")
    print("2. Password Generator")
    print("3. Help")
    print("4. Quit\n")
    
    def validate_menu_choice(value):
        choice = int(value)
        if choice < 1 or choice > 4:
            raise ValueError("Invalid choice. Please enter 1-4.")
        return choice
    
    try:
        choice = get_valid_input("Enter choice: ", validate_menu_choice)
    except KeyboardInterrupt:
        print("\n\nBye-bye now!\n")
        break
    
    try:
        if choice == 1:
            print("\n=== Hash Generator ===\n")
            text_to_hash = input("Enter text to hash: ")
            
            md5_hash = hashlib.md5(text_to_hash.encode()).hexdigest()
            sha256_hash = hashlib.sha256(text_to_hash.encode()).hexdigest()
            
            print(f"\nMD5:    {md5_hash}")
            print(f"SHA256: {sha256_hash}")
            
            input("\nPress Enter to return to menu...")
            
        elif choice == 2:
            print("\n=== Password Generator ===\n")
            
            def validate_password_length(value):
                length = int(value)
                if length < 12 or length > 64:
                    raise ValueError("Length must be between 12 and 64.")
                return length
            
            length = get_valid_input("Enter password length (12-64): ", validate_password_length)
            
            characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
            password = ''.join(secrets.choice(characters) for _ in range(length))
            
            print(f"\nGenerated password: {password}")
            print("\nNote: Password is not saved. Copy it now!")
            input("Press Enter to return to menu...")
            
        elif choice == 3:
            print("\n=== Help ===\n")
            print("Available Tools:\n")
            print("1. Hash Generator")
            print("   Generate MD5 and SHA256 hashes for any text.")
            print("   Use this to verify file integrity or create checksums.\n")
            print("2. Password Generator")
            print("   Create secure random passwords between 12-64 characters.")
            print("   Passwords include uppercase, lowercase, numbers, and symbols.\n")
            print("Navigation:")
            print("- Enter the number of your choice at the main menu")
            print("- Press Enter to return to menu after using a tool")
            print("- Press Ctrl+C in a submenu to return to the main menu")
            print("- Press Ctrl+C at the main menu to quit the program")
            print("- Select option 4 to quit the program")
            
            input("\nPress Enter to return to menu...")
            
        elif choice == 4:
            print("\nBye-bye now!\n")
            break
            
    except KeyboardInterrupt:
        print("\n\nReturning to main menu...")
        continue
