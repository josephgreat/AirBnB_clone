#!/usr/bin/env python3
import cmd


class HBNBShell(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        'Exit from console'
        exit()

    def do_EOF(self, arg):
        'Check when a file or line has ended'
        print('')
        exit()


if __name__ == '__main__':
    HBNBShell().cmdloop()
