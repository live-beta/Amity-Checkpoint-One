import unittest
#from app.classes.person import Person
from app.classes.room import Room, Living_Space, Office
from app.classes.app_state import Amity


class room_tests(unittest.TestCase):

    "Tests for person in amity"

    def setUp(self):

        self.room = Room()
        self.living = Living_Space()
        self.office = Office()

    def test_create_rooms(self):
        "Test for creating a new room"

        self.assertIn('LILAC', self.room.room_collection)
        self.assertIn('JAVA', self.room.room_collection)
        self.assertEqual(self.room.create_Rooms(['LILAC'],'OFFICE'),\
                                'The Room already exists in the system')
        self.assertEqual(self.room.room_collection['LILAC']['room_category'],'OFFICE')

    def test_print_room(self):

        "Test for room printing"

        # Check if the room being printed exists
        self.assertIn(self.room.print_room('LILAC')[0],self.room.room_collection)

    def test_allocate_living_room(self):

        "Test for room allocations"
        # Test for room availability
        self.assertNotEqual(len(self.room.room_collection),0)

        self.assertNotIn('BAMBOO',self.room.room_collection)

        # reallocated living room exists in system
        self.assertIn(self.living.allocate_living_room(),self.room.room_collection)

    def test_reallocate_living_room(self):
        "Test for room reallocated successfully"

        # Test room availability
        self.assertNotEqual(len(self.room.room_collection),0, \
                        msg='There are no more availble rooms in the system')

        # Assert a working reallocation scenario
        self.assertEqual(self.living.reallocate_living_room('JAVA','GO'),True)

    def test_allocate_office_space(self):

        "Test for office space allcations"

        # Test for room availability
        self.assertNotEqual(len(self.room.room_collection),0)

        # Should not return a null values
        self.assertNotEqual(self.office.allocate_office_space(),'')

    def test_reallocate_office_space(self):

        "Test for reallocating office spaces"

        # Test rooms available
        self.assertNotEqual(len(self.room.room_collection),0)

        # Asserting a working operation
        self.assertEqual(self.office.reallocate_office_space('SNOW',\
                            'LILAC'), True)
