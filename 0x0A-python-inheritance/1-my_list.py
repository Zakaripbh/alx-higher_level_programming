#!/usr/bin/python3
# 1-my_list.py
# Zakari Usman <zakariusman4real@gmailcom>
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
