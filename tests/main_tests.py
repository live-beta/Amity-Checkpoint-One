import unittest
from app.main_amity import Room,Person

class amity_tests(unittest.TestCase):
    """Tests for Amity functions ."""

    def test_Room(self):
        "Creating room Validation"

        self.assertIsInstance(Room.createRoom('name',7,-1,'Y'),'Capacity Problems')
        self.assertIsInstance(Room.createRoom(1234,'size','Y'),'Invalid Naming')

        "Input Validation Test"
        self.assertEqual(Room.createRoom('name','size','occupants'),'Invalid')
        #inputs should be block letters

    def test_add_person(self):

        "Test for successful creation"
        self.assertTrue(Person.add_person('name','gender','category','employee_num'))
        self.raises
         #having relevant variables, name, genfer

    def test_load_people(self):
        pass

    def test_print_allocations(self):
        pass

    def test_print_unallocations(self):
        pass

    def test_print_room(self):
        pass

    def test_save_state(self):
        pass

    def test_load_state(self):
        pass
