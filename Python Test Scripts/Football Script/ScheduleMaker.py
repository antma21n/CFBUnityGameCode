
def roundRobin(teams,numFix):
	#numFix = numFix - 1 
	if(len(teams) % 2 != 0):
		teams.append('bye')
	numRounds = len(teams) - 1
	halfSize = len(teams) / 2

	for i in range(0,int(len(teams)-numFix)):

		fixed = teams[0:numFix] #fixed
		print(fixed)
		move = teams[int(numFix)]
		rest = teams[int(numFix)+1:]
		rest.append(move)
		fixed.extend(rest)
		teams = fixed
		print(teams)

		for i in range(0,int(len(teams)-halfSize)):
			print("team "+teams[i]+" vs "+"team "+teams[int(i+halfSize)]) #save into usable data structure


	return teams
	
teams = ['a','b','c','d','e','f']
longteams = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14']
longteams = roundRobin(longteams,7)



#ACTUAL CODE

##Round Robins
#AI Out of Conference Round Robin
#Cross Division Annual Round Robin
#SEC West Round Robin
#SEC East Round Robin

##Rival Weeks
#FinalRivalWeek = 
#CrossDivisionRivalWeek =