import os
from room import Room, Living_Space, Office, Living_Space
from random import randint


class Person(object):

    """docstring for Person."""
    people_list = {}
    room_allocation_info = {}
    person_info = []
    obj_room = Room()
    obj_living = Living_Space()
    obj_office = Office()

    def __init__(self):

        self.first_name = None
        self.second_name = None
        self.person_job = None
        self.employee_number = None
        self.wants_room = None



    def add_person(self, first_name, second_name, person_job, employee_number, wants_room):

        """
        Function that adds a new person to the system

        """
        person = {}

        # Check if the person already exists in the people list

        if employee_number in self.people_list:

            return 'Employee already exists in the system, \
                        check the employee number'

        # Add person, only if they are 'STAFF' or 'FELLOW'

        if person_job.upper() == "FELLOW" or person_job.upper() == "STAFF":

            # Populate the person dictionary

            person['job'] = person_job.upper()
            person['name'] = first_name.upper() + ' ' + second_name.upper()
            person['employee_num'] = employee_number
            person['wants_room'] = wants_room

            office = self.obj_office.allocate_office_space()

            if office == 'None':
                person['work_space'] = 'Unallocated'
            else:
                person['work_space'] = office['room_name']

            # Capturing allocation transaction
            if wants_room.upper() == 'Y' and person_job.upper() \
                    == 'FELLOW':

                # If Fellow wants accomodation

                living_space = self.obj_living.allocate_living_room()

                # work_space = obj_room.allocate_office_space()

                person['living_space'] = living_space.upper()
            elif wants_room.upper() == 'N' and person_job.upper() \
                    == 'FELLOW':

                    person['living_space'] = None

            elif wants_room.upper() == 'Y' and person_job.upper() \
                    == 'STAFF':

                # An instance where Staff requests for accomodation

                return 'Accomodation is only available for fellows'

        else:

            return 'Enter the correct job description'

        # Update the people list.

        self.people_list[employee_number] = person
        persons_data = self.people_list
        self.allocation(persons_data)


    def reallocate_person(self, emp_no, space):

        """
        Placing person in a different room.

        """
        living_rooms = []
        work_space = []

        for index, area in Room.room_list.items():

            if area['room_category'] == 'LIVING':
                # Loading  all the living rooms
                living_rooms.append(index.upper())

            if area['room_category'] == 'OFFICE':
                work_space.append(index.upper())

        if space in living_rooms:

            if self.people_list[emp_no]['job'] == 'STAFF':
                return 'Cannot reallocate Staff to living room'

            initial_room = self.people_list[emp_no]['living_space']
            allocation_preference = self.people_list[emp_no]['wants_room']

            if space == initial_room:
                return 'Cannot reallocate to the same room'

            reassign = self.obj_living.reallocate_living_room(space.upper(), initial_room)

            if reassign == True:

                if allocation_preference == 'N':

                    return 'Person does not want a living room'

                self.people_list[emp_no]['living_space'] = space

            else:

                return 'Reallocation not successful'

        elif space in work_space:

            initial_room = self.people_list[emp_no]['work_space']

            if space is initial_room:
                return 'Cannot allocate to the same room'
            reassign = self.obj_office.reallocate_office_space(space.upper(),initial_room)

            if reassign is True:

                self.people_list[emp_no]['work_space'] = space.upper()
        else:

            return 'Enter a correct room name'

        self.allocation(self.people_list)

    def allocation(self, person_data):

        """
        Adds information to the allocations record
        """
        room_key = {}
        occupants = 0

        # Searching dictionary to locate available rooms
        for key0, room in self.obj_room.room_list.items():

            room_key[key0.upper()] = ''

        # Lopping through the people list using room key
        for key, person in person_data.items():

            if person['job'] == 'FELLOW' and len(Room.room_list) > 1:
                person_living_room = person['living_space']
                person_working_room = person['work_space']
                occupants += 1

                if person_living_room in room_key:
                    room_key[person_living_room] \
                        += (" ".join(person['name']) + "\n")

                if person_working_room in room_key:
                    room_key[person_working_room] \
                            += (" ".join(person['name']) + "  " + " ".\
                                join(person['job'].lower()) + "\n")

            elif person['job'] == 'STAFF':
                person_working_room = person['work_space']

                occupants +=1

                if person_working_room in room_key:

                    room_key[person_working_room] += (" ". \
                            join(person['name']) +"  " + " -" +  " ".\
                                join(person['job'].lower()) + "\n")
            else:
                return 'Are no rooms in the system'

        for info in room_key:
            print info.upper()
            print '-' * 20
            print room_key[info]
            print '_' * 20

    def print_allocations(self):
        """
        Prints out allocation information

        """
        people_list = self.people_list
        return self.allocation(people_list)

    def print_room(self, work_space):

        """
        Printing people in a room
        """
        rooms = self.obj_room.room_list
        room_id = []
        persons_data = self.people_list

        if len(rooms) == 0:
            print 'There are no rooms in the system'
        else:
            # Populating the room key

            for room_key, room in rooms.items():
                room_id.append(room_key.upper())

            # Checking if room is in the room key

            if work_space.upper() in room_id:

                # Createing a holder dictionary for display

                r_key = {work_space.upper(): ''}

                for person_key, person in persons_data.items():

                    person_room = person['work_space'].upper()

                    if person_room == work_space.upper():
                        r_key[person_room] += (" ".join(person['name']) + "\n")

                for room_info in r_key:
                    print room_info.upper()
                    print '_' * 20
                    print r_key[room_info]
                    print '_' * 20

            else:
                print 'There is no room named ' + work_space.upper()

    def print_unallocated(self):

        """
        Prints Unallocated people

        """
        unallocated_list = []

        for key, person in self.people_list.items():

            if person['work_space'] == 'None':
                unallocated_list.append(person['name'])

        if len(unallocated_list) == 0:
            return 'There are no unallocated people'
        else:
            return unallocated_list

    def load_people(self, filename):

        """
        Adding people from a text file

        """
        with open(filename, 'r') as people_file:
            people = people_file.readlines()

            for person in people:
                person = person.split(' ')

                if len(person) == 3:
                    # if there are three values
                    first_name = person[0]
                    second_name = person[1]
                    job_type = person[2].strip()
                    wants_accommodation = "N"
                    employee_number = randint(0, 1000)
                    self.add_person(first_name, second_name, job_type.upper(),\
                                    employee_number, wants_accommodation)

                elif len(person) == 4:
                    # If there are four values
                    first_name = person[0]
                    second_name = person[1]
                    job_type = person[2].strip()
                    employee_number = randint(0,1000)
                    wants_accommodation = person[3].strip()

                    self.add_person(first_name, second_name, job_type.upper(), \
                                    employee_number, wants_accommodation)

                else:
                    return 'Not available'

            return 'successfully added'


class Fellow(Person):

    """docstring for FELLOW, subclass of Person."""

    def __init__(self, arg):
        super(fellow, self).__init__()
        self.arg = arg

    def allocate_living_room(self, emp_no):
        pass


class Staff(Person):

    """docstring for staff subclass of Person."""

    def __init__(self, arg):
        super(staff, self).__init__()
        self.arg = arg
