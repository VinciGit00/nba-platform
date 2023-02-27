import streamlit as st
import pandas as pd
from nba_api.stats.endpoints import playerdashboardbyyearoveryear
from datetime import datetime
from getid import *

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
        # Exclude unnecessary columns from the data frame
        if 'GROUP_SET' in df.columns:
            df = df.drop(columns=[
            'GROUP_SET', 'TEAM_ID', 'MAX_GAME_DATE', 
            'W_RANK','MIN', 'WNBA_FANTASY_PTS_RANK', 'NBA_FANTASY_PTS',
            'WNBA_FANTASY_PTS', 'DD2', 'TD3', 'GP_RANK', 'DD2_RANK', 'L_RANK', 
            'MIN_RANK', 'FGM_RANK', 'FG3M_RANK', 'TD3_RANK', 'NBA_FANTASY_PTS_RANK',
            'TOV_RANK', 'PFD_RANK', 'FG3_PCT_RANK','FTA_RANK', 'FGM', 'FGA', 'FTM', 'FTA'
            ])

            df = df[['GROUP_VALUE','TEAM_ABBREVIATION', 'GP', 'W', 'L', 'PTS', 
            'AST', 'REB','OREB', 'DREB', 'STL', 'BLK', 
            'PLUS_MINUS', 'FG_PCT', ]]

            df['PTS'] = df['PTS'] / df['GP']
            df['AST'] = df['AST'] / df['GP']                
            df['REB'] = df['REB'] / df['GP']
            df['OREB'] = df['OREB'] / df['GP']
            df['DREB'] = df['DREB'] / df['GP']
            df['STL'] = df['STL'] / df['GP']
            df['BLK'] = df['BLK'] / df['GP']

            df = df.rename(columns={'GROUP_VALUE': 'YEAR',
                                    'PTS': 'PTS/g', 'AST': 'AST/g', 
                                    'REB': 'REB/g', 'OREB': 'OREB/g', 
                                    'DREB': 'DREB/g', 'STL': 'STL/g', 
                                    'BLK': 'BLK/g'})

            df = df.round(2)

        # Reformat the MAX_GAME_DATE column
        if 'MAX_GAME_DATE' in df.columns:
            df['MAX_GAME_DATE'] = df['MAX_GAME_DATE'].apply(lambda x: datetime.strptime(x[:10], '%Y-%m-%d').date())
        pd.set_option('display.max_columns', None)

        name = df.__class__.__name__
        data[name] = df



    # Print the data frames in Streamlit
    for name, df in data.items():
        st.write(f"### {name}")
        st.write(df)

       
        print(df)

        st.write("""
        ## Points/game
        """)

        chart_data = df[['PTS/g']]    
        st.line_chart(data = df, x= 'YEAR', y = 'PTS/g')

        st.write("""
        ## Assist/game
        """)

        chart_data = df[['REB/g']]    
        st.line_chart(data = df, x= 'YEAR', y = 'AST/g')
 
        st.write("""
        ## Rebound/game
        """)

        chart_data = df[['REB/g']]    
        st.line_chart(data = df, x= 'YEAR', y = 'REB/g')

        


st.write("""
# NBA stats
Made by Marco Vinciguerra \n
Write first surname and after name \n
""")
         
# Add a text field for user input
user_input = st.text_input("Enter the name of the player:")

# Add a button to submit the user input
if st.button("Submit"):
    # Do something with the user input
    st.write("You entered:", user_input)
    print(user_input)
    
    player_id = get_player_id(user_input) 
    print(player_id)
    if(player_id != None):
        get_player_data(player_id)
    else:
       st.write("Player inserted not found") 
    
