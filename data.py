from nba_api.stats.endpoints import playerdashboardbyyearoveryear

def get_player_data(player_id):
    """
    Given a player's ID, returns all available data for that player as a dictionary.
    """
    # Create a PlayerDashboardByYearOverYear endpoint for the player
    player_dashboard = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear(player_id=player_id)

    # Get the data frames for the endpoint
    player_dashboard_data_frames = player_dashboard.get_data_frames()

    # Store the data frames in a dictionary
    data = {}
    for df in player_dashboard_data_frames:
        name = df.__class__.__name__
        data[name] = df

    return data


print(get_player_data(1629029))