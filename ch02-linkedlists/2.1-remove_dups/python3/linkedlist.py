#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from typing import *

class IntNode(object):
    def __init__(self, value: int, next_node):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return str(self.value)

    

class LinkedList(object):
    def __init__(self, head=None):
        self.head = None
        self._current = None

    def __repr__(self):
        return '<{} {}>'.format(type(self).__name__, self.head)

    def __iter__(self):
        self._current = self.head
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        current, self._current = self._current, self._current.next
        return current

   # property(fget=None, fset=None, fdel=None, doc=None)
    #   fget - func that returns the val of managed attr
    #   fset - func allows setting val of managed attr
    #   fdel - func to define managed attr handles deletion
    #   doc - str represening the property's docstring
    #
    @property
    def is_empty(self):
        return self.head is None
    

    def prepend_node(self, valuetoadd: int):
        self.head = IntNode(valuetoadd, self.head)
    
    
if __name__ == "__main__":
    ill = LinkedList()
    for x in range(0,424):
        ill.prepend_node(x)


    for x in ill:
        open('output.log','a').write(str(x)+'\n')
