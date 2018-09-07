# -*- coding: utf-8 -*-
"""
Created on Tue May  1 17:21:53 2018

@author: staie

def func (*args):
    for x in args:
        print (x)
    print (sum(args))
    pass

func(1,2,3,4,5,6,7)
"""

import openpyxl


wb = openpyxl.Workbook()

sheet = wb['Sheet']

#column A contains the names of hte students
#columns B throuhg K contain the scores
#column L contains the averages
#column M contains the grade

#row 1 contains the due dates

sheet.cell(row = 2, column = 12).value = '= AVERAGE(B2:K2)'



