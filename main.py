from cryptography.fernet import Fernet

def gener_key(file_path: str = 'data/key.key'):
    key = Fernet.generate_key()

    with open(file_path, 'wb') as _:
        _.write(key)

def get_key(file_path: str = 'data/key.key'):
    with open(file_path, 'rb') as _:
        return _.read()

def encrypt_file(
        key_path:str = 'data/key.key',
        src:str = 'data/file.txt',
        desc:str = 'data/enc_file.txt', 
        ):
    fernet = Fernet(get_key(key_path))
    with open(src, 'rb') as _:
        data = _.read()

    enc_data = fernet.encrypt(data)

    with open(desc, 'wb') as _:
        _.write(enc_data)

def decrypt_file(
        key_path:str = 'data/key.key',
        src:str = 'data/enc_file.txt',
        desc:str = 'data/dec_file.txt', 
        ):
    fernet = Fernet(get_key(key_path))

    with open(src, 'rb') as _:
        enc_data = _.read()

    dec_data = fernet.decrypt(enc_data)

    with open(desc, 'wb') as _:
        _.write(dec_data)

def main():
    key_path = 'data/my_key.key'
    data_path = 'data/file.csv'
    enc_data_path = 'data/encfile.csv'
    dec_data_path = 'data/decfile.csv'

    gener_key(key_path)
    encrypt_file(key_path, data_path, enc_data_path)
    decrypt_file(key_path, enc_data_path, dec_data_path)

if __name__ == "__main__":
    main()
