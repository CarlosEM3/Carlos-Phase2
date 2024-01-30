import sys

#encrypting message

#making code readable and maintainable by labeling ASCII values
ASCII_CHAR_END = 90
ASCII_ALPHA_RANGE = 26



def encrypt(message,k):
    encrypt_message = ""
    for letters in message.upper():
        if letters.isalpha():
            let_code = ord(letters)
            new_let_code = let_code + k 
            if new_let_code > ASCII_CHAR_END:
                new_let_code -= ASCII_ALPHA_RANGE 
                
            encrypt_le = chr(new_let_code)
            encrypt_message += encrypt_le
        else:
            encrypt_message += letters
    print(encrypt_message)



encrypt("Te Amo Mi John", 7)