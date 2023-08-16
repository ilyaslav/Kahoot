import jsonWriter
import settings

def fill_rating():
	settings.rating = jsonWriter.load_team_list()
	print(settings.rating)
	return settings.rating

def find_team(name):
	for team in settings.rating:
		if team[1] == name:
			return team

def change_score(score, team_name):
	team = find_team(team_name)
	team[3] += score
	jsonWriter.save_team_list(settings.rating)
