# -*- coding:UTF-8 -*-
__author__ = 'FEB'
import csv
import os
import functools
init_value=10
def f(x,y):
    print(x*y*5)
    return x*y*5
print(functools.reduce(f,[1,3,5,7,9],init_value))
