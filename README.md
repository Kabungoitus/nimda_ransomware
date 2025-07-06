# Ransomware Simulator

This is an educational ransomware simulator that can mimick real world attacks and simulations project designed to demonstrate how ransomware might encrypt files and evade security measures. It is intended for learning purposes only and should **not** be used on real systems or networks.

## Project Overview
The project simulates ransomware behavior using Python, including:
- File encryption/decryption with a simple XOR algorithm.
- A placeholder for firewall disabling (disabled for safety).
- Recursive directory traversal to process multiple files.

The code is organized in a modular structure with source code, tests, and documentation.

## Folder Structure
nimda_ransomware/ |-----src/ 
#nimda ransomware folder contains a subfolder which contains the nimda_ransomware.py  
Main script(nimda_ransomware.py) |-------docs
#Documentation (this includes the README.md && LICENSE agreement that is applicable to all that want use of this software)
##prerequisites
-python 3.13.3 or python 3.x
-A virtual machine (e.g ..., VirtualBox with Kali Linux or Windows) for safetesting

## Installation 
clone the repository 
```bash 
git clone https://github.com/kabungoitus/nimda_ransomware.git
cd nimda_ransomware

no additional dependences are needed (uses os,shutil,argparse)

##Warning test only in a virtual machine to avoid data loss

nimda_ransomware usage
after navigating to the directory run
```bash
encrypt
python3 src/nimda_ransomware.py tests/test_data 42 --mode encrypt

```bash 
python3 nimda_ransomware 
this cmd displays cmd line arguements for the software
```bash 
python3 nimda_ransomware.py /home/kali/ test 42

```bash 
decrypt
python3 src/nimda_ransomware.py /tests/test_data 42 --mode decrypt
```bash 
Create a test file 
echo "Test data" > tests/test_data/sample.txt
```bash
Use the dec_enc.py file for decryptions and encryption of file
default passwd is admin 
python3 encrypt_decrypt.py ./test_directory encrypt
``bash output might looklike
Enter password: 
File ./test_directory/file1.txt has been encrypted successfully.
File ./test_directory/file2.txt has been encrypted successfully.
    .-.
   (0.0)
 '=.|m|.='
jgs     .='`"``=.
Created by Kabungo Titus
``bash
python3 encrypt_decrypt.py /path/to/directory decrypt
password:admin
output might looklike
Enter password: 
File ./test_directory/file1.txt has been encrypted successfully.
File ./test_directory/file2.txt has been encrypted successfully.
    .-.
   (0.0)
 '=.|m|.='
jgs     .='`"``=.
Created by Kabungo Titus
if the wrong password is entered you will 
Failed to decrypt file ./test_directory/file1.txt: InvalidTag

