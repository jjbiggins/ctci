#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import unittest

def is_unique_v02(string: str) -> bool:
    
    return len(list(dict.fromkeys(string).keys())) == len(list(string))

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_is_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique_v02(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_unique_v02(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()

