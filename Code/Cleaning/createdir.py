import os

folder_Path = "../Desktop/soildata"

try:
    os.mkdir(folder_Path)
except OSError:
    print("Cannot create directory")
else:
    print("Successfully created directory")
