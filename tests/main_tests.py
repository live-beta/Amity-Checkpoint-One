import unittest
from app.main_amity import Room

class amity_tests(unittest.TestCase):
    """Tests for Amity functions ."""

    def __init__(self, arg):
        super(amity_tests, self).__init__()
        self.arg = arg

    def test_create_room(self):
        "Creating room Validation"
        self.assertIsInstance(self.createRoom('name','size','occupants','Y'),'Staff')
        self.assertIsInstance(self.createRoom('name','size','occupants','N'), 'Fellow')

        "Test For room creation"
        self.assertIsInstance(self)

        "Input Validation Test"
        self.assertEqual(self.createRoom('name','size','occupants'),'Invalid')



    def test_add_person(self):
        #write tests that will validate the entries of the users as to be in the correct format
        #write a systen test to differenciate between a staff and fellow

        pass

    def test_reallocate_person(self):
        pass

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
