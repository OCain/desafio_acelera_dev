import hashlib as hash

ALPHABET = [chr(x) for x in range(ord('a'), ord('z') + 1)]


def generate_decryption_dict(nr_places):
    encryption_alphabet = ALPHABET[nr_places:] + ALPHABET[0:nr_places]
    return dict(zip(encryption_alphabet, ALPHABET))


def decrypt_text(nr_places, text):
    decrypted_text = ""
    decryption_dict = generate_decryption_dict(nr_places)
    for letter in text:
        if letter in ALPHABET:
            decrypted_text += decryption_dict[letter]
        else:
            decrypted_text += letter
    return decrypted_text


def convert_text_sha1(text):
    result = hash.sha1(str.encode(text))
    return result.hexdigest()
