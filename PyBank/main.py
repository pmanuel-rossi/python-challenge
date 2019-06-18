# Bank homework

#packages

import pandas as pd
import numpy as np

bankPath = r'/Users/pedrorossi/Documents/GitHub/python-challenge/PyBank/resources'

bankFile = '/Week 3 - Python-Homework-Instructions-PyBank-Resources-budget_data.csv'

bankDB = pd.read_csv(bankPath + bankFile)

#Number of months 

months = len(bankDB)

print('Number of months: ' + str(months))

#total Profit / loss

totalProfit = bankDB['Profit/Losses'].sum()

print('Total: $' + str(totalProfit))

#average change

profitLossesList = list(bankDB['Profit/Losses'])
dateProfitLossesList = bankDB['Date']

changeList = []
counter = 0

numDB = np.array(dateProfitLossesList)
date = ""

for i in range(len(bankDB)-1):
    curr = profitLossesList[i]
    currDown = profitLossesList[i+1]
    changeList.append(currDown-curr)
    counter = sum(bankDB['Profit/Losses'])
    minChange = min(changeList)
    maxChange = max(changeList)  
    avgChance = round(np.mean(changeList),2)
    if i == minChange - maxChange:
        date = numDB[i]

avgChange = round(np.mean(changeList), 2)
        
print('Average change: $' + str(avgChange))

#Greatest increase in profits

changeList.insert(0, 0)

bankDB['Change'] = changeList

changeDB = bankDB[['Date', 'Change']].copy()

maxIncrease = changeDB.loc[changeDB['Change'] == max(changeDB['Change'])]

print('Greatest Increase in Profits: ' + str(maxIncrease['Date'].item()) + ' ($' + str(maxIncrease['Change'].item()) + ')')

maxDecrease = changeDB.loc[changeDB['Change'] == min(changeDB['Change'])]

print('Greatest Decrease in Profits: ' + str(maxDecrease['Date'].item()) + ' ($' + str(maxDecrease['Change'].item()) + ')')


