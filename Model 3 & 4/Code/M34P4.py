#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:28:09 2026

@author: omar
"""

# Split job payment evenly between three people

amount_received = float(input("Enter the total amount received: "))

each_person_receives = amount_received / 3

print(f"Each person will receive: ${each_person_receives:.2f}")