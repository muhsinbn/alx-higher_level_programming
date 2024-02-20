#!/usr/bin/python3

def read_file(filename):
    """
    Read the contents of the file and print them to stdout
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
