# -------------------------------
# CAESAR CIPHER FUNCTIONS
# -------------------------------
def caesar_decode(message, offset):
    decoded_message = ""
    for char in message:
        if char.isalpha():
            shift = ord(char) - offset
            if char.isupper():
                decoded_message += chr((shift - 65) % 26 + 65)
            else:
                decoded_message += chr((shift - 97) % 26 + 97)
        else:
            decoded_message += char
    return decoded_message

def caesar_encode(message, offset):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            shift = ord(char) + offset
            if char.isupper():
                encoded_message += chr((shift - 65) % 26 + 65)
            else:
                encoded_message += chr((shift - 97) % 26 + 97)
        else:
            encoded_message += char
    return encoded_message

# -------------------------------
# TASK 1: Decode Vishal's first message
# -------------------------------
message1 = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
offset = 10
decoded1 = caesar_decode(message1, offset)
print("Decoded Message 1:\n", decoded1, "\n")

# -------------------------------
# TASK 2: Encode your response
# -------------------------------
my_message = "Hello Vishal! I decoded your message."
encoded_response = caesar_encode(my_message, offset)
print("Encoded Response:\n", encoded_response, "\n")

# -------------------------------
# TASK 3: Decode next two messages
# -------------------------------
message2 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
message3 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

decoded2 = caesar_decode(message2, offset)
decoded3 = caesar_decode(message3, offset)

print("Decoded Message 2:\n", decoded2)
print("Decoded Message 3:\n", decoded3, "\n")

# -------------------------------
# TASK 4: Brute-force unknown Caesar shift
# -------------------------------
message4 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

print("Brute-force Caesar Cipher Decoding:\n")
for shift in range(1, 26):
    decoded_try = caesar_decode(message4, shift)
    # Print only readable outputs (simple filter)
    if "the" in decoded_try.lower():
        print(f"Shift {shift}: {decoded_try}\n")

# -------------------------------
# VIGENÈRE CIPHER FUNCTIONS
# -------------------------------
def vigenere_encode(message, keyword):
    encoded = ""
    keyword = keyword.lower()
    keyword_repeat = ""
    
    i = 0
    for char in message:
        if char.isalpha():
            keyword_repeat += keyword[i % len(keyword)]
            i += 1
        else:
            keyword_repeat += char
    
    for c, k in zip(message, keyword_repeat):
        if c.isalpha():
            shift = ord(k) - ord('a')
            if c.isupper():
                encoded += chr((ord(c) + shift - 65) % 26 + 65)
            else:
                encoded += chr((ord(c) + shift - 97) % 26 + 97)
        else:
            encoded += c
    return encoded

def vigenere_decode(cipher_text, keyword):
    decoded = ""
    keyword = keyword.lower()
    keyword_repeat = ""
    
    i = 0
    for char in cipher_text:
        if char.isalpha():
            keyword_repeat += keyword[i % len(keyword)]
            i += 1
        else:
            keyword_repeat += char
    
    for c, k in zip(cipher_text, keyword_repeat):
        if c.isalpha():
            shift = ord(k) - ord('a')
            if c.isupper():
                decoded += chr((ord(c) - shift - 65) % 26 + 65)
            else:
                decoded += chr((ord(c) - shift - 97) % 26 + 97)
        else:
            decoded += c
    return decoded

# -------------------------------
# TASK 5: Decode Vigenère cipher message
# -------------------------------
cipher_message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"
keyword = "friends"

decoded_vigenere = vigenere_decode(cipher_message, keyword)
print("Decoded Vigenère Message:\n", decoded_vigenere, "\n")

# -------------------------------
# TASK 6: Encode a Vigenère cipher message
# -------------------------------
my_secret_message = "Hello Vishal! You are an amazing pen pal."
encoded_vigenere = vigenere_encode(my_secret_message, keyword)
print("Encoded Vigenère Message:\n", encoded_vigenere)

# Decode to check correctness
decoded_check = vigenere_decode(encoded_vigenere, keyword)
print("Decoded Back:\n", decoded_check)
