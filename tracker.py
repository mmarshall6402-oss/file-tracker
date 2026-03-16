
import os
import sys

if len(sys.argv) < 2:
    print("Usage: python tracker.py <folder_path>")
    sys.exit()

folder = sys.argv[1]

file_count = {}

for file in os.listdir(folder):
    if "." in file:
        ext = file.split(".")[-1]
    else:
        ext = "no_extension"

    file_count[ext] = file_count.get(ext, 0) + 1

print("\nFile Summary:\n")

for ext, count in file_count.items():
    print(f"{ext}: {count} files")
