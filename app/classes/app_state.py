from dbmodels import (Base, create_database,
                      Room as room_model,
                      Person as person_model)
from person import Person
from room import Room

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError


class Amity(object):

    """Amity has the state of all rooms and the number of people."""

    def save_state(self, db_name='amity_db'):
        """Saves people to the database"""
        ret_value = self.save_data(create_database(db_name))
        if ret_value:
            return 'Data Saved successfully'
        return ret_value

    def save_data(self, session):
        '''use the passed session to save data'''
        for key in Person.people.keys():
            person_class = person_model()
            person_class.emp_id = Person.people[key]['employee_num']
            person_class.name = Person.people[key]['name']
            person_class.job_type = Person.people[key]['job']
            person_class.office = Person.people[key]['office']
            person_class.living_space = Person.people[key]['livingspace']

            session.add(person_class)
            try:
                session.commit()
            except IntegrityError:
                session.rollback()
                return 'Person with ID %s already exists' % person_class.name

        for key in Rooms.room_list.keys():
            room_class = room_model()
            room_class.room_name = Rooms.room_list[key]['room_name']
            room_class.room_type = Rooms.room_list[key]['room_category']
            room_class.capacity = Rooms.room_list[key]['room_size']
            room_class.c_occupants = Rooms.room_list[key]['occupants']
            session.add(room_class)
            try:
                session.commit()
            except IntegrityError:
                session.rollback()
                return 'Room with name %s already exists'\
                    '' % room_class.room_name
        return True

    def load_state(self, db_name='amity_db'):
        """Loads all the data back to the application once it is opened"""

        engine = create_engine("sqlite:///" + db_name)
        Base.metadata.bind = engine
        dbsession = sessionmaker(bind=engine)
        ret_value = self.load_data(dbsession())
        if ret_value:
            return 'Data loaded successfully'
        return ret_value

    def load_data(self, session):
        '''Use the passed session to load data'''
        rooms = session.query(room_model).all()

        people = session.query(person_model).all()
        if len(rooms) > 0:
            for room in rooms:
                r_models = {}
                r_models['room_name'] = room.room_name
                r_models['room_category'] = room.room_type
                r_models['capacity'] = room.capacity
                r_models['occupants'] = room.c_occupants

                Rooms.room_list[room.room_name] = r_models

        else:
            print('No Rooms Available')

        if len(people) > 0:
            for person in people:
                p_model = {}
                p_model['name'] = person.name
                p_model['job'] = person.job_type
                p_model['employee_number'] = person.emp_id
                p_model['work_space'] = person.office
                p_model['living_space'] = person.living_space

                Person.people[person.employee_num] = p_model
        else:
            print('No People Registered')
