import os

def print_directory_structure(folder, indent=""):
    excluded_dirs = {'.vd'} 
    print(f"{indent}\"{os.path.basename(folder)}\"")
    
    for item in os.listdir(folder):
        if item in excluded_dirs:  
            continue
        item_path = os.path.join(folder, item)
        
        if os.path.isdir(item_path):
            print_directory_structure(item_path, indent + "    ├──")
        else:
            print(f"{indent}    ├── {item}")

print_directory_structure(r"C:\Users\dell\OneDrive\Desktop\Vision Depth")

'''
"Vision Depth"
    ├──"images"
    ├──    ├── 20240512_155111.jpg
    ├──    ├── 20240512_155123.jpg
    ├──    ├── 20240512_155130.jpg
    ├── main.py
    ├── path.py
    ├── requirements.txt

'''

