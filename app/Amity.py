#!/usr/bin/env python
"""
Usage:
    amity create_room <category> <room_name>...
    amity add_person <f_name> <s_sname> <person_job> <employee_number> [<wants_accomodation>]
    amity reallocate_person <person_identifier> <room_name>
    amity load_people
    amity print_allocations
    amity print_unallocated
    amity print_room <room_name>
    amity save_state[ -db =sqlite_database]
    amity load_state <sqlite_database>
    amity (-o | --filename)
    amity (-i | --interactive)
    amity (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
        --export
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from classes.person import Person
from classes.room import Room
from random import randint
# From inventory import Item_console


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive(cmd.Cmd):
    intro = 'Welcome to Amity'
    prompt = 'Tell_Amity_To>> '
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """
        Usage: create_room <category> <room_name>...
        """
        room_names = args["<room_name>"]
        category = args["<category>"]
        add_obj = Room()

        #print "this is to show that this function has a heart"

        if category.upper() != 'LIVING' and category.upper() != 'OFFICE':

            print category + ' Is not a valid Room type, \
                    try again with office or living'

        else:

            add_obj.create_Rooms(room_names, category.upper())

    @docopt_cmd
    def do_add_person(self, args):
        """
        Usage: add_person <f_name> <s_name> <person_job> <employee_number> [<wants_accomodation>]
        """
        s_name =args["<s_name>"]
        employee_number = None
        f_name = args["<f_name>"]
        person_job = args["<person_job>"]
        wants_accomodation = args["<wants_accomodation>"] or "N"
        employee_number =args["<employee_number>"]

        # Create Employee number using number generator and stringbuilder
        # number =randint(0,1000)
        #
        # if person_job.upper()=="FELLOW":
        #
        #     employee_number = 'F%d' %(number)
        #
        # elif person_job.upper() == "STAFF":
        #     employee_number = 'S%d' %(number)

        add_obj = Person()


        print add_obj.add_person(f_name,s_name,person_job,employee_number,wants_accomodation.upper())


    @docopt_cmd
    def do_reallocate_person(self, args):
        """
        Usage: reallocate_person <person_identifier> <room_name>
        """
        emp_no = args["<person_identifier>"]
        room_name = args["<room_name>"]
        real_obj = Person()

        print real_obj.reallocate_person(emp_no,room_name)


    @docopt_cmd
    def do_load_people(self, args):
        """
        Usage: load_people
        """
        #item_id = args["<itemid>"]
        obj_person = Person()
        obj_person.load_people()

    @docopt_cmd
    def do_print_allocations(self, args):
        """
        Usage: print_allocations
        """
        person_obj = Person()
        person_obj.print_allocations()

    @docopt_cmd
    def do_print_unallocated(self, args):
        """
        Usage: print_unallocated
        """
        #item_id = args["<itemid>"]
        person_obj= Person()
        print(person_obj.print_unallocated())

    @docopt_cmd
    def do_print_room(self, args):
        """
        Usage: print_room <room_name>
        """
        room_name=args["<room_name>"]
        person_obj= Person()
        person_obj.print_room(room_name)

    @docopt_cmd
    def do_save_state(self, args):
        """
        Usage: compute_assetvalue
        """
        add_obj = Item_console()
        print(add_obj.compute_value())

    @docopt_cmd
    def do_load_state(self,args):
        """
        Usage: export
        """
        add_obj = Item_console()
        add_obj.export_data()



opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    print(__doc__)
    MyInteractive().cmdloop()
