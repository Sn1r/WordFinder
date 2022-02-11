import os
from time import sleep

colors = {
    'red':"\033[91m",
    'base': "\033[0m"
}

def get_files_path():
    chosen_path = input("Please enter a full path: \n").lower()
    ext = ['.txt', '.json', '.log', '.conf', '.csv', '.html', '.php', '.py', '.rb', '.xml', '.htm']
    files_full_path = [os.path.join(root, f) for (root, subdirs, files) in os.walk(chosen_path) for f in os.listdir(root) if f.endswith(tuple(ext))]
    return files_full_path

def find_word_in_files(str_to_find):
    all_files = get_files_path()
    # Progress Bar
    for i in range(21):
        print ("\r[%-20s] %d%%" % ('='*i, 5*i), end='')
        sleep(0.01)
        
    for file in all_files:
        with open(file, 'r', encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
            for line in lines:
                if str_to_find in line:
                    matched_line_prettified = line.replace(
                        str_to_find, f"{colors['red']}{str_to_find}{colors['base']}"
                    )
                    new_line = '\n'
                    print(f"{new_line}{file}:{matched_line_prettified}")