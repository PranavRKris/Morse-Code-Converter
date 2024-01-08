morseDict = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        " ": "/"
    }
def decrypt(word):
    converted = ""
    for i in word.lower():
        converted += morseDict[i] + " "
    print(converted)
    return(converted)

def encrypt(word):
    word += " "
    decipher = ''
    citext = ''
    try:
        for letter in word:
            if letter != ' ':
                i = 0
                citext += letter
            else:
                i += 1
                if i == 2:
                    decipher += ' '
                else:
                    decipher += list(morseDict.keys())[list(morseDict.values()).index(citext)]
                    citext = ''
        return decipher
    except:
        return "!!!Incorrect Morse code"