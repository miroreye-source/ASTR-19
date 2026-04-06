#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:34:16 2026

@author: miloreyes
"""

def f(x):
    return x**3 + 8


def main():
    print(f(3))
    if f(3) > 27:
        print("YAY!")

if __name__ == "__main__":
    main()