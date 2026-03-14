import os
import sys 

# OS module - operating system interactions
# print(f"Current working directory: {os.getcwd()}")
# print(f"Files in current directory: {os.listdir('.')}")
# print(f"OS name: {os.name}")
# print(os.environ.get('PATH', 'Not found'))


# Path operations
path = os.path.join("folder", "subfolder", "file.txt")
# print(f"Joined path: {path}")
# print(os.path.exists('file.txt'))
# print(os.path.isfile('file.txt'))
# print(f"Is directory? {os.path.isdir('folder')}")
# print(f"File size: {os.path.getsize('file.txt') if os.path.exists('file.txt') else 'N/A'}")
# print(f"Absolute path: {os.path.abspath('.')}")



# -----------------------------------------------------------------------

# Sys module - Python interpreter info
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"Platform: {sys.platform}")
print(f"Command line args: {sys.argv}")
print(f"Path: {sys.path[:3]}...")