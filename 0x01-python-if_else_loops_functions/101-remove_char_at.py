#!/usr/bin/python3


def remove_char_at(str, n):
    if n < 0:
        return str
    else:
        str1 = str[:n]
        str2 = str[n + 1 :]
        return str1 + str2
