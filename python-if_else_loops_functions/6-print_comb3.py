#!/usr/bin/python3

for i in range(0,10):
     for k in range(1,10):
        if (i == 0 and k == 1):



            txt0 = "{}{}".format(i, k)
            print(txt0, end="")
        else:
            txt1="{}{}".format(i, k)
            print(", ", txt1, end="")
print ()
