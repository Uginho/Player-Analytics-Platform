from player import Player

class Team:
    def __init__(self, team_name):
        # Initialize a team and a spot available to add player?
        self.team_name = team_name
        self.players = []

    def add_player(self, name, position, jersey_number, nationality):
        # Add player to team
        new_player = Player(name, self.team_name, position, jersey_number, nationality)
        self.players.append(new_player)
        print(f"Added {name} to {self.team_name}")
        return new_player

    def find_player(self, player_name):
        # Find player by name makes search case insensitive
        for player in self.players:
            if player.name.lower() == player_name.lower():
                return player
        return None

    def show_roster(self):
        # Display all players on the team
        print(f"\n{self.team_name} Roster: ")
        print('=' * 40)
        for player in self.players:
            print(f"{player.name} - #{player.jersey_number} - {player.position}")

