#!/usr/bin/python3

for i in range(0,10):
     for k in range(1,10):
        if (i == 0 and k == 1):
            print(str(i)+str(k), end="")
        else:
            print(", ", str(i)+str(k), end="")
print ()
