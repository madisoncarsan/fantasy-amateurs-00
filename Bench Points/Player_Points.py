# Bench Player Points

"""Returns how many points a member left on the bench in a 
selected position (could be whole team) for a given period 
of time (one week to whole season)
"""

from espn_api.football import League 
from espn_api.football import Player 
from espn_api.football import BoxPlayer

league = League(league_id=51591979, year=2021, espn_s2='AEBjEqbBxjZIt45ocr9eFgbp%2FBkWyQmzCIuNSsyI4jmQqhhxc2s5mnRJxHr5QOc576BaF1ULvFqeeTZoM%2FHg%2FS%2FHS1beH7XX8aP4uLisyHbr1SkANX42Es7E%2BZuq%2FXqKmSDMSVTYTMF3ctf%2FKmVMapTGJNkADWmsEoTHoIT8QTdj80aENnYeygi7DGqIDjrcCbLVfcWxUWp3jKqxQRP1744e88mki7wkLuNydGGonvYuPlrfcsDCEFY%2FVpkoq9lc%2FKm0mBdoWAiWsMeb7B3w5c25',swid='{7EDF6E52-328E-4864-9E53-6190364DDF91}')

#This function returns the points that a player scored based on the league, team, player, and gameweek
def Player_Points(league_info, team_num, roster_num, gameweek):

	global player_name
	player_name = league_info.teams[team_num].roster[roster_num].name
	return league_info.teams[team_num].roster[roster_num].stats[gameweek]['points']


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

	#Calculate the difference and format to 2 decimals
	difference = float("{:.2f}".format(highest_scorer.points - starter.points))

	return difference

	# if (highest_scorer.slot_position == 'BE') and (difference != 0):
	# 	result = difference

	# elif highest_scorer == starter:
	# 	result = [highest_scorer, 0, "Right"]

	return result

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

	#Calculate the difference and format to 2 decimals
	difference = float("{:.2f}".format(highest_scorer.points - starter.points))

	return difference

	# if (highest_scorer.slot_position == 'BE') and (difference != 0):
	# 	result = [highest_scorer, difference, "Wrong"]

	# elif highest_scorer == starter:
	# 	result = [highest_scorer, 0, "Right"]

	# return result

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

	#Calculate the difference and format to 2 decimals
	difference = float("{:.2f}".format(highest_scorer.points - starter.points))

	return difference

	# if (highest_scorer.slot_position == 'BE') and (difference != 0):
	# 	result = [highest_scorer, difference, "Wrong"]

	# elif highest_scorer == starter:
	# 	result = [highest_scorer, 0, "Right"]

	# return result

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

	The_rest = All_RB[2:] + All_WR[2:] + All_TE[1:]

	The_best = All_RB[:2] + All_WR[:2]

	The_best.append(All_TE[0])

	#Sort that list to get the top scorer
	The_rest.sort(key=lambda x: x.points, reverse=True)

	best_of_the_rest = The_rest[0]

	The_best.append(best_of_the_rest)

	#Calculates the total points in a list of players
	def Position_Calc(Position_List):
		total_score = 0.0

		for p in Position_List:
			total_score = total_score + p.points

		return total_score


	Flex_Position_Differential = Position_Calc(The_best) - Position_Calc(starters)

	return float("{:.2f}".format(Flex_Position_Differential))


def Total_Points_Left_On_Bench(team):
	QB = QB_Comparison(team)
	Flex = Flex_Comparison(team)
	DST = DST_Comparison(team)
	K = K_Comparison(team)

	total = QB + Flex + DST + K
	return float("{:.2f}".format(total))

# week = int(input("Select a game week: "))
# matchup = int(input("Select a matchup by # (0-5): "))
# home_away = input("Home or away team?: ")

# check = False

# while check == False:

# 	if home_away == "home":
# 		specified_team = specified_team = league.box_scores(week)[matchup].home_lineup
# 		check = True
# 		continue

# 	elif home_away == "away":
# 		specified_team = specified_team = league.box_scores(week)[matchup].away_lineup
# 		check = True
# 		continue

# 	home_away = input("Please type home or away: ")



# print (Total_Points_Left_On_Bench(specified_team))
