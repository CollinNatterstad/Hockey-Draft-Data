

import os
import json
import psycopg2 as pg
from psycopg2 import sql
from dotenv import load_dotenv
load_dotenv()

'''This program will act as the intermediary between two tables the big_hockey_data table and the player_table.The bhd table will have it's datatypes converted within the dbms
to make the transition between the two tables as easy as possible. This will store and load 9.2k player instances spanning 1984-2021. Consequently, this program will take time
to perform each of the tasks. From previous programs the psql -> python transition will require a conversion in order to be mutable. This represents a problem
as there are over 9.2 instances. Requiring multiple loops will increase the time span of the program substantially with each for-loop interaction. Preferably, multiple steps
are performed with each cycle to eliminate as much time as possible. 

column, data type, example

player_id: serial (created with each instance)
country_key: varchar -> 'CA'
organization_key: varchar -> 'TAM'
draft_year: int -> '1984'  
draft_pick: int -> '1'
player_name: varchar -> 'Steven Stamkos'
games_played: int -> '949'
goals: int -> '1005'
assists: int -> '554'
points: int -> '1559'
plus_minus: int -> '25'
pims: int -> '300'
goalie_games_played: int -> '123'
wins: int ->'93'
losses: int -> '30'
ties_and_overtime_losses: int -> '15'
save_percentage: numeric -> '.912'
goals_against_average: numeric -> '2.18'
point_share: numeric -> '118.375'
 '''


def player_uploader():
    
    db_host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_user_pass = os.getenv("DB_USER_PASS")
    db_port = os.getenv("DB_PORT")

    #creating a connection and cursor objects
    conn = pg.connect(database = db_name, user= db_user, password= db_user_pass, host= db_host, port= db_port,)
    cur = conn.cursor()
    #confirms creation
    print('\ncreated cursor object:', cur)

    #cursor execution object
    cur.execute("""select "Player"
    , "Nationality"
    , "Team" 
    , "Start"
    , "Overall"
    , "Group"
    , "Position"
    , "GP"
    , "G"
    , "A"
    , "PTS"
    , "+/-"
    , "PIM" 
    , "GGP"
    , "W"
    , "L"
    , "T/O" 
    , "SV%" 
    , "GAA"
    , "PS"

    from big_hockey_data   
    ;
    """)   
    
    player_data = []

    #iterates over object cur to create a series of dictionaries that convert the data type and add key before merging and appending to external dictionary. 
    for row in cur:
        #list of dictionaries to convert tuple value into desired datatype. 
        d1 = {'player_name':str((row[0]))}
        d2 = {"country_key":str((row[1]))}
        d3 = {"team_name": str((row[2]))}
        d4 = {"draft_year": int((row[3]))}
        d5 = {"draft_pick": int((row[4]))}
        d6 = {"skating_group":str((row[5]))}
        d7 = {"position":str((row[6]))}
        d8 = {"games_played":int((row[7]))}
        d9 = {"goals":int((row[8]))}
        d10 ={"assists":int((row[9]))}
        d11 ={"points":int((row[10]))}
        d12 ={"plus_minus":int((row[11]))} 
        d13 ={"penalty_minutes":int((row[12]))}
        d14 ={"goalie_games_played":int((row[13]))}
        d15 ={"wins":int((row[14]))}
        d16 ={"losses": int((row[15]))} 
        d17 ={"ties_and_overtime_losses":int((row[16]))}
        d18 ={"save_percentage":float((row[17]))}
        d19 ={"goals_against_average":float((row[18]))}
        d20 ={"point_share":float((row[19]))}
       
        #merge the dictionary into one dictionary.
        instance_dict = d1|d2|d3|d4|d5|d6|d7|d8|d9|d10|d11|d12|d13|d14|d15|d16|d17|d18|d19|d20
        #take instance dict and append to external list of each instance dict. 
        player_data.append(instance_dict)
    
    #sql query to insert dictionary data 
    query = """
        INSERT into player_table (player_name,country_key,team_name,draft_year,draft_pick,skating_group,position
        ,games_played,goals,assists,points,plus_minus,penalty_minutes,goalie_games_played,wins,losses,ties_and_overtime_losses
        ,save_percentage,goals_against_average,point_share) VALUES (%(player_name)s,%(country_key)s,%(team_name)s,%(draft_year)s,%(draft_pick)s
        ,%(skating_group)s,%(position)s,%(games_played)s,%(goals)s,%(assists)s,%(points)s,%(plus_minus)s,%(penalty_minutes)s,%(goalie_games_played)s
        ,%(wins)s,%(losses)s,%(ties_and_overtime_losses)s,%(save_percentage)s,%(goals_against_average)s,%(point_share)s) 
    """  
    #executes sql query by passing query and player_data as variables. Conversion is handled by psycopg2. Thankfully do not need to for-loop dictionary; MUCH faster. 
    cur.executemany(query,player_data)
    #commits changes to the data table. 
    conn.commit()
    #closes cursor and connection. 
    cur.close()
    print('\nclosed cursor object:', cur)
    conn.close()


if __name__ == '__main__':
    player_uploader()