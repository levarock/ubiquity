# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



def fibRecursive(x):
    if x == 0 :
        return 0
    elif x==1 :
        return 1
    else:
        return fibRecursive(x-1) + fibRecursive(x-2)
  

def fibLinear(x):
    fib = 0
    for i in range(x+1):
        if i == 0:
            fib = 0
        elif i ==1:
            fib =1
            fibl = 0
        else:
            fibtemp = fib
            fib = fibtemp+ fibl
            fibl = fibtemp
    return fib
    

   
