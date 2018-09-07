# -*- coding: utf-8 -*-
"""
Created on Thu May 17 18:14:40 2018

@author: rdsta
"""

import tkinter as tk

for r in range(3):
    for c in range(3):
        btn = Button (text =' _ ', width=5, height=2, pady=2,\
                      command = lambda r=r, c=c: move(r,c))
        btn.grid(row=r,column=c)
        btns.append(btn)
        
label = Label