import tkinter as tk
import tkinter.filedialog as filedialog
import hashlib
import ttkthemes

# Create the main window
window = ttkthemes.ThemedTk()
window.get_themes()  # Get the list of available themes
window.set_theme("plastik")  # Set the theme
window.title("Checksum Calculator")
window.configure(bg='#132031')  # Set the background color to black

# Create a function to compute the checksums
def compute_checksums():
    # Use the filedialog module to open a file selection dialog
    file_path = filedialog.askopenfilename()
    
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

# Create a button to select a file using the file manager
select_button = tk.ttk.Button(text="Select File", command=compute_checksums)

# Create labels to display the checksum values
md5_label = tk.ttk.Label(text="MD5:")
sha1_label = tk.ttk.Label(text="SHA1:")
sha256_label = tk.ttk.Label(text="SHA256:")

# Create a button to exit the program
exit_button = tk.ttk.Button(text="Exit", command=exit_program)

# Add the widgets to the window and align them to the left
select_button.pack()
md5_label.pack()
sha1_label.pack()
sha256_label.pack()
exit_button.pack()

# Run the main loop
window.mainloop()
