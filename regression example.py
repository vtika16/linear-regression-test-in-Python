print (_doc_)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv as csv

###import csv first into the dataset, which i still dont understand the issue here##
with open ('C:\Users\vtika\My Documents\Alteryx\Misc Invoice\misc Invoice Sample.csv', 'rb') as csvfile:
    misc_invoice = csv.reader(csvfile, delimiter=' ')
    for row in misc_invoice:
        print(misc_invoice)

df = pd.DataFrame(misc_invoice)

##or use the pandas function of read.csv##x
pd.read_csv('C:\Users\vtika\My Documents\Alteryx\Misc Invoice\misc Invoice Sample.csv')

#need to see relationship between 2 variables prior to calculating coefficient##
fig, axs = plt.subplots(1, 3, sharey=True)
data.plot(kind='scatter', x='Misc_Invoice_Disposition', y='Deviceamountdue', ax=axs[0], figsize=(16, 8))

## need this to plot the fitted model in one line, cannot pip install for some reason on git bash command line##

import statsmodels 
