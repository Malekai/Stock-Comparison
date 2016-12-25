#Application to gather two different stock symbols
#display information about them for the last three months
#Compare by their Average differences in Opening, High, Low, Closing for the past three months
#Plot out chart displaying comparison

#Packages
import pandas as p
import pandas.io.data as web
import datetime
import matplotlib.pyplot as plt
import numpy as np

#Display plot in Jupyter
%matplotlib inline
%pylab inline

def compare(symbol1, symbol2):
    #Date when to start and date when to end quote
    start = datetime.date.today() + relativedelta(months=-10) #get date 2 months prior to today
    end = datetime.date.today() #get today's date

    try:
        #get the quote of stocks through google finance
        quote = web.DataReader(symbol1, "google", start, end)
        quote2 = web.DataReader(symbol2, "google", start, end)
        #group stocks into panda dataframe so we can make secondary plot
        stocks = p.DataFrame({symbol1: quote["Close"],symbol2: quote2["Close"]})
        #plot size
        pylab.rcParams['figure.figsize'] = (13, 8)
        #secondary plot on right Y-Axis to better display both quotes together
        stocks.plot(secondary_y = symbol2, grid = True)

        print (quote.head())
        print (quote2.head())

        #create a list of measure need to be compared
        lst = ["Open","High","Low","Close","Volume",]
        #use the map function to get list of measures for both quotes
        dif = map(lambda x: (x,abs(np.mean(quote[x] - quote2[x]))),lst)

        #print the differences
        for i in dif:
            print ("Average Differences in", i[0],':', i[1])

    except:
        print ('wrong symbol typed! please type other stock symbols')
        compare(symbol1=input("Please give me a symbol: "), symbol2=input("Please give me another symbol: "))

compare(symbol1=input("Please give me a symbol: "), symbol2=input("Please give me another symbol: "))
