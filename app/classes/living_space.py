from room import Room


class LivingSpace(Room):

    """docstring for LivingSpace."""

    def __init__(self, arg):
        super(LivingSpace, self).__init__()
        self.arg = arg

    def allocate_living_space(self):

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

            # Traversing the room list to find the living rooms available
            for living_space in Room.room_list:

                if Room.room_list[living_space]['room_category'] == 'LIVING':

                    # Creating a list of available Living Rooms

                    if Room.room_list[living_space]['room_category'] == \
                        'LIVING' and \
                            Room.room_list[living_space]['occupants'] < 4:

                        # Appending data for list with living spaces

                        living_space_list.append(living_space)

                    elif Room.room_list[living_space]['room_category'] ==\
                        'LIVING' and \
                            Room.room_list[living_space]['occupants'] == 4:

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
                Room.room_list[room_allocated]['occupants'] += 1

        return living_space_list[living_space_index]

    def reallocate_living_space(self,):

        offices_available = []
        room_allocated = {}

        # Check if there are availabble rooms in the system
        if len(Room.room_list) == 0:
            return 'There are no rooms in the system'

        else:
            # Check if the rooms are available for reallocatio
            for room_entry in Room.room_list:

                # Populate if the room is office

                if Room.room_list[room_entry]['status'] == 'available' \
                    and Room.room_list[room_entry]['room_category'] \
                        == 'OFFICE':

                    # Populate the available rooms in the list offices

                    offices_available.append(room_entry)

                elif Room.room_list[room_entry] == 'available' \
                    and Room.room_list[room_entry]['room_category'] \
                        == 'LIVING':

                    # Populating List of all realllocatable spaces
                    living_available.append(room_category)

                else:

                    return 'There are no rooms available for relocation'

        for allocate_new in Room.room_list:

            if Room.room_list[allocate_new]['room_category'] == 'OFFICE':

                # Randomly reallocate office space to the person

                reallocate_space_index = randint(0, len(offices_available)-1)
                room_allocated['name'] =\
                    offices_available[reallocate_space_index]
                room_allocated['category'] = 'OFFICE'
                Room.room_list[allocate_new]['occupants'] += 1

                return room_allocated

            if Room.room_list[allocate_new]['room_category'] == 'LIVING':

                # Randomly reallocate living space to fellow

                reallocate_space_index = randint(0, len(living_available)-1)
                room_allocated['name'] = \
                    living_available[reallocate_space_index]
                room_allocated['category'] = 'LIVING'
                Room.room_list[allocate_new]['occupants'] += 1

                return room_allocated

            else:

                # If the system does not contain the required room name

                return 'Room not in the system'

    def print_living_space(arg):
        pass
