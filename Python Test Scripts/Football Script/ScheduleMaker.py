import json
import random
import pandas as pd
import numpy as np
import re


def roundRobin(teams,numFix):
	#numFix = numFix - 1 
	if(len(teams) % 2 != 0):
		teams.append('bye')
	numRounds = len(teams) - 1
	halfSize = len(teams) / 2

	for i in range(0,int(len(teams)-numFix)):

		fixed = teams[0:numFix] #fixed
		#print(fixed)
		move = teams[int(numFix)]
		rest = teams[int(numFix)+1:]
		rest.append(move)
		fixed.extend(rest)
		teams = fixed
		print(teams)

		for i in range(0,int(len(teams)-halfSize)):
			
			print(teams[i]+" vs "+teams[int(numRounds-i)])#+halfSize)]) #save into usable data structure
			#{"Round": i,
			# "games": [
				#team1: opponent,
				#team2: opponent,
				#team3: opponent,
				#team4: opponent,
				#team5: opponent,
				#team6: opponent,
				#team7: opponent]
			#},
	return teams
	#return RRdictionary
	
# teams = ['a','b','c','d','e','f']
# longteams = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14']
# longteams = roundRobin(longteams,7)

SECW = ['Alabama','Texas A&M','Ole Miss','Auburn','Miss St.','Arkansas','LSU']
SECE = ['Georgia','Kentucky','Tennessee','Florida','Mizzou','South Carolina','Vandy']
SEC = SECW + SECE


AAC = ['Cincinati','Houston','UCF','ECU','Tulsa','SMU','Memphis','Navy','Tulane','USF','Temple']
ACCatlantic = ['Wake Forest','NC State','Clemson','Louiville','FSU','Syracuse','Boston College']
ACCcoastal = ['Pitt','Miami','Virginia Tech','Virginia','UNC','Georgia Tech','Duke']
ACC = ACCatlantic + ACCcoastal
B12 = ['Oklahoma State','Baylor','OU','Iowa State','Kansas State','West Virginia','Texas','TCU','Texas Tech','Kansas']
B1Geast = ['Michigan','Ohio State','Michigan State','Penn State','Maryland','Rutgers','Indiana']
B1Gwest = ['Iowa','Minnesota','Wisconsin','Purdue','Illinois','Nebraska','Northwestern']
B1G = B1Gwest + B1Geast
#CUSA
#Independent
#MWC
#Pac12
#Sun Belt
FCSteams = ['potato boi']

FBS = SEC + AAC + ACC +  B12 + B1G
#print(FBS)

evens = [2,4,6,8,10]
odds = [1,3,5,7,9,11]
nums = evens + odds

def schedule(evens,odds,nums):
	available = nums
	for i in nums:
		print(available)
		conference = ''
		if i in odds:
			conference = 'odd'
			for j in odds:
				available.remove(k)
			r = random.randrange(0,len(available))
			oppponent = available[r]
			available.remove(oppponent)
			print(conference)
			print(available)
			print(oppponent)
			available = available + odd
			

		if j in evens:
			conference = 'even'
			for k in evens:
				available.remove(k)
			r = random.randrange(0,len(available))
			oppponent = available[r]
			available.remove(oppponent)
			print(conference)
			print(available)
			print(oppponent)
			available = available + evens

		#readd removed and remove self and opponent only
		#remove self and random team from list 

schedule(evens,odds,nums)

#roundRobin(SECWteams,1) #conference games. determines 7 of the 12 weeks
#roundRobin(SEC,7) #determines the random annual cross conference game for each team
#need 4 ooc games

#ACTUAL CODE

##Round Robins
#AI Out of Conference Round Robin
#Cross Division Annual Round Robin
#SEC West Round Robin
#SEC East Round Robin

##Rival Weeks
#FinalRivalWeek = 
#CrossDivisionRivalWeek =





# player is able to pick literally whoever they want to play. if this happens to a pair the other of the pair just plays a team playing an fcs opponent or an fcs opponent
#if tamu. i can not pick the sec as ooc. 


