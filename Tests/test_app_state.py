import unittest
from app.classes.person import Person
from app.classes.room import Room
from app.classes.app_state import Amity
from app.classes.dbmodels import Room, Person, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class app_state_tests(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()
        self.database_engine =create_engine("sqlite:///Test_Amity_db")
        Base.metadata.create_all(self.database_engine)
        dbsession = sessionmaker(bind=self.database_engine)
        dbsession.configure(bind=self.database_engine)
        self.session = dbsession()

        # Save sample user data
        person_class = Person()
        person_class.emp_id = '1334'
        person_class.name ='VILLY VILLIANN'
        person_class.job_type = 'FELLOW'
        person_class.office = 'LILAC'
        self.session.add(person_class)

        # Save sample room data
        room_class = Room()
        room_class.room_name = 'LILAC'
        room_class.room_type = 'OFFICE'
        room_class.capacity = 6
        room_class.c_occupants= 2
        self.session.add(room_class)

        self.session.commit()
        self.session.flush()

        self.room = Room()

    def test_save_state(self):
        "Test for successful saving "
        self.assertEqual(self.amity.save_state(db_name='andela'),'Data Saved successfully')

    def test_save_data(self):
        "Test for saving data"
        response = self.amity.save_data(self.session)
        person_data = self.session.query(Person).filter_by(emp_id='1334')
        room_data = self.session.query(Room).filter_by(room_name='LILAC')

        self.assertIsNotNone(person_data)
        self.assertIsNotNone(room_data)
        self.assertTrue(response)

    def test_load_state(self):
        "Test for loading state"
        self.assertNotEqual(self.amity.load_state(db_name='andela'),'Data loaded successfully')
