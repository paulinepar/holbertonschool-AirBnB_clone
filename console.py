#!/usr/bin/python3
""" Doc """
from models.base_model import BaseModel
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """ contains the entry point of the command interpreter """
    prompt = '(hbnb) '

    def help_quit(self):
        '''quit programm'''
        print("Quit command to exit the program", end="\n\n")

    def help_EOF(self):
        return True
    
    def do_EOF(self, line):
        '''quit programm "ctrl D'''
        return True

    def do_quit(self, line):
        '''quit command to quit programm'''
        return True

    def emptyline(self):
        '''for empty line'''
        pass

    def do_create(self, args):
        '''create the new instance of class in file JSON'''
        if args == "":
            print("** class name missing **")
            return
        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **", new_instance)

    def do_show(cls, args):
        '''for print instance class'''
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return
        if len(arguments) == 1:
            print("** instance id missing **")
            return
        try:
            classes = eval(arguments[0])
            if not classes.__init__:
                raise NameError("** class not found **")
            id = '{}.{}'.format(classes.__name__, arguments[1])
            obj = storage.get(id)
            if obj is None:
                print("** no instance found **")
                return
        except NameError:
            print("** class doesn't exist **")
            
    def do_destroy(self, args):
        arguments = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(arguments) == 1:
            print("** class doesn't exist **")
        try:
            classes = eval(arguments[0])
            if not classes.__init__:
                raise NameError("Name not found")
            id = '{}.{}'.format(classes.__name__, arguments[1])
            obj = storage.get(id)
        except NameError:
            if obj is None:
                print("** instance id missing **")

    def do_all(self, args):
        arguments = args.split()
        all_class = storage.all()
        list = []
        try:
            for obj in all_class.values():
                list.append(obj)
                print(obj)
        except NameError:
            if arguments not in obj:
                print("** class doesn't exist **")

    def do_update(self, args):
         



if __name__ == '__main__':
    HBNBCommand().cmdloop()
