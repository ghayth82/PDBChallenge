# PDBChallenge
Parkinson's Disease Digital Biomarker Dream Challenge 

We have the following directory structure:

```
project
│   Walking_Activity_Train.csv
│   Walking_Activity_Test.csv
|   Walking_Activity_Supplemental.csv
│
└───Train
│   │
│   └───deviceMotion_walking_outbound
│       │   123
│       │   234
│       │   ...(the downloaded directory structure for deviceMotion_walking_outbound column)
│   │
│   └───deviceMotion_walking_outbound
│   └───deviceMotion_walking_rest
│   └───deviceMotion_walking_return
│   └───accel_walking_outbound
│   └───accel_walking_rest
│   └───acc_walking_return
│   
└───Test
|   │   
─── Supplemental
|   |
```

For every folder such as deviceMotion_walking_outbound, we use a command
```python common.py --x_y_z_norm Y --function_no 0&```
to calculate the the meanY feature for the files.

--x_y_z_norm is the argument for the type of feature, X,Y,Z or norm..
--function_no is the function no from 0 to 11.

 Similarly, there are 12 different functions that we have calculated,

0 meanX   mean of the X acceleration series
1 sdX standard deviation of the X acceleration series
2 skewX   skewness of the X acceleration series
3 kurtosisX    kurtosis of the X acceleration series
4 q1X first quartile of the X acceleration series
5 q3X third quartile of the X acceleration series
6 iqrX    interquartile range of the X acceleration series
7 ptpX  range of the X acceleration series
8 autocorrX    autocorrelation (lag = 1) of the X acceleration series
9 zcrX    zero-crossing rate of the X acceleration series
10 dfaX    scaling exponent of the detrended fluctuation analysis of the X acceleration series
11 variationX coefficient of variation of the X acceleration series

We then calculate them for each of the 4 types of features, and merge them using the merge code.

##Libraries

scikit-learn
nolds for dfa calculation( https://pypi.python.org/pypi/nolds )
numpy, scipy

Python Version - 3.6



