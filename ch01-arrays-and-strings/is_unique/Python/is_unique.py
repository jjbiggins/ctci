#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

def version01(string):

    # since there are only 128 ASCII chars
    # if the string's length exceeds 128
    # at least one char must be a duplicate
    if len(string) > 128:
        return False
    else:
        # create an array of 128 elements
        # with each element set to False
        # i.e. [False,...,False]
        has_char_appeared = [False] * 128

        # for every char ch in string
        # set the nth element of arr
        # to True, where nth is ch
        # ascii code in decimal form
        for ch in string:
            ascii_code = ord(ch)
            if has_char_appeared[ascii_code] == False:
                has_char_appeared[ascii_code] = True
            else:
                return False

        return True


def version02(string: str) -> bool:
    return len(list(dict.fromkeys(string).keys())) == len(list(string))







