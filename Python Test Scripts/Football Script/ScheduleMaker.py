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
			print(teams[i]+" vs "+teams[int(i+halfSize)]) #save into usable data structure
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

SECWteams = ['Alabama','Texas A&M','Ole Miss','Arkansas','Miss St.','Arkansas','LSU']
SECEteams = ['Georgia','Kentucky','Tennessee','Florida','Mizzou','South Carolina','Vandy']
SECteams = SECWteams + SECEteams
FBSteams = []

roundRobin(SECWteams,1)
#ACTUAL CODE

##Round Robins
#AI Out of Conference Round Robin
#Cross Division Annual Round Robin
#SEC West Round Robin
#SEC East Round Robin

##Rival Weeks
#FinalRivalWeek = 
#CrossDivisionRivalWeek =