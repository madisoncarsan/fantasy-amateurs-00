#Team_Pathing.py

"""
Figure out a way to path through and find the same team across weeks

"""

from espn_api.football import League 
from espn_api.football import Player 
from espn_api.football import BoxPlayer

from Player_Points import *

league = League(league_id=<your-leagueid>, year=<year>, espn_s2=your-s2',swid='{your-swid}')

# for w in range(5):
# 	print ('Week Index ' + str(w))
# 	print (league.box_scores(w)[0].home_team.team_name)
# 	print ("Next" + '\n')

# Going to have to iterate through matchups until reaching X team name and then moving on to the next week

#Returns a team's total bench points for the year
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
				
				# print ("week: " + str(x) + " - " + str(this_week))
				# print ("total: " +  str(total_score))

				continue

			elif league.box_scores(x)[y].away_team.team_name == team_name:
				this_week = Total_Points_Left_On_Bench(league.box_scores(x)[y].away_lineup)
				total_score = total_score + this_week

				# print ("week: " + str(x) + " - " + str(this_week))
				# print ("total: " +  str(total_score))

				continue

	return float("{:.2f}".format(total_score))

#Returns all team's bench points for the year in a league
def League_Bench_Points(league):
	for t in league.teams:
		team = t.team_name
		print (team + ": " + str(Team_Total_Year_Points(team)))


League_Bench_Points(league)

