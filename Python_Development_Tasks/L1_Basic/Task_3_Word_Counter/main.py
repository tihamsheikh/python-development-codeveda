import os 

file_name = "story.txt"
words = None 

try:
    path = os.path.abspath(file_name)
    with open(path, "r") as f:
        words = f.read().strip()
except FileNotFoundError:
    print("file not found")


if words: 
    print(f"Total word in {file_name} file: {len(words.split())}")