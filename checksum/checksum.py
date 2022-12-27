import hashlib
import tkinter as tk
from tkinter import filedialog

def compute_checksum(file_path, algorithm='md5'):
  with open(file_path, 'rb') as f:
    data = f.read()
    if algorithm == 'md5':
      return hashlib.md5(data).hexdigest()
    elif algorithm == 'sha1':
      return hashlib.sha1(data).hexdigest()
    elif algorithm == 'sha256':
      return hashlib.sha256(data).hexdigest()
    else:
      raise ValueError(f'Invalid algorithm: {algorithm}')

def select_file():
  root = tk.Tk()
  root.withdraw()
  file_path = filedialog.askopenfilename()
  return file_path

file_path = select_file()

# Calculate the MD5 checksum
md5_checksum = compute_checksum(file_path, algorithm='md5')
print(f'MD5 checksum: {md5_checksum}')

# Calculate the SHA1 checksum
sha1_checksum = compute_checksum(file_path, algorithm='sha1')
print(f'SHA1 checksum: {sha1_checksum}')

# Calculate the SHA256 checksum
sha256_checksum = compute_checksum(file_path, algorithm='sha256')
print(f'SHA256 checksum: {sha256_checksum}')
