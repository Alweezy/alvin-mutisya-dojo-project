"""
This is the dojo

Usage:
    dojo create_room (Living|Office) <room_name>...
    dojo add_person <first_name> <last_name> (Fellow|Staff) [<wants_space>]
    dojo print_allocations [--o=filename.txt]
    dojo print_unallocated [--o=filename.txt]
    dojo reallocate_person <employee_id> <new_room_name>
    dojo load_people <filename>
    dojo print_room <room_name>
    dojo save_state [--db=sqlite_database]
    dojo load_state <sqlite_database>
    dojo (-i | --interactive)

Options:
    -h,--help  :  Show this screen.
    -i,--interactive  :  Interactive Mode
    -v,--version  :  Version of the system
"""

import sys
import cmd
from os import path
from docopt import docopt, DocoptExit
from dojo import Dojo
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as exit:
            # An exception when the inputs differ from what is required

            print("You have entered an invalid command!")
            print(exit)
            return

        except SystemExit:
            # To enter help

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

dojo = Dojo()


class Interactive (cmd.Cmd):
    prompt = "(dojo)===>> "
    print(__doc__)

    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room (Living|Office) <room_name>..."""
        if args["Office"] is True:
            room_type = "office"
            for room_name in args["<room_name>"]:
                print(dojo.create_room(room_name, room_type))

        elif args["Living"] is True:
            room_type = "livingspace"
            for room_name in args["<room_name>"]:
                print(dojo.create_room(room_name, room_type))

    @docopt_cmd
    def do_add_person(self, args):
        """Usage: \
        add_person <first_name> <last_name> (Fellow|Staff) [<wants_space>]"""
        if args["Fellow"] and args["<first_name>"] and args["<last_name>"]:
            first_name = args["<first_name>"]
            last_name = args["<last_name>"]
            occupation = "Fellow"
            if args["<wants_space>"]:
                wants_space = args["<wants_space>"]
                print(dojo.add_person(first_name, last_name, occupation, wants_space))
            else:
                print(dojo.add_person(first_name, last_name, occupation))
        elif args["Staff"] and args["<first_name>"] and args["<last_name>"]:
            first_name = args["<first_name>"]
            last_name = args["<last_name>"]
            occupation = "Staff"
            print(dojo.add_person(first_name, last_name, occupation))

    def do_quit(self, arg):
        """Quits out of the interactive mode"""
        print('*********************BYE******************************')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt["--interactive"]:
    Interactive().cmdloop()

print(opt)