# Author: Tiffany Weller
# Date 04/05/2023


import csv
import operator
import os
DEBUG = False
temp = ""
candidatelist = []
candidates = {}
i = 0
Winner = 0
tempvotes = 0
tempcandidate = ""


with open(r"C:\Users\mbannon\Desktop\python-challenge\PyPoll\Resources\election_data.csv") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)
    results = sorted(csv_reader,key=operator.itemgetter(2))     
    VotesCount = 0
    for row in results:
        candidate = row[2]
        VotesCount += 1
        tempvotes += 1
        if candidate not in candidates:   
            candidates[candidate] = 0 
            candidatelist.append(candidate)
        candidates[candidate] += 1
               

#Print Election Results
print(candidates)
print(candidatelist)
print("Election Results")
print("-------------------------------")
print()
print("Total Votes: " + str(VotesCount) )
print()
print("-------------------------------")
#print(f"{candidates['Khan'].key()}")
print("-------------------------------")
print("Winner: ")
print("-------------------------------")