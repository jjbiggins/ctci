#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

#==================================================================================#
# DEFINITION                                                                       #
#==================================================================================#
# In mathematics, a permutation implies a relationship of one set to another       #
# that is, when two sets share the same elements (i.e. 1,2,3,4,5,6,7) a            #
# permutation is any possible arrangement of those elements (i.e. 2,3,4,5,7,6,1)   #
#==================================================================================#

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    elif len(str1) < 3:
        if len(str1) == 2:
            return (str1[0] == str2[0] and ord(str1[1]) == ord(str1[1]))
        else:
            return (str1 == str2)
            # I could use sorted() func and compare two strings
            # such that, if sorted(str1) == sorted(str2) is True
            # it is a permutation, and not if False.
            # However, that takes the fun part out of it, so ...
    else:
        max_str1 = ord(str1[0])
        max_str2 = ord(str2[0])

        min_str1 = ord(str1[0])
        min_str2 = ord(str2[0])

        max1_i = 0
        max2_i = 0
        min1_i = 0
        min2_i = 0

        for i in range(len(str1)):
            if ord(str1[i]) > max_str1:
                max_str1 = ord(str1[i])
                max1_i = i
            elif ord(str1[i]) < min_str1:
                min_str1 = ord(str1[i])
                min1_i = i

            if ord(str2[i]) > max_str2:
                max_str2 = ord(str2[i])
                max2_i = i
            elif ord(str2[i]) < min_str2:
                min_str2 = ord(str2[i])
                min2_i = i


        if max_str1 != max_str2 or min_str1 != min_str2:
            #print(max_str1)
            return False
        else:

            #print("{}, {}".format(str1, str2))
            if min1_i < max1_i:
                str1 = str1[:min1_i] +  str1[min1_i+1:max1_i] + str1[-1:]
            else:
                str1 = str1[:max1_i] + str1[max1_i+1:min1_i] + str1[min1_i+1:]

            if min2_i < max2_i:
                str2 = str2[:min2_i] + str2[min2_i+1:max2_i] + str2[-1:]
            else:
                str2 = str2[:max2_i] + str2[max2_i+1:min2_i] + str2[min2_i+1:]

            #print("{}, {}".format(str1, str2))
            return check_permutation(str1,str2)

if __name__ == '__main__':
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
    for i in range(len(data)):
        str1,str2 = data[i]
        if len(str1) != len(str2):
            print(False)
        else:
            print(check_permutation(str1, str2))
