from optparse import Values
import psycopg2 as pg
from psycopg2 import sql
import os
import country_converter as coco
from dotenv import load_dotenv
load_dotenv()

'''The general plan for this application is to create a series of functions that will store, transform, and update column values for the country table.
Specifically, the key values already exist within the table. The goal is to pass these key values into python, utilize the pycountry library. What I want
to do is to pass the country key in and have pycountry library match that key and provide the country name to be uploaded into the psql database.

We need to 
establish a connection to psql
pull in the country code from the psql table
pass these into a iterable object
loop over this object to match the code and the name.
push these changes to the psql table. 
close the connection to psql
'''


def main():
    
    def load_array():

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
        
        
        db_codes = []
        country_key = []
        country_name =[]
        
        '''cur.execute creates an iterable object that can be looped. Through a sql statement it pulls in distinct country codes from the big data table. 
        Within the for-loop the data type will need to be converted. Currently the datatype is a tuple so we can use the str() function to convert the tuple into a string as it
        appends items to country_codes. This way we can utilize another for-loop and string index to pass along the characters we want to match for each country 
        
        This section could definitely use refactoring in the future. Mulitple for-loops means that each item is iterated over muliple times. This satisfies MVP but
        should be rewritten to learn and experiement.  
        '''
        cur.execute("""SELECT Distinct("Nationality") FROM big_hockey_data Order By "Nationality" asc; """)
        for codes in cur:
            #Appends cur item to country_code str() converts items from tuple to string
            db_codes.append(str(codes))
           
        #this for-loop takes str objects within country_codes and selects a specific string 
        for items in db_codes:
            country_key.append((items[2:4]))
           
        #converts the ISO alpha_2 country code into a country name. 
        for items in country_key:
            country_name.append(coco.convert(names=items, to='name_short')) 
        
        #converts two lists to one dictionary with zip method. Makes it one iterable object and removes potential for miss values in key:value. 
        key_pairs = dict(zip(country_key,country_name))

        #iterates over the dictionary and inserts each row into the table. 
        for key,value in key_pairs.items():
            cur.execute("""insert into country_table (country_key, country_name) values (%s, %s);""", (key, value))

        #committing changes, closing cursor object and connection.   
        conn.commit()
        cur.close()
        print('\nclosed cursor object:',cur)
        conn.close()
        
    load_array()
    
if __name__ == '__main__':
    main()