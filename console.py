#!/usr/bin/env python3
"""
The console module. This module contains all
the files needed to run our console
for managing the state of our application
"""
import cmd
import shlex
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
        Usage:
            (hbnb) quit
        """
        return True;

    def do_EOF(self, line):
        """
        close the console when EOF is encountered
        EOF: End-Of-File
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
        Usage:
            (hbnb) create <class name>
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
        Usage:
            (hbnb) show <class name> <instance id>
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
        Usage:
            (hbnb) destroy <class name> <instance id>
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
            Usage:
                (hbnb) all
                    It will list all instances
                (hbnb) all <class name>
                    It will list instances belonging to the specified
                    class name
        """
        if line and line not in ["BaseModel"]:

            print("** class doesn't exist **")
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

    def do_update(self, line):
        """
        Updates an instance based on the class name given
        and the attribute-value pair given as argument
        Usage:
            update <class name> <id> <attribute name> \"<attribute value>\"
        """
        errors = {0: "** class name missing **",
                  1: "** instance id missing **",
                  2: "** attribute name missing **",
                  3: "** value missing **"}

        arg_idx = ["class_name", "instance_id", "attr_name",
                     "attr_value"]

        arguments = {"class_name": "", "instance_id": "",
                     "attr_name": "", "attr_value": ""}

        models = ["BaseModel"]
        line = shlex.split(line)

        # ----- check if all neccesary arguments are given -----
        for i in range(4):

            try:

                arguments[arg_idx[i]] = line[i]
                # ----- checks if the class name given is valid -----
                if i == 0 and arguments[arg_idx[0]] not in models:

                    print("** class doesn't exist **")
                    return

                # ----- checks if the inst id given is valid -----
                if i == 1:

                    class_name = arguments[arg_idx[0]]
                    instance_id = arguments[arg_idx[1]]
                    if not check_instance_id(class_name, instance_id):
                        return

            except IndexError:
                print(errors[i])
                return
        full_search_t = f"{class_name}.{instance_id}"
        storage.reload()
        inst_object = storage.all()
        to_update = inst_object[full_search_t]
        attr_name = arguments["attr_name"]
        attr_value = arguments["attr_value"]
        # ----- set the attribute and save it to the storage engine -----

        try:
            attr_value = type(getattr(to_update, attr_name))(attr_value)

        except AttributeError:
            attr_value = str(attr_value)

        setattr(to_update, arguments["attr_name"], attr_value)
        storage.save()


def check_instance_id(class_name, instance_id):
    full_search_t = f"{class_name}.{instance_id}"
    storage.reload()
    inst_object = storage.all()
    # ----- check if the id arg given is valid -----
    try:

        inst_object[full_search_t]
        return True

    except KeyError:

        print("** no instance found **")
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
