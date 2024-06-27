alphabet = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '*'
}

def crypt(message, dictionary = alphabet):
    text = ""
    for i in message:
        for j in dictionary: 
            if i == j: 
                text = text + " " + dictionary[i]
                #print(alphabet[i], end=" ")
    return text
"""
def crypt(message, dictionary=alphabet): # AI sugesstion
    return ' '.join(dictionary.get(char, char) for char in message.upper())
"""
def encrypt(message, dictionary = alphabet):
    reversed_dict = {value: key for key, value in dictionary.items()}
    message_parts = message.split()
    text = ""
    for i in message_parts:
        for j in reversed_dict:
            if i == j: 
                text = text + reversed_dict[i]
    return text

print("---------WELCOME-TO-MORESE-CODE----------")
while True:
    option = input("Do you want to crypt (c), encrypt (e) or exit (x) -> ")
    if option == "c":
        real_message = input("Insert message (e.g. sos 115): ").upper()
        print("Your crypted message is:",crypt(real_message), "\n")
    elif option == "e":
        morse_message = input("Insert message (e.g. ... --- ...): ")
        print("Your encrypted message is:",encrypt(morse_message), "\n")
    elif option == "x":
        print("Thank you, see you soon!\n")
        exit()
    else: print("Bad input! Try it again.\n")

