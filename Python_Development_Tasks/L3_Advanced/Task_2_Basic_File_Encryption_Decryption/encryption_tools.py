from cryptography.fernet import Fernet 



class EncryptionTools:


    def generate_key(self):

        key = Fernet.generate_key()
        # print(key)
        # print(key.decode())

        with open("my_key.key", "wb") as f:
            f.write(key)


    def load_key(self, file_name="my_key.key"):

        with open(file_name, "rb") as f:
            key = f.read()

        return key


    def encrypt_file(self, file_name: str, key):

        fernet = Fernet(key)

        with open(file_name, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(f"enc_{file_name}", "wb") as encrypted_file:
            encrypted_file.write(encrypted)

        return "File encrypted successfully!"


    def decrypt_file(self, enc_file_name: str, key):

        fernet = Fernet(key)

        with open(enc_file_name, "rb") as enc_file:
            encrypted = enc_file.read()

        decrypted = fernet.decrypt(encrypted)

        # Compute the output file name
        if enc_file_name.startswith("enc_"):
            output_name = "dec_" + enc_file_name[4:]
        else:
            output_name = "dec_" + enc_file_name

        with open(output_name, "wb") as dec_file:
            dec_file.write(decrypted)

        return "File decrypted successfully!"