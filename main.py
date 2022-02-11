from handlers import *
import sys

if __name__ == '__main__':
    try:
        str_to_find = sys.argv[1]
        find_word_in_files(str_to_find)
    except IndexError:
        print('[!] Please provide a valid argument\n'
        '[+] Example: python main.py foo')
    except FileNotFoundError:
        print("[!] Path was not found or bad characters were entered")
    except KeyboardInterrupt:
        print("[!] Keyboard Interrupted")
    except PermissionError:
        print("\n[!] Permission denied. Please make sure you have the right permissions for this directory")