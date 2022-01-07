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

#Player_Points("Madison", 3)

# print (league.teams)
# print (league.teams[0].roster[0].name)

# print (league.teams[0].roster[0].position)

# print (league.teams[0].roster[0].stats[17]['points'])


def Player_Points(league_info, team_num, roster_num, gameweek):

	global player_name
	player_name = league_info.teams[team_num].roster[roster_num].name
	return league_info.teams[team_num].roster[roster_num].stats[gameweek]['points']

x = Player_Points(league, 0, 0, 17)

print (player_name + ": " + str(x))