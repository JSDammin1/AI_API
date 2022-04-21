#set up environment
import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
import time
import pathlib
from tqdm import tqdm
from time import sleep
import os

#clear board
os.system('cls' if os.name == 'nt' else 'clear')

#get input for what symbol/brand
symbol = input("""What Company, type in symbol EX. IBM or TSLA
""")

#get key from read file and store API_Key
key = open('Alpha_API_Key.txt').read()

#call to API and make timeseries
ts = TimeSeries(key, output_format='pandas')
data, meta = ts.get_intraday(symbol, interval='60min', outputsize='full')

#loading bar for un-refined data
print("Contact API")
for i in tqdm(range(100)):
    sleep(0.02)

#wait time
print("Parse Data")
for i in tqdm(range(100)):
    sleep(0.02)

#give table data
data.info()

#refine table
data.head()

#wait time
print("Prep File")
for i in tqdm(range(100)):
    sleep(0.02)

#start file save proccess
directory = "/home/terminal/Documents/python/Alpha_API_Script/"
filepath = directory + symbol

#give graph and save as pdf
plt.plot(data['4. close'])
plt.savefig(filepath, dpi=1080, format='pdf')

#done message
print("Done!")
print("Saved file to", filepath)
