#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:22:13 2026

@author: miloreyes
"""

def sum(float1, float2):
    print(f"The sum of {float1} and {float2} is {float1 + float2}")
    print(type(float1+float2))


def difference(num1, num2):
    print(f"The difference between {num1} and {num2} is {num2-num1}")
    print(type(num2-num1))
    

def product(float1, num1):
    print(f"The product of {float1} and {num1} is {float1*num1}")
    print(type(float1*num1))

def main():
    sum(5.0, 6.0)
    difference(5, 6)
    product(5.0, 6)
    
if __name__ == "__main__":
    main()