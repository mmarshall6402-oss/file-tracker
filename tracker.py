import os

folder = "sample_files"

file_count = {}

for file in os.listdir(folder):
    if "." in file:
        ext = file.split(".")[-1]
    else:
        ext = "no_extension"

    if ext in file_count:
        file_count[ext] += 1
    else:
        file_count[ext] = 1

print("File Summary:\n")

for ext in file_count:
    print(ext, ":", file_count[ext], "files")


