import os
from time import sleep

SIGNATURE = b'SCTLOCK' 

def xor_encrypt_decrypt(file_path, password):
    if not os.path.isfile(file_path):
        print("⚠️ File not found!")
        return

    with open(file_path, 'rb') as f:
        data = bytearray(f.read())

    key = bytearray(password.encode())
    key_len = len(key)

    encrypting = not file_path.endswith('_enc.jpg') and not file_path.endswith('_enc.png')

    if encrypting:
        data = bytearray(SIGNATURE) + data 

    print("\n🔄 Processing...")
    for i in range(len(data)):
        data[i] ^= key[i % key_len]
        if i % (len(data)//10 + 1) == 0:
            print(f"Progress: {int((i / len(data)) * 100)}%", end='\r')
            sleep(0.01)

    if not encrypting:
        if data[:len(SIGNATURE)] != SIGNATURE:
            print("❌ Wrong password! Decryption failed.")
            return
        data = data[len(SIGNATURE):] 

    output_file = get_output_filename(file_path)
    with open(output_file, 'wb') as f:
        f.write(data)

    print(f"\n✅ Done! Output saved as: {output_file}")

def get_output_filename(original_path):
    name, ext = os.path.splitext(original_path)
    if name.endswith('_enc'):
        return name[:-4] + '_dec' + ext
    else:
        return name + '_enc' + ext

def menu():
    while True:
        print("\n=== Image Encryption Tool ===")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            path = input("Enter image file name (in this folder): ").strip()
            password = input("Enter password: ").strip()
            xor_encrypt_decrypt(path, password)

        elif choice == '2':
            path = input("Enter encrypted image file name: ").strip()
            password = input("Enter password: ").strip()
            xor_encrypt_decrypt(path, password)

        elif choice == '3':
            print("👋 Exiting.")
            break

        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
