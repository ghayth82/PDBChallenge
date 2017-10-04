import synapseclient
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
import scipy, scipy.stats
import argparse
import sys
import os
import re
import csv
import math
import nolds
import scipy.signal as signal

parser = argparse.ArgumentParser()
parser.add_argument("--x_y_z_norm", type = str)
parser.add_argument("--function_no", type = int)

args = parser.parse_args()

def q1(x):
    return np.percentile(x,25)
def q3(x):
    return np.percentile(x,75)
def autocorr(x, t=1):
    return np.corrcoef(np.array([x[0:len(x)-t], x[t:len(x)]]))[0,1]

def zcr(x):
    x = np.array(x)
    return ((x[:-1] * x[1:]) < 0.0).sum()/x.shape[0]

def F0(x, timestamps):
    nout = 10000
    f = np.linspace(0.01, 10, nout)
    pgram = signal.lombscargle(np.array(timestamps), np.array(x), f)
    return f[np.argmax(np.array(pgram))] #freq where the max occurred

#17 features should be there

'''meanX   mean of the X acceleration series
sdX standard deviation of the X acceleration series
modeX   mode of the X acceleration series
skewX   skewness of the X acceleration series
kurX    kurtosis of the X acceleration series
q1X first quartile of the X acceleration series
medianX median of the X acceleration series
q3X third quartile of the X acceleration series
iqrX    interquartile range of the X acceleration series
rangeX  range of the X acceleration series
acfX    autocorrelation (lag = 1) of the X acceleration series
zcrX    zero-crossing rate of the X acceleration series
dfaX    scaling exponent of the detrended fluctuation analysis of the X acceleration series
cvX coefficient of variation of the X acceleration series
tkeoX   teager-kaiser energy operator of the X acceleration series
F0X frequency at which the maximum peak of the Lomb-Scargle periodogram occurred for the X acceleration series
P0X maximum power in the inspected frequency interval of the Lomb-Scargle periodogram for the X acceleration series
#ignored mode as it makes no sense and will always return a random value
'''
#the above will be calculated for X, Y, Z and Norm
functions = [np.mean, np.std, scipy.stats.skew, scipy.stats.kurtosis, q1, q3, scipy.stats.iqr, np.ptp, autocorr, zcr, nolds.dfa, scipy.stats.variation, F0 ]

map_recordids_to_filepaths = {}
path = "/home/aditya15007/"
path_csv_map = path + "Test_Walking.csv"
path_files = "/ssd-scratch/aditya15007/Test/deviceMotion_walking_outbound"
with open(path_csv_map) as csv_f:
    rownum = 0
    reader = csv.reader(csv_f,delimiter=',')
    counter = 0
    for row in reader:
        if rownum != 0:
            if(row[8]!=''):
                file_id = int(row[8]) #for device Motion Walking Outbound
                folder_id = str(file_id%1000)
                #print(path_files + "/"+folder_id+"/"+str(file_id))
                map_recordids_to_filepaths[row[2]] = path_files + "/"+folder_id+"/"+str(file_id)
            else:
                counter = counter + 1
        rownum = rownum+1
    #print("Number of empty fields: " + str(counter))

avg_items = {} # initialize empty list for storing mean values
#x_accel = [] # initialize empty list for storing x-acceleration values
# loop through each record to read in json file
# grab the userAcceleration x-values and calculate the means
counter = 0
myfunc = functions[args.function_no]
fileout = "deviceMotion_walking_outbound_" + str(myfunc.__name__.split(".")[-1]) + args.x_y_z_norm + ".csv"

f = open(fileout,'w')
for recordId, path_folder in map_recordids_to_filepaths.items():
    try:
        for file in os.listdir(path_folder):
            if re.match("^deviceMotion_walking_outbound.json.items", file):
                json_file = file
                json_file_path = path_folder+"/"+json_file
                with open(json_file_path) as json_data:
                    arr_accel = [] # initialize empty list for storing acceleration values
                    arr_timestamps = []
                    data = json.load(json_data)
                    for item in data:
                        if args.x_y_z_norm == "X":
                            x = item.get("userAcceleration").get("x")
                            arr_accel.append(x)
                        elif args.x_y_z_norm == "Y":
                            y = item.get("userAcceleration").get("y")
                            arr_accel.append(y)
                        elif args.x_y_z_norm == "Z":
                            z = item.get("userAcceleration").get("z")
                            arr_accel.append(z)
                        elif args.x_y_z_norm == "norm":
                            x = item.get("userAcceleration").get("x")
                            y = item.get("userAcceleration").get("y")
                            z = item.get("userAcceleration").get("z")
                            norm = math.sqrt((x**2) + (y**2) + (z**2))
                            arr_accel.append(norm)
                        timestamp = item.get("timestamp")
                        arr_timestamps.append(timestamp)
                    if args.function_no == 12:
                        val = F0(arr_accel, arr_timestamps)
                    else:
                        val = myfunc(arr_accel)
                    f.write( recordId + "," + str(val) + "\n")
    except FileNotFoundError:
        #print(path_folder + " not found!")
        counter = counter+1
#print(str(counter) + " number of folders could not be found!")
#print(avg_items)
