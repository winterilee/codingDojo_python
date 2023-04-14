players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]

# TODO Challenge 1: Update the Constructor
# ? Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.

class Player:
    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]
    
    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nPosition: {self.position}\nTeam: {self.team}")
        print("-" * 20)
    
    @classmethod
    def get_team(cls, team_list):
        temp_team = []
        for player in team_list:
            temp_team.append(cls(player))
        return temp_team



# TODO Challenge 2: Create instances using individual player dictionaries.
# ? Given these variables, create Player instances for each of the following dictionaries. Be sure to instantiate these outside the class definition, in the outer scope.

kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}
    
# Create your Player instances here!
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

print(player_kevin.__dict__)
print(player_jason.__dict__)
print(player_kyrie.__dict__)


# TODO Challenge 3: Make a list of Player instances from a list of dictionaries
# ? Finally, given the example list of players at the top of this module (the one with many players) write a for loop that will populate an empty list with Player objects from the original list of dictionaries.

# ... (class definition and large list of players here)
new_team = []

# Write your for loop here to populate the new_team variable with Player objects.
for p in players:
    new_team.append(Player(p))

for player in new_team:
    player.display()

print(type(new_team))

# TODO NINJA BONUS: Add a get_team(cls, team_list) @class method
# ? Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects. Be sure to test your method!

another_team = Player.get_team(players)

for player in another_team:
    player.display()