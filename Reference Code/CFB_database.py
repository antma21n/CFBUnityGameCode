#this script will be used to help build a database for the unity code.
#not certain if a json structure or a scriptable object structure is best.
#this will be used for easy of input data in the future for teams.

#part 1: create a database for all FBS teams

#steps for part 1
#1. pull list of teams from completedata.json and schedules 
#2. count wins and loses
#3. rename FCS teams as generics (if team is not an fbs)
#4. give team offense, defense, special team, 
#4.5 NICE TO HAVE: give team thier coach ratings
#5. NICE TO HAVE: give team thier colors if possible 
#6. save as new json file with complete info.

import json
import random
import pandas as pd
import numpy as np
import re

#globals
gameData = []
gameDataDF = []
team = []
teams = []
schedule = []
results = []
wins = []
loses = []
offRating = []
defRating = []
offRanking = []
defRanking = []
overallRanking = []
#colors = []
#coach = [] #instead of coach Rating maybe it just has a star factor?
#players = []

f = open('C:/Anthony/Software Projects/CFB-Directed-Map/completedata.json')
completedata = json.load(f)

xl = pd.read_excel('C:/Anthony/Software Projects/CFB Game Code/sportsref_cfb.xlsx')
xl.index = xl["School"]
teams = xl["School"]
#print(xl["Rk"]["Georgia"])

xlOffense = pd.read_excel('C:/Anthony/Software Projects/CFB Game Code/sportsref_cfb_o.xlsx')
xlOffense.index = xlOffense["School"]
xlDefense = pd.read_excel('C:/Anthony/Software Projects/CFB Game Code/sportsref_cfb_d.xlsx')
xlDefense.index = xlDefense["School"]

#print(xl)
for i in range(0,len(completedata)):
	data = []
	team = xl["School"][i]
	
	#does not work weird names in old json
	#schedule = completedata[i]["opponents"] #need to include byes
	#results = completedata[i]["results"]
	
	#find wins and loses
	wins = int(xl["W"][team])
	loses = int(xl["L"][team])

	#sports reference data
	try:
		offRanking = int(xlOffense["Rk"][team])
		defRanking = int(xlDefense["Rk"][team])
		overallRanking = int(xl["Rk"][team])

		offRating = round( ((50 + float(xlOffense["Pts"][i])) + 100*(1 - offRanking/len(xl["School"])) )/2 ) #can use params like conference to help.
		defRating = round( ((100 - float(xlDefense["Pts"][i])) + 100*(1 - defRanking/len(xl["School"])) )/2 )
	except:
		print('cant find team',team)
		offRanking = []; defRanking=[]; overallRanking; offRating=40; defRating=40

	
	data = {"team":team,
			"colors": "",
			"W": wins,
			"L": loses,
			"schedule": schedule,
			"results": results,
			"Offense Rating": offRating,
			"Defense Rating": defRating,
			"Offense Ranking": offRanking,
			"Defense Ranking": defRanking,
			"Rank": overallRanking,
			}
	gameData.append(data)

gameDataDF = pd.DataFrame(gameData)
gameDataDF.index = gameDataDF["team"]
with open('gameData.json', 'w') as gD:
    json.dump(gameData, gD, indent=4)

#test


#part 2: simulate a season week to week and update results in json format

#steps for part 2
#1. random game simulation
#1.1 pull home team and stats and pull away team and stats
#1.2 teamXScore = (0.45 * offenseRating + 0.4 * defenseRating + 0.05 * specialRating) * homeModifier=1.2 * varianceModifiers
#1.3 calculate who wins ie. (team1Score > team2Score) 
#1.4 varianceModifier = random(0,1) + 1

