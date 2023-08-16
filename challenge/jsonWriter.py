import json

def save_team_list(teams):
    with open('teams.txt', 'w') as outfile:
        json.dump(teams, outfile)

def load_team_list():
    try:
        with open('teams.txt') as json_file:
            return json.load(json_file) 
    except:
        return 0