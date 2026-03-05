from encryption_tools import EncryptionTools
import os 

instance = EncryptionTools()

key = instance.load_key(file_name="my_key.key")
# print(instance.encrypt_file(file_name="dummy_data.csv", key=key))
# print(instance.decrypt_file(enc_file_name="enc_dummy_data.csv", key=key))

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Exit")

    choice = input("Enter your choice(1,2,3): ").strip()

    if choice == "1":
        file_name = input("Enter the name of the file to encrypt: ")
        print(instance.encrypt_file(file_name=file_name, key=key))

    elif choice == "2":
        enc_file_name = input("Enter the name of the encrypted file to decrypt: ")
        print(instance.decrypt_file(enc_file_name=enc_file_name, key=key))

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")

    input("Press Enter to continue...")