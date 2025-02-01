#1. Read the name of 4 teams
#2. Each team will play once with the other three
#3. Win 3 points, draw 1 point, loss 0 points

teams = []
points = [0,0,0,0]

for i in range(4):
    team_name = input (f'Team number #{i+1}: ')
    teams.append(team_name)

for i in range(3):
    for j in range(i+1,4):
        print (f'Match {teams[i]} x {teams[j]}')
        score_team_A = input(f'{teams[i]}: ')
        score_team_B = input(f'{teams[j]}: ')
        if score_team_A == score_team_B:
            points[i] += 1
            points[j] += 1
        elif score_team_A > score_team_B:
            points[i] += 3
        else:
            points[j] +=3

print (f'{"Team":^20}{"Points":^7}')
for i in range(4):
    print (f'{teams[i]:^20}{points[i]:^7}')

for i in range(3):
    if points[i] > points [i+1]:
        champion = teams[i]
print ('The winner team is',champion)