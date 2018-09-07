# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 16:03:24 2018

@author: staie
"""

import openpyxl as xl
#from openpyxl import * erases any duplicate programs
#import retains the python basic functions as well as importing the new ones



wb = xl.load_workbook ('data/excel/sample1.xlsx')

#normal python code doesn't have an _ in its name


sheets = wb.sheetnames
print (sheets)

summary = wb['Summary']


print (summary, '\n')

header = summary['A1':'D1'][0]
print (header, '\n')

for c in header:
    print (c, c.value)

col_A = summary ['A']
print (col_A)


for a1 in col_A:
    print (a1.value)
