#!/bin/python3

import math
import os
import random
import re
import sys


N = int(input())
arr = str(input()).split(" ")
arr.reverse()

for n in arr:
    print(n + " ", end="")
