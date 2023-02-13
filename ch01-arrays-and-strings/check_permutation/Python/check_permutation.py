#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import unittest
from functools import wraps

def st_time(func):
    """
    st decorator to calculate the total time of a func
    """
    @wraps(func)
    def st_time_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        st_time_wrapper.counter += 1
        st_time_wrapper.time_sum += execution_time
        st_time_wrapper.average_time = st_time_wrapper.time_sum / st_time_wrapper.counter

        print("Function=%s, Time=%s, Average=%s" % \
                (func.__name__, execution_time, st_time_wrapper.average_time))
        return result

    st_time_wrapper.counter = 0
    st_time_wrapper.time_sum = 0
    st_time_wrapper.average_time = 0
    return st_time_wrapper


@st_time
def check_permutation_v01(str1, str2):
    if len(str1) != len(str2): return False
    return sorted(str1) == sorted(str2)


@st_time
def check_permutation_v02(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    for ch in str1:
        if ch not in str2:
            return False
        elif str1.count(ch) != str2.count(ch):
            return False
    return True




class TestCheckPermutation(unittest.TestCase):
    datatrue = [
            ('abcd', 'bacd'),
            ('3563476', '7334566'),
            ('abcd2', 'd2cba'),
            ('wef34f', 'wffe34'),
            ('2314', '1234'),
            ('dcw4f', 'dcw4f'),
        ]


    datafalse = [
            ('abcd', 'baxsacd'),
            ('3563486', '7334566'),
            ('wef34ffasd', 'asewffe34'),
            ('abcdxxaA2', 'd2cbaaBxx'),
            ('2314523', '12346523'),
            ('dcw4fbigginsjoe', 'dcw4fbigginsjce'),
        ]


    def test_check_permutation_v01(self):
        for strpair in self.datatrue:
            actual = check_permutation_v01(strpair[0], strpair[1])
            self.assertTrue(actual)

        for strpair in self.datafalse:
            actual = check_permutation_v01(strpair[0], strpair[1])
            self.assertFalse(actual)

    def test_check_permutation_v02(self):
        for strpair in self.datatrue:
            actual = check_permutation_v02(strpair[0], strpair[1])
            self.assertTrue(actual)

        for strpair in self.datafalse:
            actual = check_permutation_v02(strpair[0], strpair[1])
            self.assertFalse(actual)




if __name__ == "__main__":
    unittest.main()
