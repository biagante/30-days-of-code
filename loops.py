#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    
    N = int(input().strip())
    for i in range(1, 10 + 1):
        print(N, "x", i, "=", N*i )
