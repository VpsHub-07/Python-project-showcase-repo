import math
import os
import random
import re
import sys



n=random.randint(1,100)
print(n)
if n%2==1:
    print("Weird")
else:
    if n<=5:
        print("Not Weird")
    elif n>5 and n<=20:
        print("Weird")
    else:
        print("Not Weird")