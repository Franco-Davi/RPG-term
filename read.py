import argparse

class Argument_Parser(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)

class Read():
    def __init__(self):
        ...

    parser = Argument_Parser(add_help=False)
    subparsers = parser.add_subparsers(dest="command")
    
    cmd_quit = subparsers.add_parser("quit")
    
    cmd_echo = subparsers.add_parser("echo")
    cmd_echo.add_argument("-m", "--message", nargs="+", type=str)
    
    cmd_screen = subparsers.add_parser("screen")
    cmd_screen.add_argument("select", type=str)