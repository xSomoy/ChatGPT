import tkinter as tk
import hashlib

# Create the main window
window = tk.Tk()
window.title("Checksum Calculator")

# Create a function to compute the checksums
def compute_checksums():
    # Get the file path from the entry widget
    file_path = file_entry.get()
    
    # Open the file and read its contents
    with open(file_path, 'rb') as f:
        data = f.read()
        
    # Compute the checksums
    md5 = hashlib.md5(data).hexdigest()
    sha1 = hashlib.sha1(data).hexdigest()
    sha256 = hashlib.sha256(data).hexdigest()
    
    # Update the labels with the checksum values
    md5_label["text"] = md5
    sha1_label["text"] = sha1
    sha256_label["text"] = sha256

# Create a function to exit the program
def exit_program():
    window.destroy()

# Create a label and entry widget to input the file path
file_label = tk.Label(text="Enter the file path:")
file_entry = tk.Entry()

# Create a button to compute the checksums
compute_button = tk.Button(text="Compute Checksums", command=compute_checksums)

# Create labels to display the checksum values
md5_label = tk.Label(text="MD5:")
sha1_label = tk.Label(text="SHA1:")
sha256_label = tk.Label(text="SHA256:")

# Create a button to exit the program
exit_button = tk.Button(text="Exit", command=exit_program)

# Add the widgets to the window
file_label.pack()
file_entry.pack()
compute_button.pack()
md5_label.pack()
sha1_label.pack()
sha256_label.pack()
exit_button.pack()

# Run the main loop
window.mainloop()
