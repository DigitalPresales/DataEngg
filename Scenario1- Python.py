#Blow code goes on Ubuntu(Seller machine) so make sure to install python and some of the libraries mentioned below.
#You can google to find those installation details.

import os
import pandas as pd 
import sys
df = pd.read_csv(r"<File path of buyerdata.csv", index_col=0)
df.sort_values(["Highest Purchase Amount - dollar"], ascending=[False], inplace=True)
#above line will sort data by Highest Purchase Amount - dollar . This can be changed to any column you like to get data sorted.Just use that column name and order ascending - True or false.
df.to_csv(r'<File path of output file which is o1.csv')
