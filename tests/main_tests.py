import unittest
from app.classes.main_amity import Room,Person
from app.classes.database import Database

class amity_tests(unittest.TestCase):


    """Tests for Amity functions ."""

    def test_create_Rooms(self):

        self.Room = Room()
        self.database = Database()

        "Test for retrieving data from database, assigning to list"

        self.assertTrue(self.database.openDatabase())
        self.assertTrue(self.database.select_all_rooms())

        # people_list_initial = self.main_amity.load_people()
        room_list_initial= self.main_amity.load_rooms()

        "Test for instance variables"

        # Check if the database returns a null Room record

        self.assertNotEqual(len(room_list_initial),0,msg="The room records can not be blank")

        # Check if the room code is in the correct format

        self.assertEqual(self.Room.roomcode,'C400',msg="Check that the room code is valid")

        # Checking the room categories as being in the correct range of rooms

        self.assertIn(self.Room.category,['LIVING_SPACE','OFFICE'],msg="Category can only be OFFICE or LIVING area")

        # Check if the office are in the right size categories

        self.assertTrue(self.Room.office_size < 6,msg="Room size should not be greater than 6")

        # Check if the rooms are of the correct size

        self.assertTrue(self.Room.office_size >0,msg="The Room size should be greater than 0")

        # Checking if the living spaces are of the right size

        self.assertTrue(self.Room.living_space < 4, msg="Check if the living space is of the correct size")

        # Check if room already exists

        self.assertIn(self.Room.roomcode,room_list_initial,msg="Cannot save, already exists")

        "Test for adding new room to list"

        self.assertTrue(self.Room.create_Rooms(self,roomcode,name,size,category),msg="Room not created")



    def test_add_person(self):

        self.Person = Person()
        self.database = Database()

        "Test for retrieving data from database, assigning to people list"

        self.assertTrue(self.database.openDatabase())
        self.assertTrue(self.database.select_all_people())

        # Loading database items to list

        people_list_initial = self.Person.load_people()

        "Test for instance variables"

        # Check if the database returns a null People record

        self.assertNotEqual(len(people_list_initial),0,msg="The people record set is blank")

        #Checking if the employee number is in the correct format

        self.assertEqual(self.Person.employee_num,'')

        # Check for the correct employee number format

        self.assertEqual(self.Person.employee_num.upper(),'C-13-N1-01-06N',msg="The employee number is in the wrong format")

        # Check for correct employee category

        "Test for checking if person already exists"

        # Comparing with current list elements

        self.assertIn(self.Person.employee_num,people_list_initial,msg="Person already exists in the system, cannot add")

        "Test for adding new person to a list"

        # Check for item incrementation

        self.assertTrue(len(people_list_initial)<len(people_list_final),msg="No new entry made")

        #Check for successful save operation

        self.assertTrue(self.Person.add_person(self,name,gender,category,employee_num),msg="Room not created")

    def test_reallocate_room(self):

        self.Person = Person()
        self.Room = Room()

        "Test for getting personal data using identifier"

        person_allocation_details=self.Person.load_person()
        person_reallocation_details=self.Room.reallocate_person()

        "Test for allocation"

        #Checking if the list before and after allocation are the same

        self.assertFalse(person_allocation_details == person_reallocation_details,msg="The allocation not successful")

        #new_room_name


    def test_load_people(self):

        self.Person = Person()

        "Test for reading people from a txt file"

        #Loading people data
        people_list = self.Person.load_people()

        "Test data set"
        self.assertEqual(people_list,{'["SAMMY WANAJALA","FELLOW","Y"]','["STEVENS","WAMALWA","N"]'},msg="Not in the correct format")

        #Check if the data set is empty

        self.assertNotEqual(len(people_list),0,msg="People have not been loaded")


    def test_print_allocations(self):

        "Test for empty record set"
        "Test for correct data structure"
        "Test for instance variable"

        pass

    def test_print_unallocations(self):
        "Testing for unallocations"
        "Printing formats"
        "Instance Variables"
        pass

    def test_print_room(self):
        pass

    def test_save_state(self):

        self.Person = Person()
        self.Room =Room()


        "Testing for additional data"

        #Assigning function return values for people and rooms

        people_list_initial= self.Person.load_people()
        people_list_final= self.Person.add_person()
        room_list_initial= self.Room.load_Rooms()
        room_list_final= self.Room.create_Rooms()

        #Checking for additional data in the people list

        self.assertTrue(len(people_list_initial) < len(people_list_final), msg="There is no one to save")

        #Checking for additional data in the rooms list.

        self.assertTrue(len(room_list_initial) < len(room_list_final),msg="No additional rooms")


        "Test if the additional  data is already in database"


        "Test for correct data format"

        pass

    def test_load_state(self):

        pass
