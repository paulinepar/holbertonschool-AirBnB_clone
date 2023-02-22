#!/usr/bin/python3
""" Doc """

import cmd


class HBNBCommand(cmd.Cmd):
    """ contains the entry point of the command interpreter """
    prompt = '(hbnb) '

    def help_quit(self):
        print("Quit command to exit the program", end="\n\n")

    def help_EOF(self):
        return True

    def do_EOF(self, line):
        """ End of File with Ctrl ^D"""
        return True

    def do_quit(self, line):
        """ Quit the program in writing quit"""
        return True

    def emptyline(self):
        """ an empty line + ENTER shouldnt execute anything """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
