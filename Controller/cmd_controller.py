"""
This is a cmd demo
"""

from controller import start
from cmd import Cmd


class Quitter(Cmd):
    """
    single command processor example
    """
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "

    def do_run_interpreter(self, line):
        """
        Runs UML to Class template programme
        run_interpreter alias is run_i
        :return: None
        """
        start()

    def do_exit(self, line):
        """
        Exit from CMD
        exit alias is e
        :return: True
        """
        print("Exiting ......")
        return True

    do_e = do_exit
    do_run_i = do_run_interpreter


if __name__ == "__main__":
    quitter = Quitter()
    quitter.cmdloop()
