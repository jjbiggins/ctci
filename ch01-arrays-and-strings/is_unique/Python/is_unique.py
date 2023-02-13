#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import unittest
from functools import wraps
from rich.console import Console
from rich.table import Table

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
def is_unique_v01(string):
    """
    since there are only 128 ASCII chars
    if the string's length exceeds 128
    at least one char must be a duplicate
    """

    if len(string) > 128:
        return False
    else:
        """
        create an array of 128 elements
        with each element set to False
        i.e. [False,...,False]
        """
        has_char_appeared = [False] * 128


        """
        for every char ch in string
        set the nth element of arr
        to True, where nth is ch
        ascii code in decimal form
        """
        for ch in string:
            ascii_code = ord(ch)
            if has_char_appeared[ascii_code] == False:
                has_char_appeared[ascii_code] = True
            else:
                return False
        return True

@st_time
def is_unique_v02(string: str) -> bool:

    charlst = list(string)
    uniquechars = []

    for ch in charlst:
        if ch in uniquechars:
            return False
        uniquechars.append(ch)
    return True


@st_time
def is_unique_v03(string: str) -> bool:
    return len(list(dict.fromkeys(string).keys())) == len(list(string))


@st_time
def is_unique_v04(string: str) -> bool:
    return len(set(string)) == len(string)




class TestIsUnique(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), (''), ('John Figure')]
    dataF = [('23ds2'), ('hb 627jh=j ()'), ('joebiggins')]

    def test_is_unique_v01(self):
        """
        Test that all characters in string are unique
        """
        print("")
        for test_string in self.dataT:
            actual = is_unique_v01(test_string)
            self.assertTrue(actual)

        for test_string in self.dataF:
            actual = is_unique_v01(test_string)
            self.assertFalse(actual)

    def test_is_unique_v02(self):
        print("")

        for test_string in self.dataT:
            actual = is_unique_v02(test_string)
            self.assertTrue(actual)

        for test_string in self.dataF:
            actual = is_unique_v02(test_string)
            self.assertFalse(actual)

    def test_is_unique_v03(self):
        """"""
        print("")

        for test_string in self.dataT:
            actual = is_unique_v03(test_string)
            self.assertTrue(actual)

        for test_string in self.dataF:
            actual = is_unique_v03(test_string)
            self.assertFalse(actual)
        
    def test_is_unique_v04(self):
        print("")
        for test_string in self.dataT:
            actual = is_unique_v04(test_string)
            self.assertTrue(actual)

        for test_string in self.dataF:
            actual = is_unique_v04(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
