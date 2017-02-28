import unittest
from app.classes.person import Person
from app.classes.room import Room
from app.classes.app_state import Amity


class person_tests(unittest.TestCase):

    "Tests for person in amity"
    def setUp(self):
        self.person = Person()
        self.room = Room()
        self.room.create_Rooms(['LILAC', 'VALHALLA',\
                                'KRYPTON', 'SNOW'], 'OFFICE')
        self.room.create_Rooms(['JAVA', 'SHELL', 'GO', 'PHP'], 'LIVING')

    def test_add_person(self):
        "Tests for adding person"

        self.assertEqual(self.person.add_person('SAMMY','WANJALA', 'FELLOW', 1234,'Y'),'Added successfully')

        self.assertEqual(self.person.add_person('SAMMY','WANJALA','FELLOW',1234,'Y'), 'Employee already exists')

        self.assertEqual(self.person.add_person('ANDREW','STEVENS','STAFF', 3243, 'Y'), 'Accomodation is only available for fellows')

        self.assertEqual(self.person.add_person('ALICE','ALLISON','SECURITY',1334, 'Y'),'Enter correct job description')

    def test_reallocate_person(self):

        "Test for reallocating person"

        # Reallocates people successfully with correct parameters
        self.assertEqual(self.person.reallocate_person(1234,'KRYPTON'),\
                            'Reallocated successfully ')

    def test_allocation(self):

        "Test for sorting allocations"

        self.assertNotEqual(len(self.person.people_list), 0,\
                            msg="None to allocate")
        self.assertNotEqual(len(self.room.room_collection), 0,\
                            msg = "No rooms in the system")
        self.assertEqual(self.person.allocation(self.person.people_list),\
                            'Allocation complete')

    def test_print_room(self):

        "Test for printing out the people allocated"

        # Check if there are any rooms in the system

        self.assertNotEqual(len(self.room.room_collection), 0, msg="No Rooms")

        # Check if the requested room is in the list
        self.assertIn('LILAC', self.room.room_collection)

        # Check if print room can be done successfully
        self.assertEqual(self.person.print_room('LILAC'), 'Print successful')

    def test_print_unallocated(self):

        "Test for printing unallocated people"

        # for unallocated people
        self.assertNotIn('None', self.person.people_list[1234]['living_space'] or \
                             self.person.people_list[1234]['work_space'])

    def test_load_people(self):

        "Test for loading people from text file"


        self.person.load_people("people.txt")
        self.assertEqual(len(self.person.people_list),10)
