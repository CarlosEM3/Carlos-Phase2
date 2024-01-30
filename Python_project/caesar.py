#Creating a Caesar Cipher 

import sys

#Making code readable and maintainable by labeling ASCII numbers
ASCII_CHAR_END = 90
ASCII_ALPHA_RANGE = 26
ASCII_CHAR_START = ord("A")


# function for encrypting a message 
def encrypt(message, k):
    #assigning variable to string where we can add back our encrypted message  
    encrypted_message = ""
    #for loop to run through each letter of the message, making them all cap to use same ASCII numbering  
    for letters in message.upper():
        #only shifting letters, not space or punctuations 
        if letters.isalpha():
            #converting letters to their ASCII number
            letter_code = ord(letters)
            #Shifting letter code 
            new_let_code = letter_code + k
            #Making sure our shift only happens within the ASCII alphabetical range
            if new_let_code > ASCII_CHAR_END:
                new_let_code -= ASCII_ALPHA_RANGE
            #Assigning letters to shifted letter numbers 
            encrypt_le = chr(new_let_code)
            #adding new characters back to initial variable 
            encrypted_message += encrypt_le
        #if NOT alphabetical, then just adding back to encrypted message 
        else: 
            encrypted_message += letters
    return encrypted_message

encrypt("Hello World",7) 

#function decrypting message 
def decrypt(encrypted, k):
    decrypted_message = ""
    for letters in encrypted:
        if letters.isalpha():
            enc_let_code = ord(letters)
            decrypt_let_code = enc_let_code - k 
            if decrypt_let_code < ASCII_CHAR_START:
                decrypt_let_code += ASCII_ALPHA_RANGE
            decrypted_let = chr(decrypt_let_code)
            decrypted_message += decrypted_let
        else:
            decrypted_message += letters
    return decrypted_message

decrypt("OLSSV DVYSK",7) 



if __name__ == "__main__":
    # take in first arg as word
    message = sys.argv[1]
    # take in second arg as int key
    key = int(sys.argv[2])

    # encrypt your word
    encrypted = encrypt(message, key)

    # decrypt your encrypted word
    decrypted = decrypt(encrypted, key)

    print("Your encrypted word is", encrypted)
    print("Your decrypted word is", decrypted)

