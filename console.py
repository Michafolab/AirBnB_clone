#!/usr/bin/env python3
"""
The console module. This module contains all
the files needed to run our console
for managing the state of our application
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    The HBNB class to control the console needed for
    our application
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        command to exit the console
        """
        return True;

    def do_EOF(self, line):
        """
        close the console when EOF is encountered
        """
        return True

    def emptyline(self):
        """
        do nothing when nothing is entered as a comand
        """
        pass

    def do_create(self, line):
        """
        creates a new instance of a class given
        as an argument
        """
        if not line:
            print("** class name missing **")
        elif line not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            # ----- create a new instance of the class -----
            # ----- stated and save to a file -----
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id given to the command as
        argument
        """
        line = tuple(line.split())
        try:
            classname = line[0]
            if classname not in ["BaseModel"]:
                print("** class doesn't exist **")
                return
        except IndexError:
            print("** class name missing **")
            return
        try:
            instance_id = line[1]
        except IndexError:
            print("** instance id missing **")
            return
        full_search_t = f"{classname}.{instance_id}"
        storage.reload()
        inst_object = storage.all()
        try:
            print(inst_object[full_search_t])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        deletes an instance based on the class name and id
        and saved the change into the JSON file
        """
        line = tuple(line.split())
        try:
            classname = line[0]
            if classname not in ["BaseModel"]:
                print("** class doesn't exist **")
                return
        except IndexError:
            print("** class name missing **")
            return
        try:
            instance_id = line[1]
        except IndexError:
            print("** instance id missing **")
            return
        full_search_t = f"{classname}.{instance_id}"
        storage.reload()
        inst_object = storage.all()
        try:
            del inst_object[full_search_t]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """
            Prints all the string representation of all instances
            Can be based on the class name if the class name is given,
            Otherwise just print all
        """
        if line and line not in ["BaseModel"]:
            print("class doesn't exist")
            return
        storage.reload()
        inst_object = storage.all()
        to_print = []
        if line:
            # ----- if the class name exist print it's instances -----
            for value in inst_object.values():
                if value.__class__.__name__ == line:
                    to_print.append(str(value))
        else:
            for value in inst_object.values():
                to_print.append(str(value))
        if to_print:
            print(to_print)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
