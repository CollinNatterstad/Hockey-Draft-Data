import psycopg2 as pg
import os
from dotenv import load_dotenv
load_dotenv()

def team_loader():
    db_host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_user_pass = os.getenv("DB_USER_PASS")
    db_port = os.getenv("DB_PORT")

    #The team codes are ultimately irrelevant so I created them here. They were written  in asc order. Lazy way but ultimately I'm more concerned with the names than 
    #Keys for analytics. 
    #They will be matched to their corresponding team with the dict(zip()) function.
    
    #named lists here
    team_codes = ["ANA", "ARI", "ATL", "BOS", "BUF", "CAL", "CAR", "CHI", "COL", "CBJ", "DAL", "DET"
    , "EDM", "FLO", "HAR", "LOS", "MNS", "MIN","MON","NAS", "NEW", "NYI", "NYR", "OTT", "PHI", "PHO"
    , "PIT", "QUE", "SAN", "SEA", "STL", "TAM","TOR", "VAN", "VEG", "WAS", "WIN"]
    team_storage = []
    team_names = []

    #connects to .env file and supplies appropriate credentials. 
    db_host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_user_pass = os.getenv("DB_USER_PASS")
    db_port = os.getenv("DB_PORT")
        
    #creating a connection and cursor objects
    conn = pg.connect(database = db_name, user= db_user, password= db_user_pass, host= db_host, port= db_port)
    cur = conn.cursor()
    print('\ncreated cursor object:', cur)

    #the tuple object must be converted prior to pulling the name out of the data. Should look at ways to work around this in the future.
    #there might be a more pythonic way of accomplishing this feat faster. 
    cur.execute("""select distinct("Team") from big_hockey_data Order By "Team" asc; """)
    for items in cur:
        team_storage.append(str(items))
    for items in team_storage:
        team_names.append(items[2:-3])
    
    team_pairs = dict(zip(team_codes, team_names))
    for key, value in team_pairs.items():
        cur.execute ("""insert into organization_table (organization_key, organization_name) values (%s, %s); """, (key, value))

    #committing changes, closing cursor object and connection here
    conn.commit()
    cur.close()
    print('\nclosed cursor object:', cur)
    conn.close()


if __name__ == '__main__':
    team_loader()