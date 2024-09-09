import argparse

class Argument_Parser(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)

class Read():
    def __init__(self):
        ...

    parser = Argument_Parser(add_help=False)
    subparsers = parser.add_subparsers(dest="command")
    
    cmd_help = subparsers.add_parser("help")
    cmd_help.add_argument("cmd", nargs="?", type=str, default="help")

    cmd_quit = subparsers.add_parser("quit")
    
    cmd_echo = subparsers.add_parser("echo")
    cmd_echo.add_argument("-m", "--message", nargs="+", type=str)
    
    cmd_screen = subparsers.add_parser("screen")
    cmd_screen.add_argument("select", type=str)

    cmd_save = subparsers.add_parser("save")
    cmd_save.add_argument("file", nargs="?", type=int, default=0)

    cmd_load = subparsers.add_parser("load")
    cmd_load.add_argument("file", nargs="?", type=int, default=0)