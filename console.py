#!/usr/bin/python3
""" Doc """

import cmd


class HBNBCommand(cmd.Cmd):
    """ contains the entry point of the command interpreter """
    prompt = '(hbnb) '

    def help_quit(self):
        print("Quit command to exit the program", end="\n\n")

    def help_EOF(self):
        print("syntax: EOF")

    def do_EOF(self, line):
        print()
        return True

    def do_quit(self, line):
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
