def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # alphabetic check
            shifted = ord(char) + shift  # Character shift
            if char.islower():  # lowercase or not
                if shifted > ord('z'):  # wrapping
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():  # uppercase or not
                if shifted > ord('Z'):  # Wrapping
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)  # Convert to character and add to the encrypted text
        else:
            encrypted_text += char  # not alphabetic, no change required
    return encrypted_text
