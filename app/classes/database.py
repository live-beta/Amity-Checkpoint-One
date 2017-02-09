import sqlite3
#from app.main_amity import Room,Person



class Database(object):

    """docstring for Amity Database."""
    def __init__(self):
        self.database_name = ""
        self.database = None
        self.cursor = None

    def create_db(self):

        self.database_name = database_name
        #vonfirmation that databse has the correct extention
        if self.database_name[-2].uppper() !="DB":
            self.database_name +=".db"

        self.openDatabase()
        self.closeDatabase()

    def openDatabase(self):

        # Establishing database connections

        self.database =sqlite3.connect(self.database_name)

        # Instanciating the cursor

        self.cursor =self.database.cursor()

    def closeDatabase(self):

        # Destroying the cursor

        self.cursor.close()

        #Closing the Database

        self.database.close()


    def create_db_tables(self):

        self.openDatabase()

        # Creating the rooms table, with the unique names and occupants

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Rooms
                (
                room_name TEXT NOT NULL UNIQUE,
                room_type TEXT NOT NULL,
                room_member_A TEXT NULL,
                room_member_B TEXT NULL,
                room_member_C TEXT NULL,
                room_member_D TEXT NULL,
                room_member_E TEXT NULL,
                room_member_F TEXT NULL


                )

        ''')

        # Saving information to table

        self.database.commit()

        # Creating table for Person

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Person
                (
                person_name TEXT NOT NULL ,
                employee_num TEXT NOT NULL PRIMARY KEY UNIQUE,
                category TEXT NOT NULL,
                wants_room TEXT NOT NULL,
                is_allocated TEXT NOT NULL
                    )
            ''')

        # Save information to person table

        self.database.commit()

        # Creating table for room occupants

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Room_Occupants
                (
                room_name TEXT NOT NULL ,
                employee_num TEXT NOT NULL PRIMARY KEY UNIQUE,
                person_name TEXT NOT NULL,
                category TEXT NOT NULL,
                    )
            ''')
        # Persisting room occupation and closing the database.
        self.database.commit()
        self.closeDatabase()

    def create_room(self):

        "Adding a new room to the database"

        self.openDatabase()
        try:
            if len(state_store.list_of_rooms)>0:
                for rooms in range(0,len(state_store.list_of_rooms)):
                    room_name = state_store.list_of_rooms.room_name
                    room_type =state_store.list_of_rooms.room_type
                    room_member= state_store.list_of_rooms.Room_Member
                    for rooms in range(len(room_member),6):
                        room_member.append("")
                    self.cursor.execute('''
                        INSERT INTO Rooms VALUES(?,?,?,?,?,?,?,?,?)''',(
                        room_name,
                        room_type,
                        room_member[0],
                        room_member[1],
                        room_member[2],
                        room_member[3],
                        room_member[4],
                        room_member[5]))
                    self.db.commit()

                    for members in range(len(room_member)):
                        self.cursor.execute('''
                            INSERT INTO room_members VALUES(?,?)''',(room_name, room_member[members]))
                        self.db.commit()
        except Exception as e:
            raise e
        self.closeDB()


    def create_person(self):

        "Adding a new person to database"

        # Opening database

        self.openDatabase()

        # Attempt to save information into database

        try:
            if len(People.people_list) > 0:
                for people in range(0,len(People.people_list)):
                    person_name = People.people_list[people].name
                    employee_num = People.people_list[people].employee_num
                    category = People.people_list[people].category
                    wants_room = People.people_list[people].wants_room

                    self.cursor.execute('''
                        INSERT INTO Person VALUES(?,?,?,?,?) ''',(
                        person_name,
                        employee_num,
                        category,
                        wants_room)
                        )
                    self.database.commit()

        except Exception as e:
            raise e
        #Closing database connection
        self.closeDatabase()

    def get_allocation(self):

        "Getting information for roon allocations"

        self.openDatabase()
        try:
            # Executing the selection command for all room occupants
            self.cursor.execute('''
                SELECT person_name,room_allocated FROM person WHERE Wants_Room = ? AND Is_Allocated = ?
            ''',("YES","1"))
            # Assigning information to data dictionary

            allocation_data = self.cursor.fetchall()
            state_store.room_allocation = {}

            for rows in allocation_data:
                room_allocation.update(str(rows[0]))

        except Exception as e:
            raise

        # Closing the database
        self.closeDatabase()

        pass

    def retrieve_unalocated(self):

        # Retrieving data for unalocated people_list
        self.openDatabase()
        try:
            self.cursor.execute('''
                SELECT * FROM Person WHERE wants_room = ? AND Is_Allocated = ?
            ''',("YES","0"))

            people_data= self.cursor.fetchall()
            unallocated_people=[]
            for rows in people_data:
                unallocated_people.append(str(rows[0]))
        except Exception as e:
            raise e

        # Closing the database

        self.closeDatabase()


    def retrieve_allocated(self):

        # Retieving data for people who are allocated rooms

        self.openDatabase()
        try:
            self.cursor.execute('''
                SELECT * FROM Person WHERE wants_room = ? AND Is_Allocated = ?
            ''',("YES","1"))

            people_data= self.cursor.fetchall()
            allocated_people=[]
            for rows in people_data:
                allocated_people.append(str(rows[0]))
        except Exception as e:
            raise e

        # Closing the database

        self.closeDatabase()

    def get_rooms(self):
        pass
    def retrieve_people_info(self):

        # Loading information for all people.

        self.openDatabase
        try:
            self.cursor.execute('''
                SELECT * FROM Person
            ''')
            people_data=self.cursor.fetchall()
            for rows in people_data:
                pinf= Person(rows[0], rows[1], rows[2],rows[3], rows[4])
                people_list_final.append(pinf)

        except Exception as e:
            raise e# coding=utf-8

        self.closeDatabase()

        return people_list_final

    def retrieve_people(self):
        pass
    def save_state(self):
        pass
    def load_state(self):
        pass
    def clear_tables(self):
        pass
    def Save(self,database):
        self.database =database
        self.create_db(self.database)
        self.create_db_tables()
        self.insert_room_data_into_db()

    def Load (self,database):
        self.db_name="{}.db".format(database)
        self.retrieve_data_from_db_for_allocated()
        self.retrieve_data_from_db_for_unallocated()
        self.retrieve_data_from_db_for_all_rooms()
        self.retrieve_data_from_db_for_people_info()
        self.retrieve_data_from_db_for_all_people()
