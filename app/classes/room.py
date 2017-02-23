from random import randint


class Room(object):

    """docstring for Room."""

    room_list = {}
    people_in_room_data = {}

    def __init__(self):
        pass

    def create_Rooms(self, room_names, room_category):

        """
        Creates a new room entry by ensuring that
        there are no duplicate entries,correct size and category

        """

        room = {}
        people = {}

        # Check if the room already exists in the room list
        for room_name in room_names:

            if room_name in Room.room_list:

                print 'The Room already exists in the system'

            else:

                # Populate room decitionary

                room['room_category'] = room_category.upper()
                room['room_name'] = room_name.upper()
                room['occupants'] = 0
                room['status'] = 'available'

                if room_category == 'LIVING':

                    # Living rooms should have 4 occupants

                    room['room_size'] = 4

                elif room_category == 'OFFICE':

                    # Office rooms should have 6 occupants

                    room['room_size'] = 6

            Room.room_list[room_name] = room

    def print_room(self, room_name):

        """Prints out the rooms that are available
         in the system

         """

        # Declaring a list of all avaialable rooms

        room_element = []

        # Looping through the room dictionary
        for room in Room.room_list:
            room_element.append(room)

        return room_element

    def load_Rooms(self):

        # Open file with room data
        room_data = open('load_rooms.txt')

        # Read the first line
        room_info = room_data.readline()

        while line:
            line = f.readline()
        f.close()

        return room_info


class Living_Space(Room):

    """docstring for Living_Space."""
    def __init__(self):
        super(Living_Space, self).__init__()

    def allocate_living_room(self):

        """"
        Allocates a room at random by filtering out Living spaces
        that are available

        """

        living_space_list = []
        living_space_full = []
        living_space_index = None

        if len(Room.room_list) == 0:

            return 'There are no rooms in the system'

        else:

            # Searching the room list to find living rooms available
            for index, living_space in Room.room_list.items():

                if living_space['room_category'] == 'LIVING':

                    if living_space['room_category'] == \
                        'LIVING' and \
                            living_space['occupants'] < 4:

                        # Appending data for list with living spaces

                        living_space_list.append(living_space)

                    elif living_space['room_category'] ==\
                        'LIVING' and \
                            living_space['occupants'] == 4:

                        # Collect all the full rooms
                        living_space_full.append(living_space)

                    else:

                        return 'No Living spaces in the system'

            if len(living_space_list) == 0:

                return 'No Rooms Available'

            else:

                # Run an list index generator
                living_space_index = randint(0, len(living_space_list)-1)
                room_allocated = living_space_list[living_space_index]
                living_space['occupants'] += 1

        return living_space_list[living_space_index]['room_name']

    def reallocate_living_room(self, new_space, initial_room):
        """
        Reallocating the living area on request
        """
        living_rooms_available = []
        room_allocated = {}

        if len(Room.room_list) == 0:
            return 'There are no more availble rooms in the system'
        # Check for the room category
        for index, space in Room.room_list.items():

            # If the space in room check category
            if space['room_category'] == 'LIVING' \
                        and space['status'] == 'available':
                living_rooms_available.append(index)

        if new_space in living_rooms_available:

            # Populating to a list if the room is an office
            living_rooms_available[new_space]['occupants'] += 1
            Room.room_list[initial_room]['occupants'] -= 1

        return True


class Office(Room):

    """docstring for Office."""
    def __init__(self):
        super(Office, self).__init__()

    def allocate_office_space(self):

            """"

            Allocates a room at random by filtering out office spaces
            that are available

            """

            work_space_list = []
            work_space_full = []
            work_space_number = None

            # Populating list with office spaces

            if len(Room.room_list) == 0:

                return 'None'

            else:

                # Searching list to determine available rooms

                for index, work_space in Room.room_list.items():

                    if work_space['room_category'] == 'OFFICE':

                        # Creating a list of available offices
                        if work_space['room_category'] == \
                            'OFFICE' and \
                                Room.room_list[index]['occupants'] < 6:

                            # Appending data for list with work spaces to list

                            work_space_list.append(work_space)

                        elif work_space['room_category'] ==\
                            'OFFICE' and \
                                work_space['occupants'] == 6:

                            # Collect all the full rooms
                            work_space_full.append(index)

                        else:

                            return 'No Office spaces in the system'

                if len(work_space_list) == 0:

                    return 'No more rooms'

                else:

                    # Run a list index generator

                    work_space_number = randint(0, len(work_space_list)-1)
                    room_allocated = work_space_list[work_space_number]
                    work_space['occupants'] += 1

            return work_space_list[work_space_number]

    def reallocate_office_space(self, new_space, initial_room):

        """
        Reallocating the living area on request
        """
        office_space_available = []
        room_allocated = {}

        if len(Room.room_list) == 0:
            return 'There are no more availble rooms in the system'
        # Check for the room category
        for index, space in Room.room_list.items():

            # If the space in room check category
            if space['room_category'] == 'LIVING' \
                        and space['status'] == 'available':
                office_space_available.append(index)

        if new_space in office_space_available:

            # Reflecting reallocation details
            office_space_available[new_space]['occupants'] += 1
            Room.room_list[initial_room]['occupants'] -= 1

        return True
