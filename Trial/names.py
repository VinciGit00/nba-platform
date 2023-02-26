from nba_api.stats.static import players

def get_player_id(player_name):
    """
    Given a player's name as a string, returns their ID if they are an active NBA player,
    or returns None if the player is not found.
    """
    # Get all active NBA players
    all_players = players.get_active_players()

    # Loop through each player and check if their name matches the input string
    for player in all_players:
        if player['full_name'].lower() == player_name.lower():
            # If we find a match, return the player's ID
            return player['id']

    # If we don't find a match, return None
    return None

print("Player name is: "+str(get_player_id("Luka Doncic")))