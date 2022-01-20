#Team_Pathing.py

"""
Figure out a way to path through and find the same team across weeks

"""

from espn_api.football import League 
from espn_api.football import Player 
from espn_api.football import BoxPlayer

from Team_Class import Team_Class
from Player_Points import *

league = League(league_id=51591979, year=2021, espn_s2='AEBjEqbBxjZIt45ocr9eFgbp%2FBkWyQmzCIuNSsyI4jmQqhhxc2s5mnRJxHr5QOc576BaF1ULvFqeeTZoM%2FHg%2FS%2FHS1beH7XX8aP4uLisyHbr1SkANX42Es7E%2BZuq%2FXqKmSDMSVTYTMF3ctf%2FKmVMapTGJNkADWmsEoTHoIT8QTdj80aENnYeygi7DGqIDjrcCbLVfcWxUWp3jKqxQRP1744e88mki7wkLuNydGGonvYuPlrfcsDCEFY%2FVpkoq9lc%2FKm0mBdoWAiWsMeb7B3w5c25',swid='{7EDF6E52-328E-4864-9E53-6190364DDF91}')

# for w in range(5):
# 	print ('Week Index ' + str(w))
# 	print (league.box_scores(w)[0].home_team.team_name)
# 	print ("Next" + '\n')

# Going to have to iterate through matchups until reaching X team name and then moving on to the next week

def Team_Total_Year_Points(team_name):

	total_score = 0

	#week
	for x in range(1,15):

		#matchup index
		for y in range(0,6):

			#check home and away for team name
			if league.box_scores(x)[y].home_team.team_name == team_name:
				this_week = Total_Points_Left_On_Bench(league.box_scores(x)[y].home_lineup)
				total_score = total_score + this_week
				
				print ("week: " + str(x) + " - " + str(this_week))
				print ("total: " +  str(total_score))

				continue

			elif league.box_scores(x)[y].away_team.team_name == team_name:
				this_week = Total_Points_Left_On_Bench(league.box_scores(x)[y].away_lineup)
				total_score = total_score + this_week

				print ("week: " + str(x) + " - " + str(this_week))
				print ("total: " +  str(total_score))

				continue

	return total_score

print (Team_Total_Year_Points("Cum Dumpsters"))