import random
import json

def getConference(id):
    if id == 0:
        return "SEC"
    if id == 1:
        return "B1G"
    if id == 2:
        return "BIG12"
    if id == 3:
        return "PAC12"
    if id == 4:
        return "AAC"
def getDivision(id):
    if id == 0:
        return "d1"
    if id == 1:
        return "d2"
def isOOCRival(id):
    if id == 0:
        return False
    if id == 1:
        return True


gTeamIndex = {
    "Alabama": 0,
    "Texas A&M": 1,
    "Ole Miss": 2,
    "Auburn": 3,
    "Miss St.": 4,
    "Arkansas": 5,
    "LSU": 6,
    "Georgia": 7,
    "Kentucky": 8,
    "Tennessee": 9,
    "Florida": 10,
    "Mizzou": 11,
    "South Carolina": 12,
    "Vandy": 13,
    "Wake Forest": 14,
    "NC State": 15,
    "Clemson": 16,
    "Louiville": 17,
    "FSU": 18,
    "Syracuse": 19,
    "Boston College": 20,
    "Pitt": 21,
    "Miami": 22,
    "Virginia Tech": 23,
    "Virginia": 24,
    "UNC": 25,
    "Georgia Tech": 26,
    "Duke": 27,
    "Oklahoma State": 28,
    "Baylor": 29,
    "OU": 30,
    "Iowa State": 31,
    "Kansas State": 32,
    "West Virginia": 33,
    "Texas": 34,
    "TCU": 35,
    "Texas Tech": 36,
    "Kansas": 37,
    "Iowa": 38,
    "Minnesota": 39,
    "Wisconsin": 40,
    "Purdue": 41,
    "Illinois": 42,
    "Nebraska": 43,
    "Northwestern": 44,
    "Michigan": 45,
    "Ohio State": 46,
    "Michigan State": 47,
    "Penn State": 48,
    "Maryland": 49,
    "Rutgers": 50,
    "Indiana": 51
}
gTeamInfo = {
    "Alabama": [0,0,"Auburn",0],
    "Texas A&M": [0,0,"LSU",0],
    "Ole Miss": [0,0,"Miss St.",0],
    "Auburn": [0,0,"Alabama",0],
    "Miss St.": [0,0,"Ole Miss",0],
    "Arkansas": [0,0,"Mizzou",0],
    "LSU": [0,0,"Texas A&M",0],
    "Georgia": [0,1,"Georgia Tech",1],
    "Kentucky": [0,1,"",0],
    "Tennessee": [0,1,"",0],
    "Florida": [0,1,"",0],
    "Mizzou": [0,1,"",0],
    "South Carolina": [0,1,"",0],
    "Vandy": [0,1,"",0],
    "Wake Forest": [4,0,"",0],
    "NC State": [4,0,"",0],
    "Clemson": [4,0,"",0],
    "Louiville": [4,0,"",0],
    "FSU": [4,0,"",0],
    "Syracuse": [4,0,"",0],
    "Boston College": [4,0,"",0],
    "Pitt": [4,1,"",0],
    "Miami": [4,1,"",0],
    "Virginia Tech": [4,1,"",0],
    "Virginia": [4,1,"",0],
    "UNC": [4,1,"",0],
    "Georgia Tech": [4,1,"",0],
    "Duke": [4,1,"",0],
    "Oklahoma State": [2,0,"",0],
    "Baylor": [2,0,"",0],
    "OU": [2,0,"",0],
    "Iowa State": [2,0,"",0],
    "Kansas State": [2,0,"",0],
    "West Virginia": [2,0,"",0],
    "Texas": [2,0,"",0],
    "TCU": [2,0,"",0],
    "Texas Tech": [2,0,"",0],
    "Kansas": [2,0,"",0],
    "Iowa": [2,0,"",0],
    "Minnesota": [1,0,"",0],
    "Wisconsin": [1,0,"",0],
    "Purdue": [1,0,"",0],
    "Illinois": [1,0,"",0],
    "Nebraska": [1,0,"",0],
    "Northwestern": [1,0,"",0],
    "Michigan": [1,1,"",0],
    "Ohio State": [1,1,"",0],
    "Michigan State": [1,1,"",0],
    "Penn State": [1,1,"",0],
    "Maryland": [1,1,"",0],
    "Rutgers": [1,1,"",0],
    "Indiana": [1,1,"",0]
}
#dict = {
# "team": [confluence,division,rival,OOCRivalBool]
# "Texas A&M": [iSEC,iSECW,iLSU,0] //if OOCRivalBool = 0, curate 3 ooc games, when playing rival during round robin add bye week
# "South Carolina": [iSEC,iSECE,iClemson,1] //if OOCRivalBool = 1, only curate 2 ooc games, third is a bye do team can fit rival in final week
# }

