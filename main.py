print("=== CLI Utility Toolbox ===")

while True:
    print("\nPlease select an option...")
    print("1. Hello World")
    print("2. Quit")
    
    choice = int(input("\nCommand: "))
    
    if choice == 1:
        print("Hello, World!")
    elif choice == 2:
        break
