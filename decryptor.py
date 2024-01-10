enc_message = input("Enter the encrypted message: \t")
key = int(input("Enter the key: \t"))
shift = input("\nShift to: \nL. Left \nR. Right \n\t\t")

orig_message = ""
print(f"The encrypted message is: \t{enc_message}")

for char in enc_message:
    if char.isalpha():
        char_decode = ord(char)
        if shift == "L":
            char_decode += key
        else:
            char_decode -= key

        if char.isupper():
            if char_decode > ord('Z'):
                char_decode -= 26
            if char_decode < ord('A'):
                char_decode += 26
        else:
            if char_decode > ord('z'):
                char_decode -= 26
            if char_decode < ord('a'):
                char_decode += 26
        orig_message += chr(char_decode)
    else:
        orig_message += char

print("")
print(f"The encrypted message is: \t{enc_message}")
print(f"\nThe decrypted message is: {orig_message}")
