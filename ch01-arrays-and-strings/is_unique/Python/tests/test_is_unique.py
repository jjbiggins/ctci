#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import random
import string
import is_unique 
import time

BASE = 2
NUMBER_OF_TESTS = 8


def exponential(exponent: int = 0):
    return BASE ** exponent


def generate_random_string_of_length(str_length: int = 0):
    return ''.join(random.choices(string.ascii_lowercase, k=str_length))


def test_runner(func1, func2):
    results = [[0,0, 0]] * NUMBER_OF_TESTS


    for exponent in range(1, NUMBER_OF_TESTS + 1):
        result = exponential(exponent=exponent)

        rand_string = generate_random_string_of_length(str_length=result)

        s1 = time.perf_counter()
        res1 = func1(rand_string)
        e1 =  time.perf_counter() - s1

        s2 = time.perf_counter()
        res2 = func1(rand_string)
        e2 =  time.perf_counter() - s2


        delta_percent = percent_faster(e1, e2)

        results[exponent - 1] = [str(e1), str(e2), str(delta_percent)]
        #print("{: >20} {: >20} {: >20}".format(e1, e2, delta_percent))
        #print(str(e1).ljust(10), str(e2).ljust(12), str(round(delta_percent, 2)).rjust(20), str(res1).rjust(8), str(res2).rjust(8), end=' \n')
    return results

def percent_faster(t0, t_final):
    return ((t0 - t_final) / t_final) * 100 


def print_results(results):
    for x in results:
        print(str(x[0]).rjust(8), str(x[1]).rjust(8), end=' ')



if __name__ == "__main__":
    res= test_runner(is_unique.version01, is_unique.version02)

    for row in res:
        print("{: >30} {: >30} {: >30}".format(*row))

    #print_results(res)