teamlist = []

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

con1 = ["A1","B1","C1","D1"]
con2 = ["A2","B2","C2","D2"]
con3 = ["A3","B3","C3","D3","E3"]
con4 = ["A4","B4","C4","D4","E4"]
teamlist.extend(SEC)
teamlist.extend(ACC)
teamlist.extend(B12)
teamlist.extend(B1G)

rules = {}
for i in teamlist:
    team = {i:[]}
    rules.update(team)
seasonLen = 8

#rules
 #ConN must play all opponents
 #ConN must play at least 2 other opponents
 #ConN must have at least 1 bye week

#update rules
def updateRules(team,opp):
    x = []
    for i in rules[team]:
        x.append(i)
    x.append(opp)
    teamUpdate = {team:x}
    rules.update(teamUpdate)

#Draw out of conference opponents
def getOOConference(week):
    picked_exclude = [] #depending on team there should be special excludes
    count = 0
    for team in teamlist:
        to_exclude = []
        con_exclude = []
        for i in teamlist:
            if gTeamInfo[i][0] == gTeamInfo[team][0]:
                con_exclude.append(gTeamIndex[i])
        to_exclude.extend(con_exclude)
        to_exclude.extend(picked_exclude)
        to_exclude = list(set(to_exclude))
        hangCount = 0
        findingOpp = True
        if len(rules[team]) > week:
            findingOpp = False
        while findingOpp:
            if hangCount > 1000:
                updateRules(team,"FCS")
                picked_exclude.append(count)
                count+=1
                findingOpp = False
            hangCount += 1
            isOpp = True
            isValidOpp = True
            #print(to_exclude)
            randInt = random.choice(list(set([x for x in range(0, len(teamlist))]) - set(to_exclude)))
            opp = teamlist[randInt]

            if opp == team:
                isOpp = False
            # if getConference(id) == getConference(id):
            #     print("true")
            if isOpp:
                #Check team schedule to see if opponent is Unique
                for preOpp in rules[team]:
                    if opp == preOpp:
                        isValidOpp = False
                if len(rules[opp]) > week:
                    isValidOpp = False
            else:
                isValidOpp = False
            if isValidOpp:
                updateRules(team,opp)
                updateRules(opp,team)
                to_exclude.append(randInt)
                to_exclude.append(count)
                count+=1
                findingOpp = False
    return week

def roundRobin(teams,numFix,rounds):
    #numFix = numFix - 1 
    count = 0
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
        #print(teams)
        if rounds > count:
            for i in range(0,int(len(teams)-halfSize)):
                #print(teams[i]+" vs "+teams[int(numRounds-i)])
                if teams[i] != 'bye':
                    updateRules(teams[i],teams[int(numRounds-i)])
                if teams[int(numRounds-i)] != 'bye':
                    updateRules(teams[int(numRounds-i)],teams[i])
        count +=1
    return teams

#OOC
getOOConference(0)
getOOConference(1)
getOOConference(2)

#SEC
roundRobin(SECW,1,50)
roundRobin(SECE,1,50)
roundRobin(SEC,7,2)

#B1G
roundRobin(B1Gwest,1,50)
roundRobin(B1Geast,1,50)
roundRobin(B1G,7,3)

#B12
roundRobin(B12,1,50)

print(rules)

with open("teams.json", "w") as fp:
    json.dump(rules , fp, indent = 4)

# teamindex = {}
# c=0
# for i in teamlist:
#     team = {i:c}
#     teamindex.update(team)
#     c+=1

# with open("teamsids.json", "w") as fp:
#     json.dump(teamindex , fp, indent = 4)
