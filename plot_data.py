import os
import pandas as pd
import matplotlib.pyplot as plt
from read_file import get_groceries

"""
This program plots the data returned by get_groceries
The goal is to view grocery store spending overtime
Currently, it just plots a basic line graph where each month is a tic on the x-axis
Maybe a scatter plot with a trend line?
"""
test = get_groceries()


plt.plot(test['Transaction Date'], test['Debit'])
plt.show()
