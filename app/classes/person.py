import os
from room import Room


class Person(object):

    """docstring for Person."""
    people_list = {}
    room_allocation_list = {}

    def __init__(self):
        pass

    def add_person(self, person_name, person_job, wants_room, employee_number):
        """
        Function that adds a new person to the system

        """

        person = {}
        obj_room = Room()

        # Check if the person already exists in the people list

        if person_name in Person.people_list:

            print 'The person already exists in the system'

        else:

            # Add person to app, only if they are 'STAFF' or 'FELLOW'

            if person_job.upper() == "FELLOW" or person_job.upper() == "STAFF":

                # Populate the person dictionary

                person['job'] = person_job.upper()
                person['name'] = person_name.upper()
                person['employee_num'] = employee_number
                person['job'] = person_job.upper()
                person['wants_room'] = wants_room

                # Allocate working space to person
                # work_space = obj_room.allocate_work_space()

                person['work_space'] = obj_room.allocate_work_space()

                if wants_room.upper() == 'Y' and person_job.upper() \
                        == 'FELLOW':

                    # If Fellow wants accomodation

                    room_name = obj_room.allocate_living_room()

                    # work_space = obj_room.allocate_work_space()

                    person['room'] = room_name.upper()

                elif wants_room.upper() == 'Y' and person_job.upper() \
                        == 'STAFF':

                    # An instance where Staff requests for accomodation

                    print 'Accomodation is only available for fellows'

                else:

                    # if fellow does not require accomodation

                    person['room'] = 'Unallocated'

            else:

                print 'Enter the correct job description'

        # Update the people list.

        Person.people_list[employee_number] = person

        # Print people list

        return Person.people_list

    def load_people(self):

        """
        Adding people from a text file on the users system

        """
        # Open file with people's data
        myfile = open("people.txt", "r")
        data = ""
        lines = myfile.readlines()
        for line in lines:
            data = data + line.strip()

        return data

    def reallocate_person(self, emp_no, room_name):

        """
        Placing person in a different room.

        """
        obj_room = Room()

        room_reassigned = {}

        # Assigning a new room

        room_reassigned = obj_room.reallocate(room_name.upper())

        if room_reassigned['category'] == 'OFFICE':

            # If the room returned is an office

            Person.people_list[emp_no]['work_space'] = room_reassigned['name']

        elif room_reassigned['category'] == 'LIVING' \
            and Person.people_list[emp_no]['job'] == 'FELLOW' \
                and Person.people_list['wants_room'] == 'Y':

            # If fellow wants room

            Person.people_list[emp_no]['room'] = room_reassigned['name']

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

    def print_unallocated(self):

        """
        Prints out all the people who are unallocates in the system

        """
        unallocated_list = []
        return unallocated_list


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
