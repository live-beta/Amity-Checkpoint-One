import unittest
#from app.classes.amity import Amity
from app.classes.person import Person
from app.classes.room import Room
#from app.classes.main_amity import Room,Person
from app.classes.database import Database

class amity_tests(unittest.TestCase):


    """Tests for Amity functions ."""
    # Creating an instance of Room,Person and Database

    def setUp(self):

        # Instanciating class wide Objects

        self.Person = Person()
        self.Room = Room ()
        self.database = Database()


    def test_create_Rooms(self):


        "Test for retrieving data from database, assigning to list"

        self.assertTrue(self.database.openDatabase(),msg="Was not able to communicate with database")
        self.assertTrue(self.database.select_all_rooms(), msg="Was not able to communiate with database")

        room_list_initial= self.main_amity.load_rooms()


        "Test for instance variables"

        # Check if the data is being returned successfully from database

        self.assertNotEqual(len(room_list_initial),0,msg="The room records can not be blank")

        # Check if the room code is in the correct format

        self.assertEqual(self.Room.name,'CYAN',msg="Check that the room code is valid")

        # Checking the room categories as being in the correct range of rooms

        self.assertIn(self.Room.category,['LIVING_SPACE','OFFICE'],msg="Category can only be OFFICE or LIVING area")

        # Check if the office are in the right size categories

        self.assertTrue(self.Room.office_size < 6,msg="Room size should not be greater than 6")

        # Check if the rooms are of the correct size

        self.assertTrue(self.Room.office_size >0,msg="The Room size should be greater than 0")

        # Checking if the living spaces are of the right size

        self.assertTrue(self.Room.living_space < 5, msg="Check if the living space is of the correct size")

        #Checking if living space is not null

        self.assertTrue(self.Room.living_space >0, msg="The room size should be greater than 0")

        # Check if there is already an instance of the room being created

        self.assertIn(self.Room.name,room_list_initial,msg="Cannot save, already exists")


    def test_add_person(self):

        "Test for retrieving application data."

        # self.assertTrue(self.database.openDatabase())
        # self.assertTrue(self.database.select_all_people())

        # Loading people data from application data

        people_initial_list = self.Person.load_people()

        "Test for instance variables"

        # Check if application returns a null People record

        self.assertNotEqual(len(people_initial_list),0,msg="The people record set is blank")

        # Check for the correct employee number format

        self.assertEqual(self.Person.emp_num.upper(),'C-13-N1-01-06N',msg="The employee number is in the wrong format")

        # Check for correct employee category

        "Test for checking if person already exists"

        # Comparing with current list elements

        self.assertIn(self.Person.employee_num,people_list_initial,msg="Person already exists in the system, cannot add")

        "Test for adding new person to a list"

        # Check for an additional person in the system

        self.assertTrue(len(people_list_initial)<len(people_list_final),msg="No new entry made")


    def test_reallocate_person(self):

        "Test for person reallocation"

        # Loading data dictionary for the people as allocated

        person_allocation_details = self.Person.people_list

        # Loading data dictionary for the people as reallocated

        person_reallocation_details = self.Person.reallocate_person(0,"CYAN")

        # Cheking if the reallcation was successful

        self.assertFalse(person_allocation_details == person_reallocation_details,msg="The allocation not successful")


    def test_load_people(self):

        "Test for loading people from a txt file"

        # Loading data dictionary as read from the text file

        people_list = self.Person.load_people()

        # Check for a populated data set

        self.assertNotEqual(len(people_list),0,msg="People have not been loaded")

        # Check for data presented in the correct format

        self.assertEqual(people_list,{'["SAMMY WANAJALA","FELLOW","Y"]','["STEVENS","WAMALWA","N"]'},msg="Not in the correct format")


    def test_print_allocations(self):


        "Test for printing allocations"

        room_allocation = self.Room.print_room()

        # Checking for data availability in the loded list

        self.assertNotEqual(len(room_allocation),0,msg="The list contains no allocations")

        # Check for the correct print format

        self.assertEqual(room_allocation,{'["CYAN","SAMMY WANJALA","S3424"]'})


    def test_print_unallocated(self):


        "Test for Printing unallocated people"

        people_unallocated = self.Person.print_unallocated()

        # Checking for data availability in the loaded list

        self.assertNotEqual(len(people_unallocated),0,msg="the list contains no unallocations")

        # Checking for the correct output format

        self.assertEqual(people_unallocated,{'["SAMMY WANJALA","N"]'},msg="Your information is not in the correct format")


    def test_print_room(self):


        "Test for printing room and its occupants"

        room_details = self.Room.print_room()

        # Checking for data availability in the loaded list of rooms and occupants

        self.assertNotEqual(len(room_details),0, msg="Room data has not been loaded")

        # Checking for the correct data output format

        self.assertEqual(room_details,{["HOGWARTS"],["SAMMY WANJALA","FELLOW"]})



    def test_save_state(self):

        "Test for saving the data state"

        # Loading people dictionary data from database

        people_list_initial= self.Person.load_people()

        # Loading people dictionary in the most resent application state

        people_list_final= self.Person.add_person('SAMMY WANJALA','C-13-N1-01-06N','FELLOW','Y','N')

        # Loading Room dictionary data from database

        room_list_initial= self.Room.load_Rooms()

        # Loading Room dictionary data from the most resent application state

        room_list_final= self.Room.create_Rooms('HOGWARTS','OFFICE','H001','6','0')

        # Checking for additional data in the people list

        self.assertTrue(len(people_list_initial) < len(people_list_final), msg="Saved successfully")

        #Checking for additional data in the rooms list.

        self.assertTrue(len(room_list_initial) < len(room_list_final),msg="Rooms added")



    def test_load_state(self):

        pass
