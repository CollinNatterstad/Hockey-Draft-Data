import os
import psycopg2 as pg
from psycopg2 import extras
from dotenv import load_dotenv
import json
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

    player_dict = {}

    #creating a connection and cursor objects
    conn = pg.connect(database = db_name, user= db_user, password= db_user_pass, host= db_host, port= db_port)
    cur = conn.cursor()
    print('\ncreated cursor object:', cur)

    #cursor execution object
    cur.execute("""select "Nationality", "Team", "Start", "Overall", "Player", "Position","GP", "G", 
    "A", "+/-", "PIM" from big_hockey_data where "Position" similar to '(C|LW|RW|D)' limit 100;""")
        
    row_list= []

    for row in cur:
        tuple_order = (row[0],row[1],int(row[2]),int(row[3]),row[4],(row[5]),int(row[6]),int(row[7])
        ,int(row[8]),int(row[9]))
        
    
        row_list.append(tuple_order)
    
    json_object = json.dumps(row_list,indent=1)
    
    print(json_object)


    
    
    cur.close()
    print('\nclosed cursor object:', cur)
    conn.close()


if __name__ == '__main__':
    player_uploader()