#!/usr/bin/python3
# 102-magic_calculation.py
# Zakari Usman <zakariusman4real@gmail.com>


def magic_calculation(a, b, c):
    """Match bytecode provided by Holberton School."""
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)
