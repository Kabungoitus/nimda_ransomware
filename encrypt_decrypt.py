#!/usr/bin/env python3
import os
import argparse
import getpass
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64

def derive_key(password, salt):
    """Derive a 32-byte key from the password using PBKDF2."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def enc_file(file_path, password):
    """Encrypt a file using AES-256-GCM."""
    # Generate random salt and IV
    salt = os.urandom(16)
    iv = os.urandom(12)
    
    # Derive key from password
    key = derive_key(password, salt)
    
    # Read the file
    with open(file_path, 'rb') as file:
        data = file.read()
    
    # Create cipher and encrypt
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data) + encryptor.finalize()
    
    # Write salt, IV, ciphertext, and tag to file
    with open(file_path, 'wb') as file:
        file.write(salt + iv + ciphertext + encryptor.tag)

def dec_file(file_path, password):
    """Decrypt a file using AES-256-GCM."""
    # Read the file
    with open(file_path, 'rb') as file:
        data = file.read()
    
    # Extract salt, IV, ciphertext, and tag
    salt = data[:16]
    iv = data[16:28]
    tag = data[-16:]
    ciphertext = data[28:-16]
    
    # Derive key from password
    key = derive_key(password, salt)
    
    # Create cipher and decrypt
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    
    # Write decrypted data back to file
    with open(file_path, 'wb') as file:
        file.write(plaintext)

def disable_firewall():
    pass  # Placeholder for firewall disabling (not implemented for safety)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File encryption/decryption tool")
    parser.add_argument("directory", help="Directory to process")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Action to perform: encrypt or decrypt")
    args = parser.parse_args()

    password = getpass.getpass("Enter password: ")

    for root, dirs, files in os.walk(args.directory):
        for file in files:
            file_path = os.path.join(root, file)
            if args.action == "encrypt":
                try:
                    enc_file(file_path, password)
                    print(f"File {file_path} has been encrypted successfully.")
                except Exception as e:
                    print(f"Failed to encrypt file {file_path}: {e}")
            elif args.action == "decrypt":
                try:
                    dec_file(file_path, password)
                    print(f"File {file_path} has been decrypted successfully.")
                except Exception as e:
                    print(f"Failed to decrypt file {file_path}: {e}")

    # Print the skeleton ASCII art and creator's name in red
    print("\033[91m")  # Start red color
    print("            .-.")
    print("           (0.0)")
    print("         '=.|m|.='")
    print("jgs     .='`\"``=.")
    print("Created by Kabungo Titus")
    print("\033[0m")  # Reset color to default
