#!/usr/bin/python3

def read_file(filename):
    """
    Read the contents of the file and print them to stdout
    """
    with open(filename, encoding='utf-8') as file:
        text = file.read()
        print(text, end='')
