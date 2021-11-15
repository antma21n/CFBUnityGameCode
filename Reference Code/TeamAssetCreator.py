import json
import random
import pandas as pd
import numpy as np
import re

f = open('C:/Unity Games/CFBUnityGameCode/Reference Code/gameData.json')
gameData = json.load(f)
f.close()
print(gameData)

teams = []
#for i in range(0,3):
for i in range(0,len(gameData)):
	f = open("C:/Unity Games/CFB Mobile Game/Assets/Scriptable Objects/Teams/txts/"+gameData[i]["team"]+".txt", "w")
	# string =(" %YAML 1.1\n"+
	# 		"%TAG !u! tag:unity3d.com,2011:\n"+
	# 		"--- !u!114 &11400000\n"+
	# 		"MonoBehaviour:\n"+
	# 		"  m_ObjectHideFlags: 0\n"+
	# 		"  m_CorrespondingSourceObject: {fileID: 0}\n"+
	# 		"  m_PrefabInstance: {fileID: 0}\n"+
	# 		"  m_PrefabAsset: {fileID: 0}\n"+
	# 		"  m_GameObject: {fileID: 0}\n"+
	# 		"  m_Enabled: 1\n"+
	# 		"  m_EditorHideFlags: 0\n"+
	# 		"  m_Script: {fileID: 11500000, guid: 8630ca49a9400bc4a8353b643ad56ed5, type: 3}\n"+
	# 		"  m_Name: Georgia\n"+
	# 		"  m_EditorClassIdentifier: \n"+
	# 		"  name: Georgia\n"+
	# 		"  primaryColor: \n"+
	# 		"  secondaryColor: \n"+
	# 		"  wins: 9\n"+
	# 		"  loses: 0\n"+
	# 		"  OffenseRating: 93\n"+
	# 		"  DefenseRating: 96\n"+
	# 		"  OffenseRanking: 14\n"+
	# 		"  DefenseRanking: 1\n"+
	# 		"  Rank: 1\n")
	teams.append(gameData[i]["team"])
	string =(gameData[i]["team"]+"\n"+
			str(gameData[i]["W"])+"\n"+
			str(gameData[i]["L"])+"\n"+
			str(gameData[i]["Offense Rating"])+"\n"+
			str(gameData[i]["Defense Rating"])+"\n"+
			str(gameData[i]["Offense Ranking"])+"\n"+
			str(gameData[i]["Defense Ranking"])+"\n"+
			str(gameData[i]["Rank"]))
	#print(string)
	f.write(string)
	f.close()

f = open("C:/Unity Games/CFB Mobile Game/Assets/Scriptable Objects/Teams/txts/teamlist.txt", "w")
for i in range(0,len(teams)):
	f.write(teams[i]+"\n")
f.close()