#!/usr/bin/python3
"""This Depicts blocked class module"""


class LockedClass:
    """This object prevents dynamic attribute"""

    __slots__ = ['first_name']