#test to calculate who wins
def simulateGame(team1Name,team2Name,gameDataDF):
	
	team1 = gameDataDF[gameDataDF["team"].str.contains(team1Name)]
	team2 = gameDataDF[gameDataDF["team"].str.contains(team2Name)] #need to deal with multiple teams having word alabama in it
	#print(team1, team2)
	if len(team1) > 1:
		narks = team1
		for i in range(0,len(team1)):
			if str(team1["team"][i]) != team1Name:
				narks = narks.drop(str(team1["team"][i]))
		team1 = narks
	#print(team1)

	if len(team2) > 1:
		po = team2
		for i in range(0,len(team2)):
			if str(team2["team"][i]) != team2Name:
				po = po.drop(str(team2["team"][i]))
		team2 = po
	#print(team2)

	homeModifier  = 1.2
	varianceModifier1 = random.randrange(0,100) / 100 + 1
	team1Score = (0.5 * float(team1["Offense Rating"])) + (0.5 * float(team1["Defense Rating"])) * homeModifier * varianceModifier1
	#need to generate a gameScore

	varianceModifier2 = random.randrange(0,100) / 100 + 1
	#print(team2["Offense Rating"])
	#print(team2["Defense Rating"])
	#issue here with 'empty dataframe for some entries. idk what it means'
	team2Score = (0.5 * float(team2["Offense Rating"])) + (0.5 * float(team2["Defense Rating"])) * varianceModifier2
	#need to generate a gameScore 

	if(team1Score > team2Score):
		print(team1Name,' Beat ', team2Name)
	else:
		print(team2Name,' Beat ', team1Name)

#simulateGame("Texas A&M","Alabama",gameDataDF)


#2. Schedule Creation
def week1Schedule(teams):
	matchUps = []
	t = teams.values.tolist()
	week1 = teams.values.tolist()
	for i in range(0,len(t)):
		matchup = []
		#if len(week1) > 0: #if found find opponent, otherwise remove.
		try:
			week1.remove(t[i])
			try:
				r = random.randrange(0,len(week1))
				#matchup = {t[i]:[week[r]]} #### MAKE DATA FRAME. colume is team, row is opponent from 1st to last.
				matchup = [t[i],week1[r]]
				matchUps.append(matchup) #### instead of dictionary. add row to dataframe. 
				week1.remove(week1[r])
			except:
				r = 0
				matchup = {t[i]:[week1[r]]} 
				matchUps.append(matchup)
				week1.remove(week1[r])
		except:
			#print(t[i]," was removed.")
			x=1
		#week1 = list(filter(lambda a: a != t[i], week1))
	return matchUps


#find next opponent do not repeat a game
def weekXSchedule(teams,weekx):
	matchUps = []
	t = teams.values.tolist()
	week = teams.values.tolist()
	for i in range(0,len(t)):
		matchup = []
		try:
			week.remove(t[i])
			#remove thier previous opponents. readd later
			#week1 = list(filter(lambda a: a != t[i], week1))
			try:
				r = random.randrange(0,len(week))
				preOpponents = weekx[i]
				#print(t[i])
				#print(preOpponents) #this does not work but makes sense t is still the entire 130 team list. weekx is half of the list with thier matchup. 
				#need to someone check match ups to see if it already exists. maybe using dataframes is better than dictionaries
				matchup = {t[i]:[week[r]]}
				matchUps.append(matchup)
				week.remove(week[r])
			except:
				r=0
				matchup = {t[i]:[week[r]]}
				matchUps.append(matchup)
				week.remove(week[r])
				#add previous opponents that where removed. do not readded all opponents, just ones that were removed above
		except:
			#print(t[i]," was removed.")
			x=1
	return matchUps

#print(week1MatchUps[1]["Alabama"])
# for i in range(0,12):
# 	if i == 0:
# 		weekx = week1MatchUps
# 		else
# 	weekx = weekXSchedule(teams,week1MatchUps)
#weekx = weekXSchedule(teams,week1MatchUps)

#print(week1MatchUps)
#print(weekx)


#3. complete week simulation
#3.1 pull first team in Teams.json and needed stats
#3.2 pull opponent and stats 
#3.3 simulate game using step 1
#3.4 when oponent is pulled do not resimulate this game. keep results from actual simulation and update.

#week1MatchUps = week1Schedule(teams)
#print(week1MatchUps)
for i in range(0,len(week1MatchUps)):
	try:
		simulateGame(week1MatchUps[i][0],week1MatchUps[i][1],gameDataDF)
	except:
		print('type error')
		#just force a team to win. This probably is not gonna be relevant for unity code.
	#add a w or l for week1game in the gameDataDF. again hard to do here but easy for unity