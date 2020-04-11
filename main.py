import data
import encryption
from os import path


def main():
    r = data.get_data()
    r['decifrado'] = encryption.decrypt_text(r['numero_casas'], r['cifrado'])
    r['resumo_criptografico'] = encryption.convert_text_sha1(r['decifrado'])
    if not(path.exists('answer.json')):
        data.save_file(r)
    data.send_file()


if __name__ == "__main__":
   main()
