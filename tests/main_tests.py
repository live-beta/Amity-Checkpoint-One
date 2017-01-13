import unittest
from app.main_amity import Room,Person

class amity_tests(unittest.TestCase):

    """Tests for Amity functions ."""

    def test_create_Rooms(self):

        self.Room= Room()

        "Test for instance variables"

        self.assertNotEqual(self.Room.name,"", msg="Not able to add Blank room name")
        self.assertEqual(self.Room.roomcode,'C400',msg="Check that the room code is valid")
        self.assertIn(self.Room.category,['LIVING','OFFICE'],msg="Category can only be OFFICE or LIVING area")
        self.assertTrue(self.Room.roomsize < 6,msg="Room size should not be greater than 6")
        self.assertTrue(self.Room.roomsize >0,msg="The Room size should be greater than 0")

        "Test for adding new rooms in system"
        #self.assertTrue(self.Room.create_Rooms(self,roomcode,name,category,roomsize))

"""
    def test_add_person(self):

        self.Person=Person()

        "Test for instance variables"

        self.assertNotEqual(self.Person.name,"",msg="You cannot enter a blank name to the system")
        self.assertEqual(self.Person.personcode,'N400',msg="Check that the person code is valid")
        self.assertIn(self.Person.category.upper(),['FELLOW','STAFF'],msg="Person should either be FELLOW or STAFF")

        "Output tests"
        self.assertTrue(self.Person.add_person(self,name,personcode,category))

    def test_load_people(self):
        self.Person = Person()

        "Testing for loaded varibles"
        self.assertEqual(self.Person.load_people(self,personcode),{N400:"Sammy Wanjala"})

    def test_print_allocations(self):
        "Checking result format"
        ""
        pass

    def test_print_unallocations(self):
        pass

    def test_print_room(self):
        pass

    def test_save_state(self):
        pass

    def test_load_state(self):
        pass
"""
