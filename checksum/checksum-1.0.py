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

def compute_md5():
  file_path = select_file()
  checksum = compute_checksum(file_path, algorithm='md5')
  result_label.config(text=checksum)

def compute_sha1():
  file_path = select_file()
  checksum = compute_checksum(file_path, algorithm='sha1')
  result_label.config(text=checksum)

def compute_sha256():
  file_path = select_file()
  checksum = compute_checksum(file_path, algorithm='sha256')
  result_label.config(text=checksum)

root = tk.Tk()
root.title('Checksum Calculator')

md5_button = tk.Button(root, text='Compute MD5', command=compute_md5)
md5_button.pack()

sha1_button = tk.Button(root, text='Compute SHA1', command=compute_sha1)
sha1_button.pack()

sha256_button = tk.Button(root, text='Compute SHA256', command=compute_sha256)
sha256_button.pack()

result_label = tk.Label(root, text='')
result_label.pack()

root.mainloop()
