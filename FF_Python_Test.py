""" FF Python """

# Football Import
from espn_api.football import League

# League Information - Includes login with espn_s2 and swid (needed since it is a private league)
league = League(league_id=51591979, year=2021, espn_s2='AEBjEqbBxjZIt45ocr9eFgbp%2FBkWyQmzCIuNSsyI4jmQqhhxc2s5mnRJxHr5QOc576BaF1ULvFqeeTZoM%2FHg%2FS%2FHS1beH7XX8aP4uLisyHbr1SkANX42Es7E%2BZuq%2FXqKmSDMSVTYTMF3ctf%2FKmVMapTGJNkADWmsEoTHoIT8QTdj80aENnYeygi7DGqIDjrcCbLVfcWxUWp3jKqxQRP1744e88mki7wkLuNydGGonvYuPlrfcsDCEFY%2FVpkoq9lc%2FKm0mBdoWAiWsMeb7B3w5c25',swid='{7EDF6E52-328E-4864-9E53-6190364DDF91}')

# Dictionary so that it is easy to reference each team by member name
Team_Dictionary = {
	
	"Madison": league.teams[0],
	"TA": league.teams[1],
	"Dambro": league.teams[2],
	"Jack F": league.teams[3],
	"Chuck": league.teams[4],
	"Felipe": league.teams[5],
	"Hollis": league.teams[6],
	"Jack C": league.teams[7],
	"Drew": league.teams[8],
	"Josh": league.teams[9],
	"Germain": league.teams[10],
	"Mitch": league.teams[11],
}

# Basic Tests 

#///////////

# print (Team_Dictionary["Madison"])
# print (league.teams)
# print (Team_Dictionary["Madison"].roster[2].name)

#///////////////

# Trade pulling
trades = league.recent_activity(msg_type='TRADED')

print (trades[0].actions[0])


# This pulls the last trade that was executed (list gets prepended, so the latest one is [0])
# print (trades[0])

# This generates single line items for each player being traded in a trade
# for action in trades[0].actions:
	# print (action)


# Separating trades into what players each member is sending

#for action in trades[0].actions:

	# Print team name of the line item
	# print (action[0].team_name)

	# print player being sent in transaction
	# print (action[2].name)


# for action in trades[0].actions:
	#if 

	# Need to create a team class for this






