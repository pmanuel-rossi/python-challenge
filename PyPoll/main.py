#Poll homework

#packages

import pandas as pd

pollPath = r'/Users/pedrorossi/Documents/GitHub/python-challenge/PyPoll/resources'

pollFile = '/Week 3 - Python-Homework-Instructions-PyPoll-Resources-election_data.csv'

pollDF = pd.read_csv(pollPath + pollFile)

#title

print('Election Results')

print('--------------------------')

#Total votes

totalVotes = len(pollDF)

print('Total Votes: ' + str(totalVotes))

print('--------------------------')

#Khan Voting

khanDF = pollDF[pollDF['Candidate'] == 'Khan']

khanVotes = len(khanDF)

khanPerc = round((khanVotes / totalVotes) * 100, 4)
 
print('Khan Votes : ' + str(khanPerc) + '% (' + str(khanVotes) + ')')

#Correy votes

correyDF = pollDF[pollDF['Candidate'] == 'Correy']

correyVotes = len(correyDF)

correyPerc = round((correyVotes / totalVotes) * 100, 4)

print('Correy Votes : ' + str(correyPerc) + '% (' + str(correyVotes) + ')')

#Li votes

liDF = pollDF[pollDF['Candidate'] == 'Li']

liVotes = len(liDF)

liPerc = round((liVotes / totalVotes) * 100, 4)

print('Li Votes : ' + str(liPerc) + '% (' + str(liVotes) + ')')

#O'Tooley voting

otooleyDF = pollDF[pollDF['Candidate'] == "O'Tooley"]

otooleyVotes = len(otooleyDF)

otooleyPerc = round((otooleyVotes / totalVotes) * 100, 4)

print("O'Tooley Votes : " + str(otooleyPerc) + '% (' + str(otooleyVotes) + ')')

print('--------------------------')

#Winner

winner = pollDF.Candidate.mode().item()

print('Winner: ' + str(winner))