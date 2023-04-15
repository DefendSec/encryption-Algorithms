from random import randbytes


def runOtp(input, pad):
    return bytes(input[i] ^ pad[i] for i in range(0, len(input)))


# User input of pad

text = input("Pad in [H]ex or [t]ext: ").lower() in ["text", "t"]
format = "text" if text==True else "hex";

userInput = input(f"Enter pad ({format}). Leave empty to randomly generate one: ")
if len(userInput) == 0:
    pad = randbytes(256)
    print(f"(hex) {pad.hex()}")
else:
    try:
        if text:
            pad = bytes(userInput, 'utf-8')
            print(f"(text) {userInput}")
        else:
            pad = bytes.fromhex(userInput)
            print(f"(hex) {userInput}")
    except:
        print("Error reading pad")
        quit()


# Adjust pad to have bigger or same length as plain/cipher
def adjustLen():
    global pad

    length = len(pad)
    while len(pad) < len(clain):
        pad += pad[:length]





# Ask user if he wants to en-/decrypt a file

# When user wants to en-/decrypt file
if input("Do you want to en-/decrypt any [I]nput or a [f]ile? ").lower() in  ["f", "file"]:
    
    file = input("Enter filename or path ")
    try:
        with open(file, "rb") as f:
            clain = f.read()
    except:
        print("Error opening file")
        quit()

    output = runOtp(clain, pad)
    try:
        with open(file, "wb") as f:
            f.write(output)
    except:
        print("Error writing the file")
        quit()
    print(f"Sucessfully en-/decrypted file {file}")


# When user wants to en-/decrypt input
else:
    # User input of plain/cipher
    text = input("Plain/Cipher in [H]ex or [t]ext: ").lower() in ["text", "t"]
    format = "text" if text==True else "hex";

    userInput = input(f"Enter plain/cipher ({format}) ")

    try:
        if text:
            clain = bytes(userInput, 'utf-8')
        else:
            clain = bytes.fromhex(userInput)
    except:
        print("Error reading plain/cipher")
        quit()

    output = runOtp(clain, pad)
    try:
        print(f"(text){output.decode('utf-8')}\n(hex){output.hex()}")
    except:
        print(f"(hex){output.hex()}")




