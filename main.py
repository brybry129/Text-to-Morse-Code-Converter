# dot: ·

morse_dict = {
    "A": "· -",
    "B": "- · · ·",
    "C": "- · - ·",
    "D": "- · ·",
    "E": "·",
    "F": "· · - ·",
    "G": "- - ·",
    "H": "· · · ·",
    "I": "· ·",
    "J": "· - - -",
    "K": "- · -",
    "L": "· - · ·",
    "M": "- -",
    "N": "- ·",
    "O": "- - -",
    "P": "· - - ·",
    "Q": "- - · -",
    "R": "· - ·",
    "S": "· · ·",
    "T": "-",
    "U": "· · -",
    "V": "· · · -",
    "W": "· - -",
    "X": "- · · -",
    "Y": "- · - -",
    "Z": "- - · ·",
    "0": "- - - - -",
    "1": "· - - - -",
    "2": "· · - - -",
    "3": "· · · - -",
    "4": "· · · · -",
    "5": "· · · · ·",
    "6": "- · · · ·",
    "7": "- - · · ·",
    "8": "- - - · ·",
    "9": "- - - - ·",
    " ": "       "
}


def convert_morse(text):
    output = ""
    for i in text:
        try:
            output += morse_dict.get(i)
        except TypeError:
            output = "Text includes invalid characters, please only include letters and numbers."
            break
        output += "   "
    return output


if __name__ == '__main__':
    stop = False
    while not stop:
        print("Morse Converter\n")
        phrase = input("Please type text to convert to morse code.\n")
        if phrase == "exit":
            stop = True
        else:
            print(convert_morse(phrase.upper()))
