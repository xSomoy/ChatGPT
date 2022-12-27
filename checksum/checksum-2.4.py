import tkinter as tk
import tkinter.filedialog as filedialog
import hashlib
import ttkthemes

# Create the main window
window = ttkthemes.ThemedTk()
window.get_themes()  # Get the list of available themes
window.set_theme("plastik")  # Set the theme
window.title("Checksum Calculator")
# window.configure(bg='black')  # Set the background color to black
window.geometry("600x300")  # Set the window size to 600x300

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
    md5_label["text"] = "MD5: " + md5
    sha1_label["text"] = "SHA1: " + sha1
    sha256_label["text"] = "SHA256: " + sha256
    
    # Update the file name label
    file_label["text"] = "Selected file: " + file_path

# Create a function to exit the program
def exit_program():
    window.destroy()

# Create a button to select a file using the file manager
select_button = tk.ttk.Button(text="Select File", command=compute_checksums)
select_button.configure(width=20)  # Set the width of the button

# Create a label to display the selected file name
file_label = tk.ttk.Label(text="Selected file:")

# Create labels to display the checksum values
md5_label = tk.ttk.Label(text="MD5:")
sha1_label = tk.ttk.Label(text="SHA1:")
sha256_label = tk.ttk.Label(text="SHA256:")

# Create a button to exit the program
exit_button = tk.ttk.Button(text="Exit", command=exit_program)

# Add the widgets to the window and add some padding
select_button.pack(padx=10, pady=10)
md5_label.pack(padx=10, pady=10)
sha1_label.pack(padx=10, pady=10)
sha256_label.pack(padx=10, pady=10)
exit_button.pack(padx=10, pady=10)

# Run the main loop
window.mainloop()
