import os
from room import Room, Living_Space, Office


class Person(object):

    """docstring for Person."""
    people_list = {}
    room_allocation_info = {}
    person_info = []

    def __init__(self):

        pass

    def add_person(self, first_name, second_name, person_job, employee_number, wants_room):
        """
        Function that adds a new person to the system

        """
        # if first_name is None:
        #     return 'Invalid first name input'

        person = {}
        obj_living = Living_Space()
        obj_office = Office()
        # obj_office = Office()

        # Check if the person already exists in the people list

        if employee_number in Person.people_list:

            return 'Employee already exists in the system, check the employee number'

        # Add person, only if they are 'STAFF' or 'FELLOW'

        if person_job.upper() == "FELLOW" or person_job.upper() == "STAFF":

            # Populate the person dictionary

            person['job'] = person_job.upper()
            person['name'] = first_name.upper() + ' ' + second_name.upper()
            person['employee_num'] = employee_number
            person['job'] = person_job.upper()
            person['wants_room'] = wants_room
            person['work_space'] = obj_office.allocate_office_space()

            # Capturing the allcation transaction infomrmation
            if wants_room.upper() == 'Y' and person_job.upper() \
                    == 'FELLOW':

                # If Fellow wants accomodation

                living_space = obj_living.allocate_living_room()

                # work_space = obj_room.allocate_office_space()

                person['room'] = living_space.upper()

            elif wants_room.upper() == 'Y' and person_job.upper() \
                    == 'STAFF':

                # An instance where Staff requests for accomodation

                return 'Accomodation is only available for fellows'

            else:

                # if fellow does not require accomodation

                person['room'] = 'Unallocated'

        else:

            return 'Enter the correct job description'

        # Update the people list.

        Person.people_list[employee_number] = person
        persons_data = Person.people_list
        self.allocation(persons_data)

        # Print people list

        return Person.people_list

    def reallocate_person(self, emp_no, work_space):

        """
        Placing person in a different room.
e
        """
        obj_room = Room()

        room_reassigned = {}

        initial_room = Person.people_list[emp_no]['work_space']

        # Assigning a new room

        if work_space == initial_room:
            return 'Cannot be reassigned to the same room'

        room_reassigned = obj_office.reallocate_office_space(work_space.upper(),initial_room)

        if room_reassigned['category'] == 'OFFICE':

            # If the room returned is an office

            Person.people_list[emp_no]['work_space'] = room_reassigned['name']

            self.allocation(Person.people_list)


        elif room_reassigned['category'] == 'LIVING' \
            and Person.people_list[emp_no]['job'] == 'FELLOW' \
                and Person.people_list['wants_room'] == 'Y':

            # If fellow wants room_reassi

            Person.people_list[emp_no]['room'] = room_reassigned['name']
            self.allocation(Person.people_list)

        elif room_reassigned['category'] == 'LIVING' \
            and Person.people_list[emp_no]['job'] == 'FELLOW' \
                and Person.people_list['wants_room'] == 'N':

                # If the fellow being assigned did not require a room

                option = raw_input('The fellow did not require a room before,\
                        are you sure you want to proceed? Y|N')

                if option == 'Y':

                    Person.people_list[emp_no]['room'] \
                        = room_reassigned['name']

                elif option == 'N':
                    return 'The fellow does not require a room'

                else:

                    return 'Invalid input'

        elif room_reassigned['category'] == 'LIVING' \
                and Person.people_list[emp_no]['job'] == 'STAFF':

            return 'Staff not allowed to have accomodation on site'

        return Person.people_list

    def allocation(self, person_data):
        """
        Adds information to the allocations record
        """
        obj_room = Room()
        room_key = {}
        occupants = 0

        # Stepping throught the room dictionary to locate available
        for key0, room in obj_room.room_list.items():

            room_key[key0.upper()] = ''

        # Lopping through the people list using the room key
        for key, person in person_data.items():
            person_room = person['work_space'].upper()
            occupants += 1
            if person_room in room_key:
                room_key[person_room] += (" ".join(person['name']) + "\n")

        for info in room_key:
            print info.upper()
            print '-' * 20
            print room_key[info]
            print '_' * 20

    def print_allocations(self):
        """
        Prints out allocation information

        """
        obj_room = Room()
        people_info = Person.people_list
        room_key = {}

        # loading data from fictionary

        for nkey, room in obj_room.room_list.items():
            room_key[nkey.upper()] = ''

        # Lopping through the people list using the room key
        for key, person in people_info.items():
            person_room = person['work_space'].upper()

            if person_room in room_key:
                room_key[person_room] += (" ".join(person['name']) + "\n")

        for info in room_key:
            print info.upper()
            print '-' * 20
            print room_key[info]
            print '_' * 20

    def print_room(self, work_space):

        """
        Printing people in a room
        """
        obj_room = Room()
        rooms = obj_room.room_list
        room_id = []
        persons_data = Person.people_list

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

        for key, person in Person.people_list.items():

            if person['work_space'] == 'None':
                unallocated_list.append(person['name'])

        if len(unallocated_list) == 0:
            return 'There are no unallocated people'
        else:
            return unallocated_list

    def load_people(self):

        """
        Adding people from a text file on the users system

        # """
        # myfile = open("people.txt", "r")
        # data = ""
        # lines = myfile.readlines()
        # print lines
        # for line in lines:
        #     data = data + line.strip()
        # print data


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
