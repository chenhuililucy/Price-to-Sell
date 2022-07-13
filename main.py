#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'valuation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER reqArea
#  2. LONG_INTEGER_ARRAY area
#  3. LONG_INTEGER_ARRAY price
#
from collections import defaultdict
from collections import OrderedDict
import bisect
def outlier_removal(area, price):
    """
    Removal of outliers in O(N) time
    """
    d = defaultdict(list) # keep track of area to price one to many mappings
    x_total = {} # keep track of area to total price one to many mapping
    sum_x_squared = {} # keep track of area to sum of the squares of price one to many mapping 
    for idx in range(len(area)):
        d[area[idx]].append(price[idx])
        if area[idx] not in x_total:
            x_total[area[idx]] = price[idx]
        else:
            x_total[area[idx]] += price[idx]
        if area[idx] not in sum_x_squared:
            sum_x_squared[area[idx]] = price[idx] ** 2
        else:
            sum_x_squared[area[idx]] += price[idx] ** 2
    
    comp_areas = defaultdict(float) # mapping comp area to total price
    comp_freq = defaultdict(int) # mapping comp area to number of houses
    for key, val in d.items():
        for i in range(len(val)):
            if len(val) - 1 > 0:
                average = (x_total[key] -  val[i]) / (len(val) - 1)
                sigma = ((sum_x_squared[key] -  val[i] ** 2) / (len(val) - 1) - average ** 2) ** 0.5
                if not abs(val[i] - average) > 3 * sigma:
                    comp_areas[key] += val[i]
                    comp_freq[key] += 1
            else:
                comp_areas[key] += val[i]
                comp_freq[key] += 1
    for key in comp_freq.keys():
        comp_areas[key] /= comp_freq[key]
    return comp_areas
    
def check_price_bounds(price):
    if price < 10 ** 3: 
        return 10 ** 3
    elif price > 10 ** 6:
        return 10 ** 6
    else:
        return price
    
def valuation(reqArea, area, price):
    
    comp_areas = outlier_removal(area, price)

    # sort by filtered houses by final area
    final_area, final_price= [], []
    od = OrderedDict(sorted(comp_areas.items()))
    for key, val in od.items():
        final_area.append(key)
        final_price.append(val)
    
    # determine valuation
    if len(final_area) == 0:
        return check_price_bounds(round(1000 * reqArea))
    elif len(final_area) == 1:
        return check_price_bounds(round(reqArea * (final_price[0] / final_area[0])))
    elif reqArea in final_area:
        idx = final_area.index(reqArea)
        return check_price_bounds(round(final_price[idx]))
    else:
        insert_position = bisect.bisect_left(final_area, reqArea) # note: bisect_left is a binary search
        if insert_position == len(final_area):
            lower_p, higher_p = final_price[-2], final_price[-1]
            lower_a, higher_a = final_area[-2], final_area[-1]
            return check_price_bounds(round(higher_p + (reqArea - higher_a) * ((higher_p - lower_p) / (higher_a - lower_a))))
        elif insert_position == 0:
            lower_p, higher_p = final_price[0], final_price[1]
            lower_a, higher_a = final_area[0], final_area[1]
            return check_price_bounds(round(lower_p - (lower_a - reqArea) * ((higher_p - lower_p) / (higher_a - lower_a))))
        else:
            lower_p, higher_p  = final_price[insert_position - 1], final_price[insert_position]
            lower_a, higher_a = final_area[insert_position - 1], final_area[insert_position]
            return check_price_bounds(round(lower_p + (reqArea - lower_a) * ((higher_p - lower_p) / (higher_a - lower_a))))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    reqArea = int(input().strip())

    area_count = int(input().strip())

    area = []

    for _ in range(area_count):
        area_item = int(input().strip())
        area.append(area_item)

    price_count = int(input().strip())

    price = []

    for _ in range(price_count):
        price_item = int(input().strip())
        price.append(price_item)

    result = valuation(reqArea, area, price)

    fptr.write(str(result) + '\n')

    fptr.close()
