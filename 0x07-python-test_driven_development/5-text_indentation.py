#!/usr/bin/python3
"""The module prints a text with 2 new lines after . ? : """


def text_indentation(text):
    """splits string into lines along "?", ":", "." followed by 2 new lines
    Args:
        text - Is the text to print
    raises:
        TypeError if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    myflag = 0
    for i in text:
        if myflag == 0:
            if i == ' ':
                continue
            else:
                myflag = 1
        if myflag == 1:
            if i == '?' or i == '.' or i == ':':
                print(i)
                print()
                myflag = 0
            else:
                print(i, end="")
