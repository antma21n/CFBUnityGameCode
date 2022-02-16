#Ready for Unity integration

import random
import os

#Player Stats
recuitingPoints = 500;
week = 0

Manziel =  {"Name":'Johnny Manziel',
			"Position": 'QB',
			"StarRating": 4,
			"NumRating": 69,
			"Scouted": False,
			"School 1": 'Georgia',
			"School 1 Commitment": 10,
			"School 2": 'Texas A&M',
			"School 2 Commitment": 1000,
			"School 3": 'Ohio State',
			"School 3 Commitment": 10,
			"School 4": 'Alabama',
			"School 4 Commitment": 10,
			"School 5": 'Player',
			"School 5 Commitment": 5,
			"PointstoCommit": 1000,			
			"Commited": True,
			"Commited School": 'Texas A&M'
			}
Mond =  {"Name":'Kellen Mond',
			"Position": 'QB',
			"StarRating": 4,
			"NumRating": 70,
			"Scouted": False,
			"School 1": 'Georgia',
			"School 1 Commitment": 10,
			"School 2": 'Texas A&M',
			"School 2 Commitment": 10,
			"School 3": 'Ohio State',
			"School 3 Commitment": 10,
			"School 4": 'Alabama',
			"School 4 Commitment": 10,
			"School 5": 'Player',
			"School 5 Commitment": 5,
			"PointstoCommit": 1000,			
			"Commited": False,
			"Commited School": ''
			}
King =  {"Name":'Haynes King',
			"Position": 'QB',
			"StarRating": 4,
			"NumRating": 62,
			"Scouted": False,
			"School 1": 'Georgia',
			"School 1 Commitment": 10,
			"School 2": 'Texas A&M',
			"School 2 Commitment": 10,
			"School 3": 'Ohio State',
			"School 3 Commitment": 10,
			"School 4": 'Alabama',
			"School 4 Commitment": 10,
			"School 5": 'Player',
			"School 5 Commitment": 5,
			"PointstoCommit": 1000,			
			"Commited": False,
			"Commited School": ''
			}
Calzone =  {"Name":'Zach Calzada',
			"Position": 'QB',
			"StarRating": 3,
			"NumRating": 55,
			"Scouted": False,
			"School 1": 'Georgia',
			"School 1 Commitment": 10,
			"School 2": 'Texas A&M',
			"School 2 Commitment": 10,
			"School 3": 'Ohio State',
			"School 3 Commitment": 10,
			"School 4": 'Alabama',
			"School 4 Commitment": 10,
			"School 5": 'Player',
			"School 5 Commitment": 5,
			"PointstoCommit": 1000,			
			"Commited": False,
			"Commited School": ''
			}
Weigmen =  {"Name":'Connor Weigmen',
			"Position": 'QB',
			"StarRating": 5,
			"NumRating": 75,
			"Scouted": False,
			"School 1": 'Georgia',
			"School 1 Commitment": 10,
			"School 2": 'Texas A&M',
			"School 2 Commitment": 10,
			"School 3": 'Ohio State',
			"School 3 Commitment": 10,
			"School 4": 'Alabama',
			"School 4 Commitment": 10,
			"School 5": 'Player',
			"School 5 Commitment": 5,
			"PointstoCommit": 1000,			
			"Commited": False,
			"Commited School": ''
			}

RecruitList = [Mond, King, Calzone, Weigmen, Manziel]
#print(RecruitList)

