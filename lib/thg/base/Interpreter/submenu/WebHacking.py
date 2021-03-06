from lib.thg.base.Interpreter.thgcmd import Cmd
from colorama import Fore


def help_say():
    print("This is a SecondLevel menu. Options are qwe, asd, zxc")


class WebHackingLevel(Cmd):
    colors = "Always"
    console_prompt = "{COLOR_START}WebHacking{COLOR_END}".format(
        COLOR_START=Fore.BLUE, COLOR_END=Fore.RESET
    )
    doc_header = " WebHacking COMMAND HELP"
    doc_leader = ""
    intro = None
    lastcmd = ""
    misc_header = "Miscellaneous help topics:"
    nohelp = "*** No help on %s"
    ruler = "="
    undoc_header = "Undocumented commands:"
    console_prompt_end = ">"
    module_name = None
    module_class = None
    module_instance = None
    __Menu__version__ = 1.0
    """To be used as a Crypto level command class. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.top_level_attr = None
        self.second_level_attr = 987654321
        self.prompt = self.console_prompt + self.console_prompt_end

    def thg_sayd(self, line):
        print(
            "You called a command in SecondLevel with '%s'. "
            "It has access to top_level_attr: %s" % (line, self.top_level_attr)
        )

    def complete_sayd(self, text, line, begidx, endidx):
        return [s for s in ["qwe", "asd", "zxc"] if s.startswith(text)]
