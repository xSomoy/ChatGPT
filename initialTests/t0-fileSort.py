# input : write a python program that sorts files using file type as a unique parameter


import os

def sort_files_by_type(directory):
  # Create a dictionary to store file types as keys and lists of file names as values
  file_types = {}
  
  # Iterate through the files in the given directory
  for file in os.listdir(directory):
    # Get the file name and file type
    file_name, file_ext = os.path.splitext(file)
    file_ext = file_ext[1:]  # remove the leading '.' from the file extension
    
    # If the file type is not in the dictionary yet, add it as a key
    if file_ext not in file_types:
      file_types[file_ext] = []
    
    # Add the file name to the list for its file type
    file_types[file_ext].append(file_name)
  
  # Print the sorted file names for each file type
  for file_type, file_names in file_types.items():
    print(f"{file_type}: {', '.join(sorted(file_names))}")

# Test the function with a directory of test files
sort_files_by_type("test")
