while True:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = []
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(text, shift, direction):
        if direction == "encode":
            for i in text:
                if i == " ":
                    result.append(" ")
                else:
                    letterindex = alphabet.index(i)
                    while letterindex + shift > 25:
                        letterindex -= 26
                    result.append(alphabet[letterindex + shift])
        else:
            for i in text:
                if i == " ":
                    result.append(" ")
                else:
                    letterindex = alphabet.index(i)
                    while letterindex-shift < 0:
                        letterindex += 26
                    result.append(alphabet[letterindex - shift])
        return "".join(result)    


    print(f"Your {direction}d text is {caesar(text, shift, direction)}.")
    if input("Do you want to encode/decode again? Y/N ") == "N":
        break
    
        
    