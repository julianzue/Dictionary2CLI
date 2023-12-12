from colorama import Fore, Style, init
import time
import os


# init colorama
init()


# colors
r = Fore.LIGHTRED_EX
c = Fore.LIGHTCYAN_EX
y = Fore.LIGHTYELLOW_EX
re = Fore.RESET


# styles
dim = Style.DIM
res = Style.RESET_ALL


def color(type, text_colored, text_normal):

    output = ""

    if text_colored == "":
        space = ""
    else:
        space = " "


    if type == "normal":
        output = c + "[*] " + text_colored + space + re + text_normal

    elif type == "input":
        output = y + "[+] " + text_colored + space + re + text_normal

    elif type == "error":
        output = r + "[!] " + text_colored + space + re + text_normal


    return output

 
class Dictionary():
    def __init__(self):
        self.prompt()

    
    def prompt(self):
        self.commands = [
            {
                "name": "add",
                "description": "Adds an entry.",
                "function": self.add
            },

            {
                "name": "list",
                "description": "Lists all dictionaries.",
                "function": self.list
            },

            {
                "name": "search",
                "description": "Search a word from a specific languare to a other.",
                "function": self.search
            },

            {
                "name": "help",
                "description": "Shows the commands and the description of them.",
                "function": self.help
            },

            {
                "name": "exit",
                "description": "Closes this program",
                "function": self.exit
            },

            {
                "name": "tl",
                "description": "Translates a word.",
                "function": self.translate
            }
        ]

        main = input(color("input", ">", ""))
        print("")

        isCommand = False

        for command in self.commands:
            if main == command["name"]:
                isCommand = True
                command["function"]()

        if not isCommand:
            print(color("error", "", "Command not found."))

        print("")
        self.prompt()


    def add(self):
        language_1 = input(color("input", "Lang 1:", ""))
        word_1 = input(color("input", "Word 1:", ""))

        language_2 = input(color("input", "Lang 2:", ""))
        word_2 = input(color("input", "Word 2:", ""))

        if not os.path.exists("dictionaries"):
            os.mkdir("dictionaries")
            print(color("normal", "", "Directory 'dictionaries' created."))


        with open("dictionaries/" + language_1.upper() + "-" + language_2.upper() + ".txt", mode="a", encoding="utf-8") as dict_file:
            dict_file.write(time.strftime("%Y-%m-%d %H:%M") + " | " + word_1 + " = " + word_2 + "\n")
        
        print(color("normal", "", "Successfully added."))
 
   
    def list(self):
        try:

            counter = 0
            dict_name_old = ""

            counter_dict = 0

            for dict in os.scandir("dictionaries"):
                with open("dictionaries/" + dict.name, mode="r", encoding="utf-8") as dict_read:
                    for line in dict_read.readlines():

                        if dict.name != dict_name_old and counter != 0:
                            print("")
                            counter_dict = 0

                        dict_name_old = dict.name

                        counter += 1
                        counter_dict += 1
                        print("{:02d}".format(counter) + " | " + "{:02d}".format(counter_dict) + " | " + dict.name.strip(".txt") + " | " + line.strip("\n").split(" | ")[1])

        except:
            print(color("error", "", "Directory not found. Please add an entry first."))


    def search(self):
        try:

            search_text = input(color("input", "Enter Word:", ""))
            counter = 0

            print("")

            for dict in os.scandir("dictionaries"):
                with open("dictionaries/" + dict.name, mode="r", encoding="utf-8") as dict_read:
                    for line in dict_read.readlines():
                        if search_text.upper() in line.strip("\n").upper():
                            counter += 1
                            print("{:02d}".format(counter) + " | " + dict.name.strip(".txt") + " | " + line.strip("\n"))

            if counter == 0:
                print(color("error", "", "No results found. Please try again."))

        except:
            print(color("error", "", "Directory not found. Please add an entry first."))


    def help(self):
        for command in self.commands:
            print(c + command["name"] + re + "\t" + command["description"])


    def exit(self):
        print(color("error", "", "Program closed."))
        exit()


    def translate(self):
        try:

            search_text = input(color("input", "Enter Word:", ""))
            counter = 0

            print("")

            for dict in os.scandir("dictionaries"):
                with open("dictionaries/" + dict.name, mode="r", encoding="utf-8") as dict_read:
                    for line in dict_read.readlines():
                        if search_text.upper() in line.strip("\n").upper():
                            counter += 1
                            
                            words = line.strip("\n").split(" | ")[1]
                            word = words.split(" = ")

                            lang = dict.name.strip(".txt").split("-")

                            if search_text.upper() in word[0].upper():
                                print(dim + lang[0] + ": " + res + word[0] + c + " -> " + re + dim + lang[1] + ": " + res + word[1])

                            elif search_text.upper() in word[1].upper():
                                print(dim + lang[1] + ": " + res + word[1] + c + " -> " + re + dim + lang[0] + ": " + res + word[0])

            if counter == 0:
                print(color("error", "", "No results found. Please try again."))

        except:
            print(color("error", "", "Directory not found. Please add an entry first."))


Dictionary()