def Commited():
	for i in range(0,len(RecruitList)):
		if RecruitList[i]['School 1 Commitment'] >= 1000:
			RecruitList[i]['Commited'] = True
			RecruitList[i]['Commited School'] = RecruitList[i]['School 1']
			RecruitList[i]['School 1 Commitment'] = 0
			print(RecruitList[i]['Name'] + " has commited to " + RecruitList[i]['School 1'] +'.')
		elif RecruitList[i]['School 2 Commitment'] >= 1000:
			RecruitList[i]['Commited'] = True
			RecruitList[i]['Commited School'] = RecruitList[i]['School 2']
			RecruitList[i]['School 2 Commitment'] = 0
			print(RecruitList[i]['Name'] + " has commited to " + RecruitList[i]['School 2'] +'.')
		elif RecruitList[i]['School 3 Commitment'] >= 1000:
			RecruitList[i]['Commited'] = True
			RecruitList[i]['Commited School'] = RecruitList[i]['School 3']
			RecruitList[i]['School 3 Commitment'] = 0
			print(RecruitList[i]['Name'] + " has commited to " + RecruitList[i]['School 3'] +'.')
		elif RecruitList[i]['School 4 Commitment'] >= 1000:
			RecruitList[i]['Commited'] = True
			RecruitList[i]['Commited School'] = RecruitList[i]['School 4']
			RecruitList[i]['School 4 Commitment'] = 0
			print(RecruitList[i]['Name'] + " has commited to " + RecruitList[i]['School 4'] +'.')
		elif RecruitList[i]['School 5 Commitment'] >= 1000:
			RecruitList[i]['Commited'] = True
			RecruitList[i]['Commited School'] = RecruitList[i]['School 5']
			RecruitList[i]['School 5 Commitment'] = 0
			print(RecruitList[i]['Name'] + " has commited to " + RecruitList[i]['School 5'] +'.')

def playerList(RecruitList):
	for i in range(0,len(RecruitList)):
		if RecruitList[i]['Commited'] == False:
			if RecruitList[i]['Scouted'] == False:
				print(str(i) + ' NAME: ' + RecruitList[i]['Name'] + " | Position: " + RecruitList[i]['Position'] + " | Star Rating: " + str(RecruitList[i]['StarRating']) + " | Commitment: " + str(RecruitList[i]['School 5 Commitment']) +'/1000')
			else:
				print(str(i) + ' NAME: ' + RecruitList[i]['Name'] + " | Position: " + RecruitList[i]['Position'] + " | Star Rating: " + str(RecruitList[i]['StarRating']) + " | Num Rating: " + str(RecruitList[i]['NumRating']) + " | Commitment: " + str(RecruitList[i]['School 5 Commitment']) +'/1000')

def fullplayerList(RecruitList):
	for i in range(0,len(RecruitList)):
		if RecruitList[i]['Scouted'] == False:
			print(str(i) + ' NAME: ' + RecruitList[i]['Name'] + " | Position: " + RecruitList[i]['Position'] + " | Star Rating: " + str(RecruitList[i]['StarRating']) + " | Commitment: " + str(RecruitList[i]['School 5 Commitment']) +'/1000')
		else:
			print(str(i) + ' NAME: ' + RecruitList[i]['Name'] + " | Position: " + RecruitList[i]['Position'] + " | Star Rating: " + str(RecruitList[i]['StarRating']) + " | Num Rating: " + str(RecruitList[i]['NumRating']) + " | Commitment: " + str(RecruitList[i]['School 5 Commitment']) +'/1000')

def specificPlayer(val):
	if RecruitList[val]['Commited'] == False:
		if RecruitList[val]['Scouted'] == False:
			print(str(val) + ' NAME: ' + RecruitList[val]['Name'] + " | Position: " + RecruitList[val]['Position'] + " | Star Rating: " + str(RecruitList[val]['StarRating'])+ " | Commitment: " + str(RecruitList[val]['School 5 Commitment']) +'/1000')
		else:
			print(str(val) + ' NAME: ' + RecruitList[val]['Name'] + " | Position: " + RecruitList[val]['Position'] + " | Star Rating: " + str(RecruitList[val]['StarRating']) + " | Num Rating: " + str(RecruitList[val]['NumRating']) + " | Commitment: " + str(RecruitList[val]['School 5 Commitment']) +'/1000')
		print(RecruitList[val]['School 1'] + ' ' + str(RecruitList[val]['School 1 Commitment']))
		print(RecruitList[val]['School 2'] + ' ' + str(RecruitList[val]['School 2 Commitment']))
		print(RecruitList[val]['School 3'] + ' ' + str(RecruitList[val]['School 3 Commitment']))
		print(RecruitList[val]['School 4'] + ' ' + str(RecruitList[val]['School 4 Commitment']))
	else:
		print(RecruitList[val]['Name'] + ' has commited to ' + RecruitList[val]['Commited School'] + '. They are no longer recruitable.')

