import pandas as pd
import os
from player import Player

class DataLoader:
    def __init__(self):
        self.base_url = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2024-25/"
        self.target_teams = [
            "Arsenal", "Aston Villa", "Chelsea", "Liverpool", "Manchester United", "Manchester City", "Newcastle", "Tottenham"
        ]
    def load_players_data(self):
        url = self.base_url + "cleaned_players.csv"
        print(f"Loading player data from: {url}")

        df = pd.read_csv(url)
        print(f" Loaded {len(df)} total players")

        return df


    def csv_row_to_player(self, row, debug_count=0):
        # Converting player row to a player object

        name = f"{row['first_name']} {row['second_name']}"

        if debug_count < 5:
            print(f"Debug: {name} - element_type: '{row['element_type']}' (type: {type(row['element_type'])})")

        # Map element_type to position
        position_map = {
            "GK": "GK",
            "DEF": "DEF",
            "MID": "MID",
            "FWD": "FWD"
        }

        position = position_map.get(row['element_type'], "Unknown")

        player = Player(
            name=name,
            team="TBD",
            position=position,
            jersey_number=0,
            nationality="TBD"
        )

        player.total_goals = row['goals_scored']
        player.total_assists = row['assists']
        player.total_minutes = row['minutes']
        player.games_played = 1 if row['minutes'] > 0 else 0

        #player.clean_sheets = row['clean_sheets']

        return player

    def create_players_from_csv(self):
        # Load the CSV and convert rows to objects in Player
        df = self.load_players_data()

        players = []
        for index, row in df.iterrows():
            try:
                player = self.csv_row_to_player(row, len(players))
                players.append(player)
            
                # Debug: Print first few players
                if len(players) <= 3:
                    print(f"DEBUG Player {len(players)}: {player.name}")
                    print(f"  Goals: {player.total_goals}, Assists: {player.total_assists}")
                    print(f"  Position: {player.position}")
                
            except Exception as e:
                print(f"ERROR creating player at index {index}: {e}")
                break  # Stop on first error to see what's wrong
    
        print(f"Created {len(players)} Player objects!")
        return players


    def load_teams_data(self):
        # Load team names and IDs
        url = self.base_url + "teams.csv"
        print(f"Loading teams data from: {url}")
    
        teams_df = pd.read_csv(url)
        print(f"Loaded {len(teams_df)} teams")
        print(f"Teams columns: {list(teams_df.columns)}")
        print("First few teams:")
        print(teams_df.head())
    
        return teams_df

    def load_players_raw_data(self):
        # Load raw player data with team IDs
        url = self.base_url + "players_raw.csv" 
        print(f"Loading raw players data from: {url}")
    
        raw_df = pd.read_csv(url)
        print(f"Loaded {len(raw_df)} raw players")
        print(f"Raw players columns: {list(raw_df.columns)}")
    
        return raw_df


    def merge_all_data(self):
        # First, we merge all data

        cleaned_df = self.load_players_data()
        raw_df = self.load_players_raw_data()
        teams_df = self.load_teams_data()

        team_mapping = dict(zip(teams_df['id'], teams_df['name']))
        print(f"Team mapping {team_mapping}")

        cleaned_df['full_name'] = cleaned_df['first_name'] + ' ' + cleaned_df['second_name']
        raw_df['full_name'] = raw_df['first_name'] + ' ' + raw_df['second_name']

        merged_df = pd.merge(cleaned_df, raw_df, on='full_name', suffixes=('_cleaned', '_raw'))

        merged_df['team_name'] = merged_df['team'].map(team_mapping)

        print("Successfully merged {len(merged_df)} players with complete data.")

        print(f"Available columns: {list(merged_df)} players with complete data.")

        return merged_df

        
    def create_players_from_merged_data(self):
        # Creating  player objects using the merged data and their real names

        merged_df = self.merge_all_data()

        players = []
        for index, row in merged_df.iterrows():
            name = row['full_name']
            position = row['element_type_cleaned']
            team_name = row['team_name']
            jersey_number = row['squad_number'] if not pd.isna(row['squad_number']) else 0

            player = Player(
                name=name,
                team=team_name,
                position=position,
                jersey_number=int(jersey_number),
                nationality='TBD'
            )

            player.total_goals = row['goals_scored_cleaned']
            player.total_assists = row['assists_cleaned']
            player.total_minutes = row['minutes_cleaned']
            #player.games_played = row['games']
            if row['minutes_cleaned'] > 0:
                # More accurate estimation: consider that players don't always play full games
                estimated_games = max(1, int(row['minutes_cleaned'] / 90))
                # Use the higher of estimated games or starts (since starts should be <= total games)
                player.games_played = max(estimated_games, row['starts'])
            else:
                player.games_played = row['starts']  # If no minutes, just use starts

                player.games_started = row['starts']

                players.append(player)

        print(f"Created {len(players)} players with Complete Data.")
        return players