#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:39:34 2020

@author: bruno
"""

import basico

while True:
    text = input('basico> ')
    result, error = basico.run('<stdin>',text)

    if error: print(error.as_string())
    else: print(result)