def addPoints(weeklyPoints):
	playerIndex = int(input("Which Player: "))
	if playerIndex > len(RecruitList):
		print('this player does not exist')
	else:
		if RecruitList[playerIndex]['Commited'] == False:
			amount = int(input("How Many Points: ")) #throws error if not a integer. for code make this a thing.
			if amount > weeklyPoints:
				print('you do not have this many points available.')
			else:
				weeklyPoints = weeklyPoints - int(amount) #only if tempAmount is less than weeklypoints
				RecruitList[playerIndex]['School 5 Commitment'] = RecruitList[playerIndex]['School 5 Commitment'] + amount
		else:
			print('player has already commited to a team')
		#print(RecruitList[playerIndex]['School 5 Commitment'])
	return weeklyPoints

def AIaddPoints():
	for i in range(0,len(RecruitList)):
		if RecruitList[i]['Commited'] == False:
			RecruitList[i]['School 1 Commitment'] = RecruitList[i]['School 1 Commitment'] + random.randrange(-50,200)
			RecruitList[i]['School 2 Commitment'] = RecruitList[i]['School 2 Commitment'] + random.randrange(-50,200)
			RecruitList[i]['School 3 Commitment'] = RecruitList[i]['School 3 Commitment'] + random.randrange(-50,200)
			RecruitList[i]['School 4 Commitment'] = RecruitList[i]['School 4 Commitment'] + random.randrange(-50,200)

#new Week
## if player reached point threshold player commits
## if another team reaches point threshold player commits
## Add random points for each team to players 
## let player use points and distribute to each player
## let player scout players to unlock num rating 

#for i in range(0,len(completedata)):

while week < 13:
	#playerList(RecruitList)
	week = week + 1
	AIaddPoints()
	Commited()
	weeklyPoints = recuitingPoints
	print('##### WEEK: ' + str(week) + ' #####')
	while True:
		val = input("Type a Command: ")
		try:
			val = int(val)
		except:
			val = val
		if isinstance(val, int):
			try: 
				specificPlayer(val);
				#print(RecruitList[val])
			except:
				print("No player with index: " + str(val))
		if val == "list":
			playerList(RecruitList)
		if val == "full list":
			fullplayerList(RecruitList)
		if val == "points":
			print("You have " + str(weeklyPoints) + " points left over this week.")
		if val == "add points":
			#tempPlayer = int(input("Which Player: "))
			#tempAmount = int(input("How Many Points: "))
			#weeklyPoints = weeklyPoints - int(tempAmount) #only if tempAmount is less than weeklypoints
			weeklyPoints = addPoints(weeklyPoints)#tempPlayer,tempAmount)
			print("You have " + str(weeklyPoints) + " points left over this week.")
		if val == 'scout':
			if weeklyPoints >= 50:
				tempPlayer = int(input("Which Player: "))
				if RecruitList[tempPlayer]['Scouted'] == True:
					print('player has already been scouted.')
				else:
					weeklyPoints = weeklyPoints - 50 #only if tempAmount is less than weeklypoints
					print("Player scouted. You have " + str(weeklyPoints) + " points left over this week.")
					RecruitList[tempPlayer]['Scouted'] = True
			else:
				print('not enough points to scout. you need at least 50.')
		if val == "clear":
			os.system('cls||clear')
			print('##### WEEK: ' + str(week) + ' #####')
		if val == "next week":
			os.system('cls||clear')
			break

#to do
## at the end display which players commited to you
## add on the list which shows who is in the lead/who player commited too.


#for integration
## need a container for around 1000 players with star ratings and positions (need a script for this)
## need to code this script into c#
## when able, integratation recruiting into the team manager systems. 