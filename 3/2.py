import pprint

pp = pprint.PrettyPrinter(indent=4)
ALPHABET = "abcdefghijklmnopqrstuvwxyz"



def generate_caesar_key(shift):
    encryption_key = {letter: ALPHABET[(ALPHABET.index(letter) + shift) % len(ALPHABET)] for letter in ALPHABET}
    decryption_key = {letter: ALPHABET[(ALPHABET.index(letter) - shift) % len(ALPHABET)] for letter in ALPHABET}
    return encryption_key, decryption_key


shift = 3
encryption_key, decryption_key = generate_caesar_key(shift)
pp.pprint(encryption_key)
pp.pprint(decryption_key)
