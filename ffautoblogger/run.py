# Run the fantasy football autoblogger

from scraper import Scraper

args = {}

config = open('ffautoblogger.ini', 'r')
for line in config:
    pair = line.strip().split('=')
    args[pair[0]] = pair[1]

week_id = args['week_id']
team_count = int(args['team_count'])

espn = Scraper(args['league_id'], args['season_id'])

all_active = {}
all_bench = {}
all_teams = espn.get_teams(team_count, week_id)

print('-------------------------')

for team in all_teams[1:]:
    print('TEAM {0} {1} - {2} pts'.format(team.team_name, team.team_name_short, team.score))

    active = [player for player in team.players.values() if player.slot != 'Bench']
    bench = [player for player in team.players.values() if player.slot == 'Bench']

    active_score = 0.0
    for player in active:
        print('\t{0}\t| {1} {2}: {3}/{4} pts'.format(player.slot,
                                                    player.name,
                                                    team.team_name_short,
                                                    player.points,
                                                    player.projected_points))
        active_score += player.points
        all_active[player.player_id] = player

    print('\t\tTotal: {0}'.format(active_score))
    print()

    bench_score = 0.0
    for player in bench:
        print('\t{0} | {1} {2}: {3}/{4} pts'.format(player.slot,
                                                    player.name,
                                                    team.team_name_short,
                                                    player.points,
                                                    player.projected_points))
        bench_score += player.points
        all_bench[player.player_id] = player

    print('\t\tTotal: {0}'.format(bench_score))
    print()
