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
            print("** class doesn't exist **")

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
            print(obj)
        except NameError:
            print("** class doesn't exist **")
            
    def do_destroy(self, args):
        '''function that destroy an instance'''
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
                raise NameError("Name not found")
            id = '{}.{}'.format(classes.__name__, arguments[1])

            if not storage.destroy(id):
                print("** no instance found **")
                return
            #  Successfull delete
        except NameError:
            print("** class doesn't exist **")
            
    def do_all(self, args):
        '''for print all string representation'''
        arguments = args.split()

        all_class = storage.all()
        list = []
        try:
            if len(arguments) == 0:
                for obj in all_class.values():
                    list.append(str(obj))
                print(list)
            else:
                classe = eval(arguments[0])
                
                for obj in all_class.values():
                    if isinstance(obj, classe):
                        list.append(str(obj))
                print(list)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, args):
        '''function that update'''
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return
        if len(arguments) == 1:
            print("** instance id missing **")
            return
        if len(arguments) == 2:
            print("** attribute name missing **")
            return
        if len(arguments) == 3:
            print("** value missing **")
            return
        try:
            classe = eval(arguments[0])
            if not classe.__init__:
                raise NameError("** class doesn't exist **")
            id = '{}.{}'.format(classe.__name__, arguments[1])
            obj = storage.get(id)
            
            if not obj:
                print("** no instance found **")
                return
            key = arguments[2]
            if key == "update_at" or key == "created_at" or key == "id":
                return
            
            obj.__setattr__(key, arguments[3])
            obj.save()

        except:
            print("** class doesn't exist **")

         
if __name__ == '__main__':
    HBNBCommand().cmdloop()
