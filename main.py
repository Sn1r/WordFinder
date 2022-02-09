from helpers import *
import sys

if __name__ == '__main__':
    try:
        str_to_find = sys.argv[1]
        find_word_in_files(str_to_find)
    except IndexError:
        print('[!] Please provide a valid argument\n'
        '[+] Example: pytohn main.py foo')