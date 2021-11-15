#proof of concept for game manager script

#Current missing components
	# clock
	# simulation of defensive plays

#starting variables
startLine = 20
down = 1
yardsToGo = 10
team1Score = 0
team2Score = 0
		
#offense
while True:
	yards = input ("Yards This Play: ")
	print ("Player ran for:", yards, "yard(s)") 

	yardsToGo -= int(yards)
	startLine += int(yards)
	if startLine == 0:
		print("SAFETY")
		break
	if startLine >= 100:
		print("TOUCH DOWN")
		team1Score += 7
		print("Score: ",team1Score,"-",team2Score)
		break	
	print ("Offense on", startLine, "yard line")
	
	if yardsToGo > 0:
		down += 1
		if down == 4:
			print("Turn over on downs")
			break
	else:
		down = 1
		yardsToGo = 10
	print ("It is",down,"down and",yardsToGo)