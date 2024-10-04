# python file_handling/fileHandling.py

import shutil
import os

# Creating a directory
def create_directory(path):
    os.makedirs(path, exist_ok=True)
    print(f"Created directory at {path}")

# Creating a file
def create_file(path, content=""):
    with open(path, 'w') as file:
        file.write(content)
    print(f"Created file at {path}")

# Copying a file
def copy_file(src, dst):
    shutil.copy(src, dst)
    print(f"Copied file from {src} to {dst}")

# Copying a directory
def copy_directory(src, dst):
    shutil.copytree(src, dst)
    print(f"Copied directory from {src} to {dst}")

# Moving a file or directory
def move(src, dst):
    shutil.move(src, dst)
    print(f"Moved from {src} to {dst}")

# Deleting a file
def delete_file(path):
    os.remove(path)
    print(f"Deleted file at {path}")

# Deleting a directory
def delete_directory(path):
    shutil.rmtree(path)
    print(f"Deleted directory at {path}")
    
# Writing to a file
def write_to_file(path, content):
    with open(path, 'w') as file:
        file.write(content)
    print(f"Written to file at {path}")

# Reading from a file
def read_from_file(path):
    with open(path, 'r') as file:
        content = file.read()
    print(f"Read from file at {path}: {content}")
    return content

# Appending to a file
def append_to_file(path, content):
    with open(path, 'a') as file:
        file.write(content)
    print(f"Appended to file at {path}")

# Checking if a file exists
def file_exists(path):
    exists = os.path.isfile(path)
    print(f"File exists at {path}: {exists}")
    return exists
    
def main():

    path = os.path.join(os.path.dirname(__file__), 'filedata')
    
    # Create a directory
    create_directory(f'{path}/new_dir')

    # Create a file
    create_file(f'{path}/new_dir/new_file.txt', 'Hello, World!')

    # Copy a file
    copy_file(f'{path}/new_dir/new_file.txt', f'{path}/new_dir/destination.txt')

    # Copy a directory
    copy_directory(f'{path}/new_dir', f'{path}/destination_dir')

    # Move a file
    move(f'{path}/new_dir/destination.txt', f'{path}/destination_dir/source.txt')

    # Delete a file
    delete_file(f'{path}/destination_dir/destination.txt')

    # Delete a directory
    delete_directory(f'{path}/new_dir')
    delete_directory(f'{path}/destination_dir')
    
    # Write to a file
    write_to_file(f'{path}/new_file.txt', 'Hello, World!')

    # Read from a file
    read_from_file(f'{path}/new_file.txt')

    # Append to a file
    append_to_file(f'{path}/new_file.txt', '\nAppended content.')

    # Read from a file again to see appended content
    read_from_file(f'{path}/new_file.txt')

    # Check if a file exists
    file_exists(f'{path}/new_file.txt')
    
if __name__ == '__main__':
    main()