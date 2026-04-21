#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:45:35 2026

@author: miloreyes
"""

import math

def main():
    start = 0
    end = 2
    amount = 1000
    step_size = (end - start) / (amount - 1)

    for i in range(amount):
        x = start + (i * step_size)
        y = math.sin(x)
        print(f"{x:<10.4f} | {y:<10.4f}")




if __name__ == "__main__":
    main()