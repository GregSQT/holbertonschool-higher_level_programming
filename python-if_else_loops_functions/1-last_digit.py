#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
  
s = str(number)
lastDigit = int(s[-1])

print("Last digit of ",number," is ",lastDigit) 
