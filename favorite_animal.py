#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:00:03 2026

@author: miloreyes
"""

class Dog:
    def __init__(self, arm_length, leg_length, eye_count, tail, furry):
        self.arm_length = float(arm_length)
        self.leg_length = float(leg_length)
        self.eye_count = int(eye_count)
        self.tail = bool(tail)
        self.furry = bool(furry)
    
    def describe_dog(self):
        print(f"Arm Length: {self.arm_length} cm")
        print(f"Leg Length: {self.leg_length} cm")
        print(f"Number of Eyes: {self.eye_count}")
        print(f"Has a Tail? {self.tail}")
        print(f"Is it Furry? {self.furry}")
        

zoe = Dog(17.5, 18.2, 2, True, True)

zoe.describe_dog()
