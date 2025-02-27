import random
import string

def generate_password():
    print("Password Generator")
    
    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("Password length should be at least 4 for better security.")
            return
        
        # Character sets
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special_chars = string.punctuation

        # Ask user for complexity preferences
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        # Ensure at least one category is selected
        if not (use_upper or use_digits or use_special):
            print("At least one character type (uppercase, numbers, or special characters) must be included.")
            return

        # Build the character pool
        char_pool = lowercase
        if use_upper:
            char_pool += uppercase
        if use_digits:
            char_pool += digits
        if use_special:
            char_pool += special_chars

        # Ensure password contains at least one of each selected type
        password = []
        if use_upper:
            password.append(random.choice(uppercase))
        if use_digits:
            password.append(random.choice(digits))
        if use_special:
            password.append(random.choice(special_chars))
        
        # Fill the rest with random choices from the pool
        password += random.choices(char_pool, k=length - len(password))

        # Shuffle to avoid predictable patterns
        random.shuffle(password)

        # Convert list to string
        final_password = ''.join(password)
        print(f"Generated Password: {final_password}")

    except ValueError:
        print("Invalid input! Please enter a valid number for password length.")

# Run the password generator
generate_password()
