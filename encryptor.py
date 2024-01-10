#my original code for the Caesar Cipher

message = input("Enter the message to be encrypted:\t")
key = int(input("Enter the key:\t"))

#message = message.split()

print(f"The original message: {message}")

enc_message = ""

for char in message:
    if char.isalpha():
        char_code = ord(char)#change the character to Unicode
        char_code = char_code + key#add the shift. Shift to the right

        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26

            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26
        enc_message += chr(char_code)
    else:
        enc_message += char

print("")
print(f"The encrypted message is: {enc_message}" )
        

    

