#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys


def check_permutation_v02(str1, str2):

    if len(str1) != len(str2): return False
    return sorted(str1) == sorted(str2)



if __name__ == "__main__":

    str1='abcd'
    str2='bacd'
    data = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    for str1, str2 in data:
        print(check_permutation_v02(str1, str2))
