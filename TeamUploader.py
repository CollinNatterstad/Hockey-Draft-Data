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

    team_codes = ["ANA", "ARI", "ATL", "BOS", "BUF", "CAL", "CAR", "CHI", "COL", "CBJ", "DAL", "DET"
    , "EDM", "FLO", "HAR", "LOS", "MNS", "MIN","MON","NAS", "NEW", "NYI", "NYR", "OTT", "PHI", "PHO"
    , "PIT", "QUE", "SAN", "SEA", "STL", "TAM", "VAN", "VEG", "WAS", "WIN"]
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

    cur.execute("""select distinct("Teams") from big_hockey_data Order By "Teams" asc.; """)
    for items in cur:
        team_names.append(str(items))
    
    

if __name__ == '__main__':
    team_loader()