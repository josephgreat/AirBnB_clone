#!/usr/bin/env python3
import cmd, sys

class HBNBShell(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        'Exit from console'
        exit()

    def do_EOF(self, arg):
        'Check when a file or line has ended'
        for line in sys.stdin:
            if line:
                pass
            else:
                raise EOFError()

if __name__ == '__main__':
    HBNBShell().cmdloop()
