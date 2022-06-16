from multiprocessing.connection import Connection
import os
import json
import psycopg2 as pg
from psycopg2 import sql
from dotenv import load_dotenv
load_dotenv()

''' 
    the purpose of this program is to create a class based library of discrete solutions for the files that I've already created. This is so that I can better understand 
    object oriented programming and how class based libraries can facilitate scripting functionality by creating a library of commonly performed tasks postgreSQL components.
    Furthermore, this will incorporate many of the  
    
    S(ingle responsibility): classes and methods that perform a single thing with high cohesion
    O(pen/closed): open to function extension but closed to modification (you shouldn't need to change the code to extend the functionality) 
    L(iskov Subsitution): if you have program objects you should be able to replace them with instances of subtypes/subclasses without alterting the 'correctness' of the program
        you shouldn't have to change what parameters mean to fit a specific use type.
    I(nterface Segregation)
    D(ependency Inversion): We want classes to depend on abstraction not concrete subclasses. You can create different abstract methods to pass into other classes 

    

'''


class Psql_Interaction:
    def __init__(self) -> None:
        pass
    
class connection(Psql_Interaction):    
    
    def __init__(self,db_name:str,db_user:str,db_user_pass:str,db_host:str,db_port:str):
        
        self.name = db_name
        self.user = db_user
        self.user_pass = db_user_pass
        self.host = db_host
        self.port = db_port
    
    def __enter__(self):
        self.conn = pg.connect(database = self.name, user= self.user, password= self.user_pass, host= self.host, port= self.port)
        self.cur = self.conn.cursor()
        return self.conn, self.cur 
    
    def __exit__(self,exception_type, exception_value, exception_traceback):
        self.cur.close()
        self.conn.close()


    
    #variables are stored in local .env file. stipulates the connection factors for the postgress server 
db_host= os.getenv("DB_HOST")
db_name= os.getenv("DB_NAME")
db_user= os.getenv("DB_USER")
db_user_pass= os.getenv("DB_USER_PASS")
db_port= os.getenv("DB_PORT")

#calls the connection class and supplies appropriate arguments. With acts as a context manager 
with connection(db_name, db_user, db_user_pass,db_host,db_port) as conn:
    self.cur.execute("""select * from player_table limit 1""")
    