# Bench Player Points

"""Returns how many points a member left on the bench in a 
selected position (could be whole team) for a given period 
of time (one week to whole season)
"""

from espn_api.football import League 
from espn_api.football import Player 
from espn_api.football import BoxPlayer

from Team_Class import Team_Class

league = League(league_id=51591979, year=2021, espn_s2='AEBjEqbBxjZIt45ocr9eFgbp%2FBkWyQmzCIuNSsyI4jmQqhhxc2s5mnRJxHr5QOc576BaF1ULvFqeeTZoM%2FHg%2FS%2FHS1beH7XX8aP4uLisyHbr1SkANX42Es7E%2BZuq%2FXqKmSDMSVTYTMF3ctf%2FKmVMapTGJNkADWmsEoTHoIT8QTdj80aENnYeygi7DGqIDjrcCbLVfcWxUWp3jKqxQRP1744e88mki7wkLuNydGGonvYuPlrfcsDCEFY%2FVpkoq9lc%2FKm0mBdoWAiWsMeb7B3w5c25',swid='{7EDF6E52-328E-4864-9E53-6190364DDF91}')

#This function returns the points that a player scored based on the league, team, player, and gameweek
def Player_Points(league_info, team_num, roster_num, gameweek):

	global player_name
	player_name = league_info.teams[team_num].roster[roster_num].name
	return league_info.teams[team_num].roster[roster_num].stats[gameweek]['points']

# x = Player_Points(league, 0, 0, 17)

# print (player_name + ": " + str(x))

#This function simply spits out whether you made the right play or not between 2 guys
def Player_Points_Comparison(player_1_pts, player_2_pts):
	if player_1_pts >= player_2_pts:
		return "You made the right play!"
	else:
		return "You should've started the other guy!"

# print (Player_Points_Comparison(5,3))

#Sorts players into a dictionary or positions
def Position_Check(player_list):

	#Create empty position dictionary
	position_dict = {'QB':[],'WR':[],'RB':[],'TE':[],'D/ST':[],'K':[]}

	#Go through roster
	for x in player_list:
		#Compare player to each of the position lists
		for key in position_dict.keys():
			#If the position is the same, sort player into that list
			if str(x.position) == str(key):
				position_dict[key].append(x)

	return position_dict

#print (league.box_scores(12)[0].home_lineup)
# print (league.box_scores(12)[0].home_lineup[5].name)
# print (league.box_scores(12)[0].home_lineup[5].points)
# print (league.box_scores(12)[0].home_lineup[5].slot_position)

#Compare the bench performance of positions to starters
def QB_Comparison(team):

	#Run Position Check to build roster sorted by position
	position_roster = Position_Check(team)

	#Check if correct player was played in each slot
	highest_scorer = None
	starter = None

	for p in position_roster['QB']:

		if p.slot_position == 'QB':
			starter = p

		#Replace the highest scorer slot with the highest score
		if highest_scorer == None or p.points > highest_scorer.points:
			highest_scorer = p

	difference = highest_scorer.points - starter.points

	if (highest_scorer.slot_position == 'BE') and (difference != 0):
		print ('You made the wrong move: ' + highest_scorer.name + " scored " + str(difference) + " more points than " + starter.name)

	elif highest_scorer == starter:
		print ('You made the right play with ' + starter.name + ' at ' + starter.slot_position)

def DST_Comparison(team):

	#Run Position Check to build roster sorted by position
	position_roster = Position_Check(team)

	#Check if correct player was played in each slot
	highest_scorer = None
	starter = None

	for p in position_roster['D/ST']:

		if p.slot_position == 'D/ST':
			starter = p

		#Replace the highest scorer slot with the highest score
		if highest_scorer == None or p.points > highest_scorer.points:
			highest_scorer = p

	difference = highest_scorer.points - starter.points

	if (highest_scorer.slot_position == 'BE') and (difference != 0):
		print ('You made the wrong move: ' + highest_scorer.name + " scored " + str(difference) + " more points than " + starter.name)

	elif highest_scorer == starter:
		print ('You made the right play with ' + starter.name + ' at ' + starter.slot_position)

def K_Comparison(team):

	#Run Position Check to build roster sorted by position
	position_roster = Position_Check(team)

	#Check if correct player was played in each slot
	highest_scorer = None
	starter = None

	for p in position_roster['K']:

		if p.slot_position == 'K':
			starter = p

		#Replace the highest scorer slot with the highest score
		if highest_scorer == None or p.points > highest_scorer.points:
			highest_scorer = p

	difference = highest_scorer.points - starter.points

	if (highest_scorer.slot_position == 'BE') and (difference != 0):
		print ('You made the wrong move: ' + highest_scorer.name + " scored " + str(difference) + " more points than " + starter.name)

	elif highest_scorer == starter:
		print ('You made the right play with ' + starter.name + ' at ' + starter.slot_position)

def Flex_Comparison(team):

	#Run Position Check to build roster sorted by position
	position_roster = Position_Check(team)

	#Separate lists for RBs and WR's
	All_RB = []
	All_WR = []
	All_TE = []

	The_rest = []

	starters = []

	#Create lists for all positions and a list of starters

	for p in position_roster['RB']:

		All_RB.append(p)

		if (p.slot_position == 'RB') or (p.slot_position == 'RB/WR/TE'):
			starters.append(p)

	for p in position_roster['WR']:

		All_WR.append(p)

		if (p.slot_position == 'WR') or (p.slot_position == 'RB/WR/TE'):
			starters.append(p)

	for p in position_roster['TE']:

		All_TE.append(p)

		if (p.slot_position == 'TE') or (p.slot_position == 'RB/WR/TE'):
			starters.append(p)


	#Sort each list by points scored so that the top scorers are at the beginning of each list

	All_RB.sort(key=lambda x: x.points, reverse=True)

	All_WR.sort(key=lambda x: x.points, reverse=True)

	All_TE.sort(key=lambda x: x.points, reverse=True)

	#Take the highest scorers and put them in their own lists

	RB_highest = All_RB[:2]

	WR_highest = All_WR[:2]

	TE_highest = All_TE[0]

	#Put the rest into a list of their own

	count = 2

	while count < len(All_RB):
		The_rest.append(All_RB[count])
		count = count + 1

	count = 2

	while count < len(All_WR):
		The_rest.append(All_WR[count])
		count = count + 1

	count = 1

	while count < len(All_TE):
		The_rest.append(All_TE[count])
		count = count + 1

	#Sort that list to get the top scorer
	The_rest.sort(key=lambda x: x.points, reverse=True)

	best_of_the_rest = The_rest[0]

	#next thing to do is to show if the players were played in the right positions


# QB_Comparison(league.box_scores(12)[0].home_lineup)

# TE_Comparison(league.box_scores(12)[0].home_lineup)

# DST_Comparison(league.box_scores(12)[0].home_lineup)

# K_Comparison(league.box_scores(12)[0].home_lineup)

Flex_Comparison(league.box_scores(13)[0].home_lineup)





# for x in league.box_scores(12)[0].home_lineup:
# 	print(x.name)
# 	print ("eligible for : "+ x.position)
# 	print ("played at: "+ x.slot_position)
