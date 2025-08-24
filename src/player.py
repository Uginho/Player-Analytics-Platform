class Player():
    def __init__(self, name, team, position, jersey_number, nationality):
        self.name = name
        self.team = team
        self.position = position
        self.jersey_number = jersey_number
        self.nationality = nationality

        # Stats tracking
        self.games_played = 0
        self.games_started = 0
        self.total_goals = 0
        self.total_assists = 0
        self.total_minutes = 0

        self.game_history = []

        # Method to record stats by game
    def add_game_stats(self, goals, assists, minutes_played, started=False):
            
        self.total_goals += goals
        self.total_assists += assists
        self.total_minutes += minutes_played
        self.games_started += 1

        # When we call this method
        if started:
            self.games_played += 1


        game_stats = {
            'goals': goals,
            'assists': assists,
            'minutes': minutes_played,
            'starts': started
        }
        self.game_history.append(game_stats)

    
    def get_averages(self):
        if self.games_played == 0:
            return {
                'goals_per_game' : 0,
                'assists_per_game' : 0,
                'minutes_per_game': 0
            }
            
        goals_per_game = self.total_goals / self.games_played
        assists_per_game = self.total_assists / self.games_played
        minutes_per_game = self.total_minutes / self.games_played

            # Round function = rounds the deciaml 2 decimal places
        return {
                'goals_per_game' : round(goals_per_game, 2),
                'assists_per_game' : round(assists_per_game, 2),
                'minutes_per_game' : round(minutes_per_game, 2)
            }

    def display_stats(self):

        averages = self.get_averages()

        print(f"Player: {self.name}")
        #print(f"Games Played: {self.games_played} | Games Started: {self.games_started}")
        print(f"Goals: {self.total_goals} | Assists: {self.total_assists}")
        print(f"Avg Goals/Game: {averages['goals_per_game']} | Avg Assists/Game: {averages['assists_per_game']}")



