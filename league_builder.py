import csv


# to read player information from the csv file
def read_playerinfo():
    # open the csv file and read it to create a list of all player details
    with open('soccer_players.csv', newline='') as csvfile:
        socc_players = csv.DictReader(csvfile, delimiter=',')
        players = list(socc_players)
        return players


# for seperating the players into experienced and non-experienced groups
def player_grouping(players):

    # create a list for each group and return them together as a tuple
    inexperienced = [player for player in players
                     if player['Soccer Experience'] != "YES"]
    experienced = [player for player in players
                   if player['Soccer Experience'] == "YES"]

    return experienced, inexperienced


# to assign players for the 3 teams, Sharks, Dragons and Raptors
def player_assigning(players, team_list):
    index = 0
    sorted_players = player_grouping(players)
    player_list = []
    teams = [key for key, values in team_list.items()]

    # looping through experienced and inexperienced group
    for group in sorted_players:
        range = len(teams) - 1
        # looping through each player in group and assigning them to each team
        for player in group:
            # assigning teams for the players
            player['Team'] = teams[index]
            player_list.append(player)
            if index < range:
                index += 1
            else:
                index = 0
    return player_list


# to create three teams with the assigned players and to create a team list
def team_creating(team_list, player_list):

    for player in player_list:
        team = player['Team']
        if team in team_list:
            team_list[team].append(player)
    return team_list


# to create a 'teams.txt' file with teams and team's player details
def writing_txtfile(team_list):

    file = open('teams.txt', 'w')
    for team, players in team_list.items():
        file.write(team + "\n")
        for player in players:
            file.write("{}, {}, {}\n".format(player['Name'],
                                             player['Soccer Experience'],
                                             player['Guardian Name(s)']))
        file.write("\n")
    file.close()


# to create a welcome letters to all the player's guardians
def welcome_letter(team_list):

    for team, players in team_list.items():
        for player in players:
            lowercase_name = player['Name'].lower()
            name = lowercase_name.split(' ')
            first_name = name[0]
            last_name = name[1]
            file = open('{}_{}.txt'.format(first_name, last_name), 'w')
            content = " Dear {}, \n \
Congratulations!! Your kid {} has been officially selected for \
the team {} in the Soccer League. \n \
The first practise begins on June 4th, 2019. And the practise starts \
at 9 AM. \n \
Thanks, \n \
Aishwarya Ravichandran,\n \
Coordinator. \n".format(player['Guardian Name(s)'], player['Name'], team)
            file.write(content)
            file.close()


if __name__ == '__main__':
    team_list = {'Sharks': [],
                 'Dragons': [],
                 'Raptors': []}
    available_players = read_playerinfo()
    players_assigned = player_assigning(available_players, team_list)
    teams = team_creating(team_list, players_assigned)
    writing_txtfile(team_list)
    welcome_letter(team_list)
