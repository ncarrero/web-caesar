def alphabet_position(letter):
    lowercaseAlphabet = "abcdefghijklmnopqrstuvwxyz"
    uppercaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter in lowercaseAlphabet:
        return lowercaseAlphabet.index(letter)
    if letter in uppercaseAlphabet:
        return uppercaseAlphabet.index(letter)

def rotate_character(char, rot):
    lowercaseAlphabet = "abcdefghijklmnopqrstuvwxyz"
    uppercaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if char in lowercaseAlphabet:
        new_alphabet_position = alphabet_position(char) + rot
        if new_alphabet_position < 26:
            new_char = lowercaseAlphabet[new_alphabet_position]
        else:
            new_char = lowercaseAlphabet[new_alphabet_position % 26]
        return new_char
    else:
        if char in uppercaseAlphabet:
            new_alphabet_position = alphabet_position(char) + rot
            if new_alphabet_position < 26:
                new_char = uppercaseAlphabet[new_alphabet_position]
            else:
                new_char = uppercaseAlphabet[new_alphabet_position % 26]
            return new_char
        else:
            return char

def encrypt(text, rot):
    new_text = ""
    for i in text:
        new_text = new_text + rotate_character(i, rot)
    return new_text