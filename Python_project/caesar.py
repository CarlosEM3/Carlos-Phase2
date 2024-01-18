#The goal of ceasar cipher 
# 1. Select some string value as your message. Label this string as “message”.
# 2. Select some numeric key value to encode your message. Label this value as `k`.
# 3. For each letter in “message”

# a. Shift each letter in your message `k` letters forward.
# b. If we go past the last letter in our alphabet (`z`), simply continue counting from
# the first letter (`a`).
import sys

#encrypting a message 
def encrypt(message, k):
message = 
encrypted_message = 
for letters in message:
    enletters + k
    return encrypted_message

character = 'a'
numer = ord(character)
print(numer)

def decrypt(message, k):
    return


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

character = 'a'
numer = ord(character)
print(numer)