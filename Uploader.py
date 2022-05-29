def main():  
    import os
    import psycopg2 as pg
    from dotenv import load_dotenv
    load_dotenv() 
    #Function for loops over the .csv / .json files and uploads each one into postgres database. 
    def connect_and_store():
        #connects to .env file and supplies appropriate credentials. 
        DB_HOST = os.getenv("DB_HOST")
        DB_NAME = os.getenv("DB_NAME")
        DB_USER = os.getenv("DB_USER")
        DB_USER_PASS = os.getenv("DB_USER_PASS")
        DB_PORT = os.getenv("DB_PORT")
        
        draftyearfiles = os.listdir(r'D:\Coding Projects\Hockey Stats\DraftYear.csv')        
        
        for files in draftyearfiles:
            #Connection to postgres database. secrets stored in .env file. 
            conn = pg.connect(database = DB_NAME, user= DB_USER, password= DB_USER_PASS, host= DB_HOST, port= DB_PORT)
            copypath= r'D:\Coding Projects\Hockey Stats\DraftYear.csv\\'+ files
        
            #creating cursor to interact with the database.
            cur=conn.cursor()
            #confirming the creation of the cursor
            print('\ncreated curser object:', cur)
            #selects and copies the appropriate .csv file into the Hockey Draft Database
            with open (copypath,'r') as f:
                #skips header row. 
                next(f)
                #uploads data format is from[], to, and 
                cur.copy_from(f,'bighockeydata',',')
            #Commits changes1
            conn.commit()
            
            #Closes the cursor object
            cur.close()
            print('\nclosed cursor object:',cur)

    connect_and_store()
if __name__ == "__main__":
    main()
