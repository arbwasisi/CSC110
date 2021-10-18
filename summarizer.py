## Author: Arsene Bwasisi
## Description: summerizer.py will take a text file of a sports game, and read
##              it's content to print a statement that summerizers the gamelog.
##              This includes the winner of the game, the players that scored,
##              and the score of each team.

def process_file(file):
    ''' This function process and organizes the information from the inputed file.'''

    game_log = open(file, 'r') # Opens the file in read mode
    
    # Define empty list
    teams = list()
    player = list()
    points = list()
    
    # Organize data into empty list
    for line in game_log:
        ls = line.split(' ')
        teams.append(ls[0])
        player.append(ls[1])
        points.append(int(ls[2]))

    return teams, player, points

def team_points(teams, points):
    ''' This function will keep count of the score for each team.'''

    points_1 = 0 # Points for the first team
    points_2 = 0 # Points for the second team
    team_1 = teams[0] # Defines the first team

    index = 0
    for point in points:
        if teams[index] == teams[0]: # Adds point to first team
            points_1 += point
        else:
            points_2 += point # Adds point to first team
            team_2 = teams[index] # Defines the second team
        index += 1

    return points_1, points_2, team_1, team_2

def player_count(player):
    ''' This funtion will return the number of players that scored.'''

    count = list() # Creat a list for individual player
    
    # From player list, add a player to count once
    for name in player:
       if name not in count:
           count.append(name)

    return len(count)

def winner(team_1, team_2, points_1, points_2):
    ''' This function will determine the winner.'''
    
    if points_1 > points_2:
        print(team_1, 'won!')
    else:
        print(team_2, 'won!')

    print(team_1, 'scored', points_1, 'points.')
    print(team_2, 'scored', points_2, 'points.')

def main():
    
    # Call all functions and display a summary of the data
    file_name = input('enter gamelog file name:\n')

    teams, player, points = process_file(file_name)
    points_1, points_2, team_1, team_2 = team_points(teams, points)
    winner(team_1, team_2, points_1, points_2)
    count = player_count(player)
    
    print(count, 'players scored.')
    print(player[0], 'scored first.')
    print(player[-1], 'scored last.')

main()
