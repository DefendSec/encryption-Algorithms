from random import randbytes



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


# Adjust pad to have bigger or same length as plain/cipher
length = len(pad)
while len(pad) < len(clain):
    pad += pad[:length]




output = bytes(clain[i] ^ pad[i] for i in range(0, len(clain)))
try:
    print(f"(text){output.decode('utf-8')}\n(hex){output.hex()}")
except:
    print(f"(hex){output.hex()}")