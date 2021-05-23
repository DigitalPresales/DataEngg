# This code goes on Ubuntu (Seller machine). Pl. make sure to have python and below libraries installed. You can refer to google for help to install those.
import os
import pandas as pd 
import sys
df = pd.read_csv(r"<File path of all seller> retailer.csv", index_col=0)
df.sort_values(["dis price", "delivery in days"], ascending=(True, True), inplace=True)
# pl. note, you can use any column to sort the output as shown above, replace dis price with your column name

df.to_csv(r'<File path of output data/o2.csv')
df.head(2).to_csv(r'File path of output data/o2.csv')
#you can show more than 2 competitors to seller by changing df.head(2) to df.head(x) where x is any number you like
