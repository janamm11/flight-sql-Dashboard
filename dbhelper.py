import  mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class DB:
    def __init__(self):
        #connect to database
        try:
            self.conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
            )
            self.mycursor = self.conn.cursor()
            print("Connected to database")
        except mysql.connector.Error as e:
            print(f"Connection error: {e}")

    def fetch_city_names(self):
        city = []
        self.mycursor.execute("""
        select distinct(Destination) from flight.flights_cleaned
         union
         select distinct(Source) from flight.flights_cleaned
        """)
        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
        return city

    def fetch_all_flights(self,source,destination):

        self.mycursor.execute("""
                              select Airline,Route,Dep_Time,Duration,Price from flight.flights_cleaned
                              where Source='{}' and Destination= '{}'
                              """.format(source,destination))
        data = self.mycursor.fetchall()
        return data

    def fetch_airline_frequency(self):
        airline = []
        frequency = []

        self.mycursor.execute("""
                              select Airline,count(*) from flight.flights_cleaned
                              group by Airline""")
        data = self.mycursor.fetchall()
        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline,frequency

    def busy_airport(self):
        city = []
        frequency = []

        self.mycursor.execute("""
                              select Source,count(*) from (select Source from flights_cleaned
                              union all 
                              select Destination from flights_cleaned)t
                              group by t.Source
                              order by count(*) desc
                              """)
        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city,frequency