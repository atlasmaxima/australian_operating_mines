import sqlite3
import csv 
import logging 

class SQLiteDatabase:
    def __init__(self, database_name):
        # set up and create a connection to the SQLite database
        self.conn = sqlite3.connect(database_name)
        # create a new cursor object
        self.cursor = self.conn.cursor()
        logging.info('Connected to database')
        # execute table if not already exists
        self.create_table()
        # insert values into table 
        self.insert_mine_sites()

    def create_table(self):
        with open('./model/tables/mine_sites.sql', 'r') as file:
            mine_sites_sql = file.read()
            
        with open('./model/tables/commodity.sql', 'r') as file:
            commodity_sql = file.read()
        
        self.cursor.execute(mine_sites_sql)
        self.cursor.execute(commodity_sql)

    def excute_sql_command(self, command, params=None):
        try: 
            # excute sql queries
            if params:
                self.cursor.execute(command, params)
            else:
                self.cursor.execute(command)
            # commit the changes to the database
            self.conn.commit()
            logging.info(f'Successfully executed command: {command}')
        except Exception as e:
            logging.error(f'Error executing command: {command} - {e}')
            raise e
   
    def fetch_mine_sites(self):
        # execute a SELECT statement on the mine_sites table
        self.cursor.execute('SELECT latitude, longitude FROM mine_sites LIMIT 500')
        # fetch all rows of the result
        rows = self.cursor.fetchall()
        return rows

    def insert_mine_sites(self):
        insert_sql_command = "INSERT INTO mine_sites (proj_code, short_title, site_type, sub_type, stage, longitude, latitude) VALUES (?, ?, ?, ?, ?, ?, ?)"
        # 'ISO-8859-1' is the encoding of the file in order to read it
        with open('./artifacts/operating_mines.csv', encoding='ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)
            # iterate over each from in the csv file
            for row in reader:
                # extract values from each row
                proj_code = row['PROJ_CODE']
                short_title = row['SHORT_TITLE']
                site_type = row['SITE_TYPE']
                sub_type = row['SUB_TYPE']
                stage = row['STAGE']
                longitude = row['LONGITUDE']
                latitude = row['LATITUDE']
                self.excute_sql_command(insert_sql_command,
                      (proj_code, short_title, site_type, sub_type, stage, longitude, latitude))
     
            
    def close_connection(self):
        self.conn.close()


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='database.log',
                    filemode='w')