'''
from player import Player

Ibrahimovic = Player("Zlatan Ibrahimovic", "Internazionale", "Striker", 9, "Sweden")

# Start of Season Initial Stats
print(f"{Ibrahimovic.name} - Initial Stats:")
print(f"Goals: {Ibrahimovic.total_goals}")
print(f"Games Played: {Ibrahimovic.games_played}")
print(f"Games Started: {Ibrahimovic.games_started}")
print()

# Players stats by game
# Game 1
#print("Game 1 Stats")
Ibrahimovic.add_game_stats(goals=3, assists=2, minutes_played=90, started=True)

# Game 2
#print('Game 2')
Ibrahimovic.add_game_stats(goals=2, assists=1, minutes_played=90, started=True)


print(f"\n{Ibrahimovic.name} - Updated Stats")
print(f"Total Goals: {Ibrahimovic.total_goals}")
print(f"Total Assists: {Ibrahimovic.total_assists}")
print(f"Total Minutes {Ibrahimovic.total_minutes}")
print(f"Games Played: {Ibrahimovic.games_played}")
print(f"Starts: {Ibrahimovic.games_started}")
print(f"Game History: {Ibrahimovic.game_history}")
'''
'''
# averages
print("\n" + "="*40)
print("Zlatans Averages:")
print("="*40)

averages = Ibrahimovic.get_averages

Ibrahimovic.get_averages()
Ibrahimovic.display_stats()

from team import Team

# Create a team
inter_miami = Team("Inter Miami CF")

# Add multiple players
print("Adding players to the team...")
messi = inter_miami.add_player("Lionel Messi", "Forward", 10, "Argentina")
ibra = inter_miami.add_player("Zlatan Ibrahimovic", "Striker", 9, "Sweden")
beckham = inter_miami.add_player("David Beckham", "Midfielder", 23, "England")

# Show the roster
inter_miami.show_roster()

# Add some game stats
print("\nAdding game stats...")
messi.add_game_stats(goals=2, assists=1, minutes_played=90, started=True)
messi.add_game_stats(goals=1, assists=2, minutes_played=85, started=True)

ibra.add_game_stats(goals=3, assists=0, minutes_played=90, started=True)

# Test the search function
print("\nSearching for players...")
found_player = inter_miami.find_player("Lionel Messi")
if found_player:
    print("Found player!")
    found_player.display_stats()
else:
    print("Player not found")

print("="*50)

# Test searching for non-existent player
not_found = inter_miami.find_player("Cristiano Ronaldo")
if not_found:
    print("Found Ronaldo!")
else:
    print("Ronaldo not on this team") '''
'''
from scraper import SoccerScraper

scraper = SoccerScraper()
players = scraper.scrape_player_stats()

if players:
    print("\n🔥 TOP 10 PREMIER LEAGUE PLAYERS 2024-25:")
    print("="*60)
    
    for i, player in enumerate(players[:10]):
        print(f"{i+1:2}. {player['name']} ({player['club']})")
        print(f"    Goals: {player['goals']} | Assists: {player['assists']} | Total: {player['combined']}")
        print()
else:
    print("❌ No players found - something went wrong")


from data_loader import DataLoader

loader = DataLoader()
df = loader.load_players_data()

print(f"Columns: {list(df.columns)}")
print(f"First few rows:")
print(df.head())
'''
from data_loader import DataLoader

loader = DataLoader()
merged_df = loader.merge_all_data()

# Show sample of merged data
print("\n MERGED DATA SAMPLE:")
print("="*60)
print(merged_df[['full_name', 'team_name', 'squad_number', 'goals_scored_cleaned', 'starts']].head(10))

# Check our target teams
print(f"\n📊 UNIQUE TEAMS ({len(merged_df['team_name'].unique())} total):")
for team in sorted(merged_df['team_name'].unique()):
    count = len(merged_df[merged_df['team_name'] == team])
    print(f"  {team}: {count} players")

complete_players = loader.create_players_from_merged_data()

    # Show first few players
for player in complete_players[:5]:
    player.display_stats()
    print()

players = loader.create_players_from_csv()

print("\n First 5 Players Created:")
print("="*50)
for i, player in enumerate(players[:5]):
    player.display_stats()
    if i < 4:
        print()

print("\n Looking for player...")
print("="*40)
for player in players:
    if "Palmer" in player.name or "De Bryune" in player.name or "Watkins" in player.name or "Isak" in player.name:
        print(f"Found: {player.name} ({player.position})")
        player.display_stats()

teams_df = loader.load_teams_data()
raw_df = loader.load_players_raw_data()
