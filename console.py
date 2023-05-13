#!/usr/bin/python3
"""Console Module
This module controls all databases.
Can create, modify and delete instances.
"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from shlex import split
import re
import json


class HBNBCommand(cmd.Cmd):
    """Type class HBNBCommand CLI"""
    prompt = '(hbnb) '
    __classes = {
        'BaseModel',
        'Amenity',
        'Place',
        'User',
        'State',
        'Review',
        'City'
    }

    def emptyline(self):
        """
        When an empty line is entered in response to the prompt,
        it won't repeat the last nonempty command entered.

        """
        pass

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Quit command to exit the program
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
