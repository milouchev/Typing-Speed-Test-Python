#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 23:32:56 2022

@author: milouchev
"""

import time
import random
from words import words

prompt = "Enter the sentence below: \n"


while 1:
    a = (random.choice(words))
    b = (random.choice(words))
    c = (random.choice(words))
    d = (random.choice(words))
    e = (random.choice(words))
    f = (random.choice(words))
    g = (random.choice(words))
    h = (random.choice(words))
    i = (random.choice(words))
    j = (random.choice(words))
    
    text = (a+" "+b+" "+c+" "+d+" "+e+" "+f+" "+g+" "+h+" "+i+" "+j)
    word_count = len(text.split())
    print(prompt)
    print(text)
    t0 = time.time()
    input_text = str(input("\nType the sentence: "))
    t1 = time.time()
    accuracy = len(set(input_text.split())&set(text.split()))
    accuracy = round((accuracy/word_count)*100,2)
    time_taken = round(t1-t0,2)
    wpm = round(word_count/(time_taken/60),2)
    print("\nWPM:",wpm,"\nAccuracy:",accuracy,"%","\nTime:",time_taken,"seconds\n\n\n\n")
    

    