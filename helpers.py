import os

colors = {
    'red':"\033[91m",
    'base': "\033[0m"
}

def get_files_path():
    chosen_path = input("What is your path?\n")
    # files_path = os.path.join(os.curdir, chosen_path)
    ext = ['.txt', '.json', '.log', '.conf', '.csv', '.html', '.php', '.py', '.rb']
    files_full_path = [os.path.join(root, f) for (root, subdirs, files) in os.walk(chosen_path) for f in os.listdir(root) if f.endswith(tuple(ext))]
    return files_full_path

def find_word_in_files(str_to_find):
    all_files = get_files_path()
    for file in all_files:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if str_to_find in line:
                    matched_line_prettified = line.replace(
                        str_to_find, f"{colors['red']}{str_to_find}{colors['base']}"
                    )
                    print(f"{file}:{matched_line_prettified}")