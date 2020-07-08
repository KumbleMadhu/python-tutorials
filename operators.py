import math
import os
import random
import re
import sys

meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())


def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    total = meal_cost + tip + tax
    print(str(round(total)))


if __name__ == '__main__':
    solve(meal_cost, tip_percent, tax_percent)
