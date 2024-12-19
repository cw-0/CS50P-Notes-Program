import threading
import cursor
import pyfiglet
import time
import os
import sys
import subprocess
import stat
import random
import win32gui, win32con
from colorama import init, Fore

init(autoreset=True)  # Colorama Reset Colors


class Pages:
    def __init__(self):
        self.week_select = None

    def intro(self):
        intro_title = fig_GREEN + pyfiglet.figlet_format("CS50 Python\n".center(50))
        intro_subtitle = f"{RED}--- Coding Cain ---{RESET}\n".center(110)
        print(intro_title)
        print(intro_subtitle)
        print("\n" * 3)
        input(f"Press {GREEN}Enter{RESET} to continue".center(108))
        clear_console()

    def home(self):
        home_title = fig_YELLOW + pyfiglet.figlet_format("Home".center(55))
        home_subtitle = f"{YELLOW}What Notes Would You Like To View?{RESET}".center(90)
        clear_console()
        print(home_title, end="")
        print("\n", home_subtitle)
        print(
            f"""
{YELLOW}0. Basics of Python and Terminal{RESET}\n
{YELLOW}1. Conditionals{RESET}\n
{YELLOW}2. Match and Loops / Basic Lists and Dicts{RESET}\n
{YELLOW}3. Exceptions / Try-Except{RESET}\n
{YELLOW}4. Libraries{RESET}\n
{YELLOW}5. Unit Tests - Pytest{RESET}\n
{YELLOW}6. File I/O{RESET}\n
{YELLOW}7. Regular Expressions (Regex){RESET}\n
{YELLOW}8. Object Orientated Programming{RESET}\n
{YELLOW}9. Et Cetera (Sets, Global, Argparse, Map, Unpacking, Line/Dict Comprehension, Filter, Enumerate){RESET}\n
\n
. Exit
- Fix Files
\n\n
              """
        )
        self.week_select = input("> ").strip().lower()

    def change_page(self):
        while True:
            if self.week_select in ["0", "0.", "basics", "basics of python"]:
                self.page_basics()
            elif self.week_select in ["1", "1.", "conditionals"]:
                self.page_conditionals()
            elif self.week_select in [
                "2",
                "2.",
                "match",
                "loops",
                "match and loops",
                "match and loops / basic lists and dicts",
            ]:
                self.page_loops()
            elif self.week_select in [
                "3",
                "3.",
                "exceptions",
                "try-except",
                "exceptions / try-except",
            ]:
                self.page_exceptions()
            elif self.week_select in ["4", "4.", "libraries"]:
                self.page_libraries()
            elif self.week_select in [
                "5",
                "5.",
                "unit test",
                "unit tests",
                "pytest",
                "unit tests - pytest",
            ]:
                self.page_tests()
            elif self.week_select in ["6", "6.", "file", "file io", "file i/o", "io"]:
                self.page_IO()
            elif self.week_select in [
                "7",
                "7.",
                "regex",
                "regular expressions",
                "regular expression",
                "regular expressions (regex)",
            ]:
                self.page_regex()
            elif self.week_select in [
                "8",
                "8.",
                "oop",
                "object orientated programming",
            ]:
                self.page_oop()
            elif self.week_select in [
                "9",
                "9.",
                "et cetera",
                "sets",
                "global",
                "argparse",
                "map",
                "unpacking",
                "line/dict comprehension",
                "line comprehension",
                "dict comprehension",
                "comprehension",
                "filter",
                "enumerate",
            ]:
                self.page_cetera()
            elif self.week_select in ["exit", "."]:
                clear_console()
                print(f"{RED}Closing...{RESET}")
                time.sleep(0.5)
                cursor.show()
                sys.exit()
            
            elif self.week_select in ["fix", "files", "fix files", "fix file", "- fix files"]:
                clear_console()
                fix_title = fig_YELLOW + pyfiglet.figlet_format("Fix Files")
                print(fix_title, end="")
                fix_files()
                print(f"\n{GREEN}Files Fixed{RESET}")
                input(f"Press {GREEN}Enter{RESET} to continue")
                self.home()

            else:
                print(f"\n{RED}invalid selection{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
                self.home()

    # ---- BASICS PAGE ----

    def page_basics(self):
        basics_title = fig_CYAN + pyfiglet.figlet_format(
            "Basics of Python and Terminal"
        )
        basics_subtitle = f"{CYAN}What Would You Like To View?{RESET}".center(75)
        clear_console()
        print(basics_title, end="")
        print("\n", basics_subtitle)
        print(
            f"""
{CYAN}1. Written Notes{RESET}\n
{CYAN}2. Example Programs{RESET}\n
{CYAN}3. Assignments{RESET}\n
. Back
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "written notes"]:
            self.basics_notes()
        elif self.week_select in ["2", "2.", "example programs", "programs"]:
            self.basics_programs()
        elif self.week_select in ["3", "3.", "assignment", "assignments"]:
            self.basics_assignments()
        elif self.week_select in [".", "back"]:
            self.home()
        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.page_basics()

    def basics_notes(self):
        clear_console()
        basics_title = fig_GREEN + pyfiglet.figlet_format(
            "Basics of Python and Terminal"
        )
        basics_pdf = rf"{assets_path}\PDFs\Week 0 - Basics of Python.pdf"
        print(basics_title)
        try:
            os.startfile(basics_pdf)
            print(f"{GREEN}PDF Week 0 - Basics of Python and Terminal now OPEN{RESET}")
        except Exception:
            print(
                f"{RED}PDF Week 0 - Basics of Python and Terminal FAILED TO OPEN{RESET}"
            )
        input(f"\nPress {GREEN}Enter{RESET} to continue")
        self.page_basics()

    def basics_programs(self):
        # Programs
        squaring_calc = rf"{assets_path}\Week 0 Basics of Python and Terminal\Calculator\calculator.py"
        root_calc = rf"{assets_path}\Week 0 Basics of Python and Terminal\Square Root Calculator\square_root.py"
        first_hour = rf"{assets_path}\Week 0 Basics of Python and Terminal\first_hour.py"

        # Headers
        basics_title = fig_RED + pyfiglet.figlet_format("Basics of Python and Terminal")
        basics_subtitle = f"{RED}What Program Would You Like To Open?{RESET}".center(75)

        clear_console()
        print(basics_title, end="")
        print("\n", basics_subtitle)
        print(
            f"""
{RED}1. Squaring Calculator{RESET}\n
{RED}2. Square Root Calculator{RESET}\n
{RED}3. First Program{RESET}\n
. Back\n
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "squaring calculator", "squaring"]:
            try:
                openpy(squaring_calc)
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.basics_programs()

        elif self.week_select in ["2", "2.", "square root", "square root calculator"]:
            try:
                openpy(root_calc)
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.basics_programs()

        elif self.week_select in ["3", "3.", "first", "program","first program"]:
            try:
                openpy(first_hour)
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.basics_programs()

        elif self.week_select in [".", "back"]:
            self.page_basics()

        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.basics_programs()

    def basics_assignments(self):
        # Assignments
        indoor = rf"{assets_path}\Week 0 Basics of Python and Terminal\Assignments\Indoor Voice\indoor.py"
        playback = rf"{assets_path}\Week 0 Basics of Python and Terminal\Assignments\Playback\playback.py"
        faces = rf"{assets_path}\Week 0 Basics of Python and Terminal\Assignments\Faces\faces.py"
        einstein = rf"{assets_path}\Week 0 Basics of Python and Terminal\Assignments\Einstein\einstein.py"
        tip = rf"{assets_path}\Week 0 Basics of Python and Terminal\Assignments\Tip Calculator\tip.py"

        # Headers
        basics_title = fig_LIGHT_PURPLE + pyfiglet.figlet_format(
            "Basics of Python and Terminal"
        )
        basics_subtitle = (
            f"{LIGHT_PURPLE}What Assignment Would You Like To Open?{RESET}".center(75)
        )

        clear_console()
        print(basics_title, end="")
        print("\n", basics_subtitle)
        print(
            f"""

{LIGHT_PURPLE}1. Indoor Voice{RESET}\n
{LIGHT_PURPLE}2. Playback Speed{RESET}\n
{LIGHT_PURPLE}3. Making Faces{RESET}\n
{LIGHT_PURPLE}4. Einstein{RESET}\n
{LIGHT_PURPLE}5. Tip Calculator{RESET}\n
.Back\n
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "indoor", "voice", "indoor voice"]:
            try:
                openpy(indoor)
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.basics_assignments()

        elif self.week_select in ["2", "2.", "playback", "speed", "playback speed"]:
            try:
                openpy(playback)
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.basics_assignments()

        elif self.week_select in ["3", "3.", "making", "faces", "making faces"]:
            try:
                openpy(faces)
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.basics_assignments()

        elif self.week_select in ["4", "4.", "einstein"]:
            try:
                openpy(einstein)
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.basics_assignments()

        elif self.week_select in ["5", "5.", "tip", "calculator", "tip calculator"]:
            try:
                openpy(tip)
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.basics_assignments()
        
        elif self.week_select in [".", "back"]:
            self.page_basics()

        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.basics_assignments()

    # ---- CONDITIONALS PAGE ----

    def page_conditionals(self):
        conditionals_title = fig_CYAN + pyfiglet.figlet_format("Python Conditionals")
        conditionals_subtitle = f"{CYAN}What Would You Like To View?{RESET}".center(75)
        clear_console()
        print(conditionals_title, end="")
        print("\n", conditionals_subtitle)
        print(
            f"""
{CYAN}1. Written Notes{RESET}\n
{CYAN}2. Example Programs{RESET}\n
{CYAN}3. Assignments{RESET}\n
. Back
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "written notes"]:
            self.conditionals_notes()
        elif self.week_select in ["2", "2.", "example programs", "programs"]:
            self.conditionals_programs()
        elif self.week_select in ["3", "3.", "assignment", "assignments"]:
            self.conditionals_assignments()
        elif self.week_select in [".", "back"]:
            self.home()
        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.page_conditionals()

    def conditionals_notes(self):
        clear_console()
        conditionals_title = fig_GREEN + pyfiglet.figlet_format("Python Conditionals")
        conditionals_pdf = rf"{assets_path}\PDFs\Week 1 - Conditionals.pdf"
        print(conditionals_title)
        try:
            os.startfile(conditionals_pdf)
            print(f"{GREEN}PDF Week 1 - Python Conditionals OPEN{RESET}")
        except Exception:
            print(f"{RED}PDF Week 1 - Python Conditionals FAILED TO OPEN{RESET}")
        input(f"\nPress {GREEN}Enter{RESET} to continue")
        self.page_conditionals()

    def conditionals_programs(self):
        # Programs
        books = rf"{assets_path}\Week 1 Conditionals\books.py"
        compare = rf"{assets_path}\Week 1 Conditionals\greater_or_less.py"
        grades = rf"{assets_path}\Week 1 Conditionals\grades.py"
        parity = rf"{assets_path}\Week 1 Conditionals\parity.py"


        conditionals_title = fig_RED + pyfiglet.figlet_format("Python Conditionals")
        conditionals_subtitle = f"{RED}What Program Would You Like To Open?{RESET}".center(75)

        clear_console()
        print(conditionals_title, end="")
        print("\n", conditionals_subtitle)
        print(
            f"""

{RED}1. Books{RESET}\n
{RED}2. Greater or Less Than{RESET}\n
{RED}3. Grades{RESET}\n
{RED}4. Modulo and Parity{RESET}\n
. Back\n
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "book", "books"]:
            try:
                openpy(books)
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.conditionals_programs()

        elif self.week_select in ["2", "2.", "greater", "less", "less than", "greater or less than"]:
            try:
                openpy(compare)
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.conditionals_programs()

        elif self.week_select in ["3", "3.", "grades", "grade"]:
            try:
                openpy(grades)
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.conditionals_programs()

        elif self.week_select in ["4", "4.", "modulo", "parity", "modulo and parity"]:
            try:
                openpy(parity)
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.conditionals_programs()

        elif self.week_select in [".", "back"]:
            self.page_conditionals()

        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.conditionals_programs()

    def conditionals_assignments(self):
        # Assignments
        bank = rf"{assets_path}\Week 1 Conditionals\Assignments\Bank\bank.py"
        test_bank = rf"{assets_path}\Week 1 Conditionals\Assignments\Bank\test_bank.py"
        deep = rf"{assets_path}\Week 1 Conditionals\Assignments\Deep Thought\deep.py"
        extension = rf"{assets_path}\Week 1 Conditionals\Assignments\File Extensions\extensions.py"
        interpreter = rf"{assets_path}\Week 1 Conditionals\Assignments\Math Interpreter\interpreter.py"
        meal = rf"{assets_path}\Week 1 Conditionals\Assignments\Meal Time\meal.py"

        # Headers
        conditionals_title = fig_LIGHT_PURPLE + pyfiglet.figlet_format(
            "Python Conditionals"
        )
        conditionals_subtitle = (
            f"{LIGHT_PURPLE}What Assignments Would You Like To Open?{RESET}".center(75)
        )

        clear_console()
        print(conditionals_title, end="")
        print("\n", conditionals_subtitle)
        print(
            f"""
{LIGHT_PURPLE}1. Bank{RESET}\n
{LIGHT_PURPLE}2. Deep Thought{RESET}\n
{LIGHT_PURPLE}3. File Extensions{RESET}\n
{LIGHT_PURPLE}4. Math Interpreter{RESET}\n
{LIGHT_PURPLE}5. Meal Time{RESET}\n
. Back\n
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "bank"]:
            try:
                openpyfiles(bank, test_bank)
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.conditionals_assignments()

        elif self.week_select in ["2", "2.", "deep", "thought", "deep thought"]:
            try:
                openpy(deep)
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.conditionals_assignments()

        elif self.week_select in ["3", "3.", "file extensions", "file", "extensions"]:
            try:
                openpy(extension)
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.conditionals_assignments()

        elif self.week_select in ["4", "4.", "math", "interpreter", "math interpreter"]:
            try:
                openpy(interpreter)
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.conditionals_assignments()

        elif self.week_select in ["5", "5.", "meal", "time", "meal time"]:
            try:
                openpy(meal)
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.conditionals_assignments()

        elif self.week_select in [".", "back"]:
            self.page_conditionals()

        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.conditionals_assignments()

    # ---- LOOPS PAGE ----

    def page_loops(self):
        loops_title = fig_CYAN + pyfiglet.figlet_format(
            "Python Match and Loops"
        )  # Change Title
        loops_subtitle = f"{CYAN}What Would You Like To View?{RESET}".center(75)
        clear_console()
        print(loops_title, end="")
        print("\n", loops_subtitle)
        print(
            f"""
{CYAN}1. Written Notes{RESET}\n
{CYAN}2. Example Programs{RESET}\n
{CYAN}3. Assignments{RESET}\n
. Back
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "written notes"]:
            self.loops_notes()  # Change page
        elif self.week_select in ["2", "2.", "example programs", "programs"]:
            self.loops_programs()  # Change page
        elif self.week_select in ["3", "3.", "assignment", "assignments"]:
            self.loops_assignments()  # Change page
        elif self.week_select in [".", "back"]:
            self.home()
        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.page_loops()  # Change page

    def loops_notes(self):  # change name
        clear_console()
        loops_title = fig_GREEN + pyfiglet.figlet_format(
            "Python Match and Loops"
        )  # Change Title
        loops_pdf = rf"{assets_path}\PDFs\Week 2 - Match and Loops.pdf"  # Change pdf and name
        print(loops_title)
        try:
            os.startfile(loops_pdf)  # change argument name
            print(
                f"{GREEN}PDF Week 2 - Python Match and Loops OPEN{RESET}"
            )  # Change naming
        except Exception:
            print(
                f"{RED}PDF Week 2 - Python Match and Loops FAILED TO OPEN{RESET}"
            )  # change naming
        input(f"\nPress {GREEN}Enter{RESET} to continue")
        self.page_loops()  # change name

    def loops_programs(self):  # change name
        # Programs
        i_in_range = rf"{assets_path}\Week 2 Loops\For i in range\mario.py"  # change path
        spam_range = rf"{assets_path}\Week 2 Loops\Spam (range)\spam.py"  # change path
        dictionary = rf"{assets_path}\Week 2 Loops\dict.py"
        big_dict = rf"{assets_path}\Week 2 Loops\big_dict.py"
        for_loop = rf"{assets_path}\Week 2 Loops\forloops.py"
        login = rf"{assets_path}\Week 2 Loops\login.py"
        loop_list = rf"{assets_path}\Week 2 Loops\looplist.py"
        matches = rf"{assets_path}\Week 2 Loops\matchloop.py"
        advanced_range = rf"{assets_path}\Week 2 Loops\advanced_range.py"
        real_estate = rf"{assets_path}\Week 2 Loops\real_estate.py"
        win_tracker = rf"{assets_path}\Week 2 Loops\win_tracker.py"


        # Headers
        loops_title = fig_RED + pyfiglet.figlet_format(
            "Python Match and Loops"
        )  # Change Title
        loops_subtitle = f"{RED}What Program Would You Like To Open?{RESET}".center(75)

        clear_console()
        print(loops_title, end="")
        print("\n", loops_subtitle)
        print(
            f"""   
{RED}1. i in range{RESET}\n
{RED}2. spam using range{RESET}\n
{RED}3. Dictionary{RESET}\n
{RED}4. Big Dictionary{RESET}\n
{RED}5. For Loops{RESET}\n
{RED}6. Login Loop{RESET}\n
{RED}7. Loop Over Lists{RESET}\n
{RED}8. Case Match{RESET}\n
{RED}9. Advanced Range{RESET}\n
{RED}10. Real Estate App{RESET}\n
{RED}11. Win Tracker App{RESET}\n
. Back\n
\n\n
            """
        )  # Change Menu Choices
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "i", "i in range"]:  # change
            try:
                openpy(i_in_range)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.loops_programs()  # change name

        elif self.week_select in ["2", "2.", "spam", "spam using range"]:  # change
            try:
                openpy(spam_range)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.loops_programs()  # change name

        elif self.week_select in ["3", "3.", "dictionary"]:  # change
            try:
                openpy(dictionary)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.loops_programs()  # change name

        elif self.week_select in ["4", "4.", "dictionary", "big dictionary"]:  # change
            try:
                openpy(big_dict)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.loops_programs()  # change name

        elif self.week_select in ["5", "5.", "for loop", "for loops"]:  # change
            try:
                openpy(for_loop)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.loops_programs()  # change name

        elif self.week_select in ["6", "6.", "login", "login loops"]:  # change
            try:
                openpy(login)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.loops_programs()  # change name

        elif self.week_select in ["7", "7.", "loop list", "loop lists", "loop over lists", "loop over list", "list", "lists"]:  # change
            try:
                openpy(loop_list)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.loops_programs()  # change name

        elif self.week_select in ["8", "8.", "case", "case match", "match"]:  # change
            try:
                openpy(matches)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.loops_programs()  # change name

        elif self.week_select in ["9", "9.", "advanced range", "advanced"]:  # change
            try:
                openpy(advanced_range)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.loops_programs()  # change name

        elif self.week_select in ["10", "10.", "real estate app", "real estate", "real", "estate"]:  # change
            try:
                openpy(real_estate)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.loops_programs()  # change name

        elif self.week_select in ["11", "11.", "win tracker app", "win tracker", "win", "tracker"]:  # change
            try:
                openpy(win_tracker)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.loops_programs()  # change name

        elif self.week_select in [".", "back"]:  # change if needed
            self.page_loops()  # change name

        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.loops_programs()  # change name

    def loops_assignments(self):  # change name
        # ASSIGNMENTS
        plates = rf"{assets_path}\Week 2 Loops\Assignments\Plates (Functions)\plates.py"  # change
        twitter = rf"{assets_path}\Week 2 Loops\Assignments\Twttr\twttr.py"  # change
        camel = rf"{assets_path}\Week 2 Loops\Assignments\Camel\camel.py"
        coke = rf"{assets_path}\Week 2 Loops\Assignments\Coke\coke.py"
        nutrition = rf"{assets_path}\Week 2 Loops\Assignments\Nutrition\nutrition.py"


        # HEADERS
        loops_title = fig_LIGHT_PURPLE + pyfiglet.figlet_format(
            "Python Match and Loops"
        )  # change
        loops_subtitle = (
            f"{LIGHT_PURPLE}What Assignments Would You Like To Open?{RESET}".center(75)
        )

        clear_console()
        print(loops_title, end="")
        print("\n", loops_subtitle)
        print(
            f"""
{LIGHT_PURPLE}1. Plates{RESET}\n
{LIGHT_PURPLE}2. Twitter{RESET}\n
{LIGHT_PURPLE}3. Camel Case{RESET}\n
{LIGHT_PURPLE}4. Coke Machine{RESET}\n
{LIGHT_PURPLE}5. Nutrition{RESET}\n
. Back\n
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "plate", "plates"]:  # change
            try:
                openpy(plates)  # change
            except Exception as e:
                print(f"{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.loops_assignments()  # change

        elif self.week_select in ["2", "2.", "twitter"]:  # change
            try:
                openpy(twitter)  # change
            except Exception as e:
                print(f"{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.loops_assignments()  # change

        elif self.week_select in ["3", "3.", "camel", "case", "camel case"]:  # change
            try:
                openpy(camel)  # change
            except Exception as e:
                print(f"{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.loops_assignments()  # change

        elif self.week_select in ["4", "4.", "coke", "machine", "coke machine"]:  # change
            try:
                openpy(coke)  # change
            except Exception as e:
                print(f"{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.loops_assignments()  # change

        elif self.week_select in ["5", "5.", "nutrition"]:  # change
            try:
                openpy(nutrition)  # change
            except Exception as e:
                print(f"{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.loops_assignments()  # change

        elif self.week_select in [".", "back"]:  # change if needed
            self.page_loops()  # change

        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.loops_assignments()  # change

    # ---- Exceptions PAGE ----

    def page_exceptions(self):  # change
        exceptions_title = fig_CYAN + pyfiglet.figlet_format(
            "Python Exceptions"
        )  # Change Title
        exceptions_subtitle = f"{CYAN}What Would You Like To View?{RESET}".center(75)
        clear_console()
        print(exceptions_title, end="")
        print("\n", exceptions_subtitle)
        print(
            f"""
{CYAN}1. Written Notes{RESET}\n
{CYAN}2. Example Programs{RESET}\n
{CYAN}3. Assignments{RESET}\n
. Back
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "written notes"]:
            self.exception_notes()  # Change page
        elif self.week_select in ["2", "2.", "example programs", "programs"]:
            self.exceptions_programs()  # Change page
        elif self.week_select in ["3", "3.", "assignment", "assignments"]:
            self.exceptions_assignments()  # Change page
        elif self.week_select in [".", "back"]:
            self.home()
        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.page_exceptions()  # Change page

    def exception_notes(self):  # change name
        clear_console()
        exceptions_title = fig_GREEN + pyfiglet.figlet_format(
            "Python Exceptions"
        )  # Change Title
        exceptions_pdf = rf"{assets_path}\PDFs\Week 3 - Exceptions and Try-Except.pdf"  # Change pdf and name
        print(exceptions_title)
        try:
            os.startfile(exceptions_pdf)  # change argument name
            print(f"{GREEN}PDF Week 3 - Python Exceptions OPEN{RESET}")  # Change naming
        except Exception:
            print(
                f"{RED}PDF Week 3 - Python Exceptions FAILED TO OPEN{RESET}"
            )  # change naming
        input(f"\nPress {GREEN}Enter{RESET} to continue")
        self.page_exceptions()  # change name


    def exceptions_programs(self):  # change name
        # Headers
        exceptions_title = fig_RED + pyfiglet.figlet_format(
            "Python Exceptions"
        )  # Change Title
        exceptions_subtitle = f"{RED}What Program Would You Like To Open?{RESET}".center(75)

        # Programs
        value_e = rf"{assets_path}\Week 3 Exceptions\value_error.py"
        interrupt = rf"{assets_path}\Week 3 Exceptions\interrupt.py"


        clear_console()
        print(exceptions_title, end="")
        print("\n", exceptions_subtitle)
        print(
            f"""   
{RED}1. Value Errors{RESET}\n
{RED}2. Keyboard Interrupt{RESET}\n
. Back\n
\n\n
            """
        )  # Change Menu Choices
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "value", "error", "errors", "value error", "value errors"]:
            try:
                openpy(value_e)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.exceptions_programs()  # change name

        elif self.week_select in ["2", "2.", "keyboard", "interrupt", "keyboard interrupt"]:
            try:
                openpy(interrupt)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.exceptions_programs()  # change name

        elif self.week_select in [".", "back"]:  # change if needed
            self.page_exceptions()  # change name
        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.exceptions_programs()  # change name

    def exceptions_assignments(self):  # change name
        # Programs
        fuel = rf"{assets_path}\Week 3 Exceptions\Assignments\Fuel (Raise Exception)\fuel.py"
        outdated = rf"{assets_path}\Week 3 Exceptions\Assignments\Outdated Assignment (Dictionary)\outdated.py"
        felipes = rf"{assets_path}\Week 3 Exceptions\Assignments\Felipes\taqueria.py"
        grocery = rf"{assets_path}\Week 3 Exceptions\Assignments\Grocery\grocery.py"

        # Headers
        exceptions_title = fig_LIGHT_PURPLE + pyfiglet.figlet_format(
            "Python Exceptions"
        )  # change
        exceptions_subtitle = (
            f"{LIGHT_PURPLE}What Assignment Would You Like To Open?{RESET}".center(75)
        )

        clear_console()
        print(exceptions_title, end="")
        print("\n", exceptions_subtitle)
        print(
            f"""
{LIGHT_PURPLE}1. Fuel{RESET}\n
{LIGHT_PURPLE}2. Outdated{RESET}\n
{LIGHT_PURPLE}3. Felipes Taqueria{RESET}\n
{LIGHT_PURPLE}4. Grocery List{RESET}\n
. Back\n
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "fuel"]:  # change
            try:
                openpy(fuel)  # change
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.exceptions_assignments()  # change

        elif self.week_select in ["2", "2.", "outdated"]:  # change
            try:
                openpy(outdated)  # change
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.exceptions_assignments()  # change

        elif self.week_select in ["3", "3.", "felipe", "felipes", "taqueria", "felipes taqueria"]:  # change
            try:
                openpy(felipes)  # change
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.exceptions_assignments()  # change

        elif self.week_select in ["4", "4.", "grocery", "grocery list", "list"]:  # change
            try:
                openpy(grocery)  # change
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.exceptions_assignments()  # change

        elif self.week_select in [".", "back"]:  # change if needed
            self.page_exceptions()  # change

        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.exceptions_assignments()  # change

    # ---- LIBRARIES PAGE ----

    def page_libraries(self):
        libraries_title = fig_CYAN + pyfiglet.figlet_format(
            "Python Libraries"
        )  # Change Title
        libraries_subtitle = f"{CYAN}What Would You Like To View?{RESET}".center(75)
        clear_console()
        print(libraries_title, end="")
        print("\n", libraries_subtitle)
        print(
            f"""
{CYAN}1. Written Notes{RESET}\n
{CYAN}2. Example Programs{RESET}\n
{CYAN}3. Assignments{RESET}\n
. Back
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "written notes"]:
            self.libraries_notes()  # Change page
        elif self.week_select in ["2", "2.", "example programs", "programs"]:
            self.libraries_programs()  # Change page
        elif self.week_select in ["3", "3.", "assignment", "assignments"]:
            self.libraries_assignments()  # Change page
        elif self.week_select in [".", "back"]:
            self.home()
        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.page_libraries()  # Change page

    def libraries_notes(self):  # change name
        clear_console()
        libraries_title = fig_GREEN + pyfiglet.figlet_format(
            "Python Libraries"
        )  # Change Title
        libraries_subtitle = (
            f"{RED}No Written Notes for Week 4 - Libraries{RESET}".center(35)
        )
        print(libraries_title)
        print(libraries_subtitle)
        input(f"\nPress {GREEN}Enter{RESET} to continue")
        self.page_libraries()  # change name

    def libraries_programs(self):  # change name
        # Programs
        average = rf"{assets_path}\Week 4 Libraries\Average (py statistics)\average.py"
        json = rf"{assets_path}\Week 4 Libraries\Json (requests)\itunes.py"
        random = rf"{assets_path}\Week 4 Libraries\Random Choice and Shuffle\generate.py"

        # Headers
        libraries_title = fig_RED + pyfiglet.figlet_format(
            "Python Libraries"
        )  # Change Title
        libraries_subtitle = f"{RED}What Program Would You Like To Open?{RESET}".center(
            75
        )

        clear_console()
        print(libraries_title, end="")
        print("\n", libraries_subtitle)
        print(
            f"""   
{RED}1. Average{RESET}\n
{RED}2. Json{RESET}\n
{RED}3. Random{RESET}\n
. Back\n
\n\n
            """
        )  # Change Menu Choices
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "i", "average"]:  # change
            try:
                openpy(average)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.libraries_programs()  # change name

        elif self.week_select in ["2", "2.", "json"]:  # change
            try:
                openpy(json)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.libraries_programs()  # change name

        elif self.week_select in ["3", "3.", "random"]:  # change
            try:
                openpy(random)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.libraries_programs()  # change name

        elif self.week_select in [".", "back"]:  # change if needed
            self.page_libraries()  # change name

        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.libraries_programs()  # change name

    def libraries_assignments(self):  # change name
        # Assignments
        join_append = rf"{assets_path}\Week 4 Libraries\Assignments\adieu (join and append)\adieu.py"  # change
        response_request = rf"{assets_path}\Week 4 Libraries\Assignments\Bitcoin\bitcoin.py"  # change
        emojis = rf"{assets_path}\Week 4 Libraries\Assignments\Emojize\emojize.py"  # change
        figlet = rf"{assets_path}\Week 4 Libraries\Assignments\Figlet and sys.argv\figlet.py"  # change
        random_game = rf"{assets_path}\Week 4 Libraries\Assignments\Guessing Game (py Random)\guessing_game.py"  # change
        professor = rf"{assets_path}\Week 4 Libraries\Assignments\Professor (py random)\professor.py"  # change

        # Headers
        libraries_title = fig_LIGHT_PURPLE + pyfiglet.figlet_format(
            "Python Libraries"
        )  # change
        libraries_subtitle = (
            f"{LIGHT_PURPLE}What Assignment Would You Like To Open?{RESET}".center(75)
        )

        clear_console()
        print(libraries_title, end="")
        print("\n", libraries_subtitle)
        print(
            f"""
{LIGHT_PURPLE}1. Adieu - Join and Append{RESET}\n
{LIGHT_PURPLE}2. Bitcoin - Response and Request{RESET}\n
{LIGHT_PURPLE}3. Emojize - Emojis{RESET}\n
{LIGHT_PURPLE}4. Frank, Ian, & Glens Letters - Figlet{RESET}\n
{LIGHT_PURPLE}5. Guessing Game - Random{RESET}\n
{LIGHT_PURPLE}6. Little Professor - Random{RESET}\n

. Back\n
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in [
            "1",
            "1.",
            "adieu",
            "adieu - join and append",
            "adieu join and append",
            "join and append",
            "join",
            "append",
        ]:  # change
            try:
                openpy(join_append)  # change
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.libraries_assignments()  # change

        elif self.week_select in [
            "2",
            "2.",
            "bitcoin",
            "response",
            "request",
            "response and request",
            "bitcoin - response and request",
            "bitcoin response and request",
        ]:  # change
            try:
                openpy(response_request)  # change
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.libraries_assignments()  # change

        elif self.week_select in [
            "3",
            "3.",
            "emojize",
            "emojis",
            "emojize - emojis",
            "emojize emojis",
        ]:  # change
            try:
                openpy(emojis)  # change
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.libraries_assignments()  # change

        elif self.week_select in [
            "4",
            "4.",
            "figlet",
            "frank, ian, and glen",
            "frank, ian, & glen",
            "frank, ian, and glen letters",
            "frank, ian, & glen letters",
            "frank, ian, and glen letters - figlet",
            "frank, ian, & glen letters - figlet",
        ]:  # change
            try:
                openpy(figlet)  # change
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.libraries_assignments()  # change

        elif self.week_select in [
            "5",
            "5.",
            "guessing game",
            "guessing",
            "game",
            "guessing game - random",
            "guessing game random",
        ]:  # change
            try:
                openpy(random_game)  # change
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.libraries_assignments()  # change

        elif self.week_select in [
            "6",
            "6.",
            "professor",
            "little professor",
            "little professor random",
            "little professor - random",
        ]:  # change
            try:
                openpy(professor)  # change
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.libraries_assignments()  # change

        elif self.week_select in [".", "back"]:  # change if needed
            self.page_libraries()  # change

        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.libraries_assignments()  # change

    # ---- TEST PAGE ----

    def page_tests(self):
        tests_title = fig_CYAN + pyfiglet.figlet_format(
            "Python Unit Tests"
        )  # Change Title and variable name
        tests_subtitle = f"{CYAN}What Would You Like To View?{RESET}".center(
            75
        )  # change variable name
        clear_console()
        print(tests_title, end="")  # chaneg arg
        print("\n", tests_subtitle)  # change arg
        print(
            f"""
{CYAN}1. Written Notes{RESET}\n
{CYAN}2. Example Programs{RESET}\n
{CYAN}3. Assignments{RESET}\n
. Back
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "written notes"]:
            self.tests_notes()  # Change page
        elif self.week_select in ["2", "2.", "example programs", "programs"]:
            self.tests_programs()  # Change page
        elif self.week_select in ["3", "3.", "assignment", "assignments"]:
            self.tests_assignments()  # Change page
        elif self.week_select in [".", "back"]:
            self.home()
        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.page_tests()  # Change page

    def tests_notes(self):  # change name
        clear_console()
        tests_title = fig_GREEN + pyfiglet.figlet_format(
            "Python Unit Tests"
        )  # Change Title
        tests_pdf = rf"{assets_path}\PDFs\Week 5 - Unit Test - Pytest.pdf"  # Change pdf and name
        print(tests_title)
        try:
            os.startfile(tests_pdf)  # change argument name
            print(f"PDF Week 5 - Python Unit Tests {GREEN}Open{RESET}")  # Change naming
        except Exception:
            print(f"PDF Week 5 - Python Unit Tests {RED}Failed to Open{RESET}")
        input(f"\nPress {GREEN}Enter{RESET} to continue")
        self.page_tests()  # change name

    def tests_programs(self):  # change name

        # Headers
        tests_title = fig_RED + pyfiglet.figlet_format(
            "Python Unit Tests"
        )  # Change Title
        tests_subtitle = f"{RED}No Programs for Week 5 - Unit Tests{RESET}".center(75)

        clear_console()
        print(tests_title, end="")
        print("\n", tests_subtitle)
        print(
            f"""   
. Back\n
\n\n
            """
        )  # Change Menu Choices
        self.week_select = input("> ").strip().lower()
        if self.week_select in [".", "back"]:  # change if needed
            self.page_tests()  # change name

        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.tests_programs()  # change name

    def tests_assignments(self):  # change name
        # Assignments
        bank = rf"{assets_path}\Week 5 Unit Tests\Assignments\Bank\bank.py"  # change
        bank_test = rf"{assets_path}\Week 5 Unit Tests\Assignments\Bank\test_bank.py"  # change
        fuel = rf"{assets_path}\Week 5 Unit Tests\Assignments\Fuel (Raise Exception)\fuel.py"  # change
        fuel_test = rf"{assets_path}\Week 5 Unit Tests\Assignments\Fuel (Raise Exception)\test_fuel.py"  # change
        plates = rf"{assets_path}\Week 5 Unit Tests\Assignments\Plates (Functions)\plates.py"  # change
        plates_test = rf"{assets_path}\Week 5 Unit Tests\Assignments\Plates (Functions)\test_plates.py"  # change
        twitter = rf"{assets_path}\Week 5 Unit Tests\Assignments\Twttr\twttr.py"  # change
        twitter_test = rf"{assets_path}\Week 5 Unit Tests\Assignments\Twttr\test_twttr.py"  # change

        # Headers
        tests_title = fig_LIGHT_PURPLE + pyfiglet.figlet_format(
            "Python Unit Tests"
        )  # change
        tests_subtitle = (
            f"{LIGHT_PURPLE}What Assignment Would You Like To Open?{RESET}".center(75)
        )

        clear_console()
        print(tests_title, end="")
        print("\n", tests_subtitle)
        print(
            f"""
{LIGHT_PURPLE}1. Bank{RESET}\n
{LIGHT_PURPLE}2. Fuel{RESET}\n
{LIGHT_PURPLE}3. Plates{RESET}\n
{LIGHT_PURPLE}4. Twitter{RESET}\n
. Back\n
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "bank"]:  # change
            try:
                openpyfiles(bank, bank_test)
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.tests_assignments()  # change

        elif self.week_select in ["2", "2.", "fuel"]:  # change
            try:
                openpyfiles(fuel, fuel_test)  # change
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.tests_assignments()  # change

        elif self.week_select in ["3", "3.", "plate", "plates"]:  # change
            try:
                openpyfiles(plates, plates_test)  # change
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.tests_assignments()  # change

        elif self.week_select in ["4", "4.", "twitter"]:  # change
            try:
                openpyfiles(twitter, twitter_test)  # change
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.tests_assignments()  # change

        elif self.week_select in [".", "back"]:  # change if needed
            self.page_tests()  # change

        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.tests_assignments()  # change

    # ---- FILE IO PAGE ----

    def page_IO(self):
        IO_title = fig_CYAN + pyfiglet.figlet_format("Python File IO")  # Change Title
        IO_subtitle = f"{CYAN}What Would You Like To View?{RESET}".center(75)
        clear_console()
        print(IO_title, end="")
        print("\n", IO_subtitle)
        print(
            f"""
{CYAN}1. Written Notes{RESET}\n
{CYAN}2. Example Programs{RESET}\n
{CYAN}3. Assignments{RESET}\n
. Back
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "written notes"]:
            self.IO_notes()  # Change page
        elif self.week_select in ["2", "2.", "example programs", "programs"]:
            self.IO_programs()  # Change page
        elif self.week_select in ["3", "3.", "assignment", "assignments"]:
            self.IO_assignments()  # Change page
        elif self.week_select in [".", "back"]:
            self.home()
        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.page_IO()  # Change page

    def IO_notes(self):  # change name
        clear_console()
        IO_title = fig_GREEN + pyfiglet.figlet_format(
            "Python File IO"
        )  # Change Title and variable name
        IO_pdf = rf"{assets_path}\PDFs\Week 6 - File IO.pdf"  # Change pdf and name
        print(IO_title)
        try:
            os.startfile(IO_pdf)  # change argument name
            print(f"PDF Week 6 - Python File IO {GREEN}Open{RESET}")  # Change naming
        except Exception:
            print(
                f"PDF Week 6 - Python File IO {RED}Failed to Open{RESET}"
            )  # change naming
        input(f"\nPress {GREEN}Enter{RESET} to continue")
        self.page_IO()  # change name

    def IO_programs(self):  # change name
        # Programs
        pillow = rf"{assets_path}\Week 6 File IO\learn_pillow.py"  # change path
        open_txt = rf"{assets_path}\Week 6 File IO\names.py"  # change path
        dict_reader = (
            rf"{assets_path}\Week 6 File IO\students.py"
        )
        dict_writer = (
            rf"{assets_path}\Week 6 File IO\writecsv.py"
        )

        # Headers
        IO_title = fig_RED + pyfiglet.figlet_format("Python File IO")  # Change Title
        IO_subtitle = f"{RED}What Program Would You Like To Open?{RED}".center(75)

        clear_console()
        print(IO_title, end="")
        print("\n", IO_subtitle)
        print(
            f"""   
{RED}1. Open Image{RESET}\n
{RED}2. Open Text{RESET}\n
{RED}3. Use Dict Reader{RESET}\n
{RED}4. Use Dict Writer{RESET}\n
. Back\n
\n\n
            """
        )  # Change Menu Choices
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "open image", "image"]:  # change
            try:
                openpy(pillow)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.IO_programs()  # change name

        elif self.week_select in ["2", "2.", "text", "open text"]:  # change
            try:
                openpy(open_txt)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.IO_programs()  # change name

        elif self.week_select in [
            "3",
            "3.",
            "use dict reader",
            "dict reader",
        ]:  # change
            try:
                openpy(dict_reader)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.IO_programs()  # change name

        elif self.week_select in [
            "4",
            "4.",
            "use dict writer",
            "dict writer",
        ]:  # change
            try:
                openpy(dict_writer)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.IO_programs()  # change name

        elif self.week_select in [".", "back"]:  # change if needed
            self.page_IO()  # change name

        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.IO_programs()  # change name

    def IO_assignments(self):  # change name
        # Assignments
        shirt = rf"{assets_path}\Week 6 File IO\Assignments\CS50 Shirt\shirt.py"  # change
        lines_of_code = rf"{assets_path}\Week 6 File IO\Assignments\lines of code\lines.py"  # change
        pizza = rf"{assets_path}\Week 6 File IO\Assignments\pizza\pizza.py"
        scourgify = rf"{assets_path}\Week 6 File IO\Assignments\scourgify\scourgify.py"

        # Headers
        IO_title = fig_LIGHT_PURPLE + pyfiglet.figlet_format("Python File IO")  # change
        IO_subtitle = (
            f"{LIGHT_PURPLE}What Assignment Would You Like To Open?{RESET}".center(75)
        )

        clear_console()
        print(IO_title, end="")
        print("\n", IO_subtitle)
        print(
            f"""
{LIGHT_PURPLE}1. Shirt - Images{RESET}\n
{LIGHT_PURPLE}2. Lines of code - For Line in Lines{RESET}\n
{LIGHT_PURPLE}3. Pizza - CSV Reader & Tabulate{RESET}\n
{LIGHT_PURPLE}4. Scourgify - CSV DictReader & CSV DictWriter{RESET}\n
. Back\n
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in [
            "1",
            "1.",
            "shirt",
            "images",
            "image",
            "shirt images",
            "shirt - images",
        ]:  # change
            try:
                openpy(shirt)  # change
            except Exception as e:
                print(f"{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.IO_assignments()  # change

        elif self.week_select in [
            "2",
            "2.",
            "lines of code",
            "for line in lines",
            "lines of code - for line in lines",
            "lines of code for line in lines",
        ]:  # change
            try:
                openpy(lines_of_code)  # change
            except Exception as e:
                print(f"{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.IO_assignments()  # change

        elif self.week_select in [
            "3",
            "3.",
            "pizza",
            "csv reader",
            "tabulate",
            "csv reader & tabulate",
            "csv reader tabulate",
            "pizza csv reader & tabulate",
            "pizza - csv reader & tabulate",
        ]:  # change
            try:
                openpy(pizza)  # change
            except Exception as e:
                print(f"{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.IO_assignments()  # change

        elif self.week_select in [
            "4",
            "4.",
            "scourgify",
            "csv dictreader",
            "csv dictwriter",
            "dictreader",
            "dictwriter",
            "scourgify - csv dictreader & csv dictwriter",
        ]:  # change
            try:
                openpy(scourgify)  # change
            except Exception as e:
                print(f"{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.IO_assignments()  # change

        elif self.week_select in [".", "back"]:  # change if needed
            self.page_IO()  # change

        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.IO_assignments()  # change

    # ---- REGEX PAGE ----

    def page_regex(self):
        regex_title = fig_CYAN + pyfiglet.figlet_format(
            "Python Regular Expressions"
        )  # Change Title
        regex_subtitle = f"{CYAN}What Would You Like To View?{RESET}".center(
            75
        )  # change variable name
        clear_console()
        print(regex_title, end="")  # change
        print("\n", regex_subtitle)  # change
        print(
            f"""
{CYAN}1. Written Notes{RESET}\n
{CYAN}2. Example Programs{RESET}\n
{CYAN}3. Assignments{RESET}\n
. Back
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "written notes"]:
            self.regex_notes()  # Change page
        elif self.week_select in ["2", "2.", "example programs", "programs"]:
            self.regex_programs()  # Change page
        elif self.week_select in ["3", "3.", "assignment", "assignments"]:
            self.regex_assignments()  # Change page
        elif self.week_select in [".", "back"]:
            self.home()
        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.page_regex()  # Change page

    def regex_notes(self):  # change name
        clear_console()
        regex_title = fig_GREEN + pyfiglet.figlet_format(
            "Python Regular Expressions"
        )  # Change Title and variable name
        regex_pdf = rf"{assets_path}\PDFs\Week 7 - Regular Expressions.pdf"  # Change pdf and name
        print(regex_title)
        try:
            os.startfile(regex_pdf)  # change argument name
            print(
                f"{GREEN}PDF Week 7 - Python Regular Expressions OPEN{RESET}"
            )  # Change naming
        except Exception:
            print(
                f"{RED}PDF Week 7 - Python Regular Expressions FAILED TO OPEN{RESET}"
            )  # change naming
        input(f"\nPress {GREEN}Enter{RESET} to continue")
        self.page_regex()  # change name

    def regex_programs(self):  # change name
        # Programs
        colors = rf"{assets_path}\Week 7 Regular Expression\colors.py"  # change path
        format = rf"{assets_path}\Week 7 Regular Expression\format.py"  # change path
        phone = rf"{assets_path}\Week 7 Regular Expression\phone.py"
        twitter_validate = rf"{assets_path}\Week 7 Regular Expression\twitter.py"
        email_validate = rf"{assets_path}\Week 7 Regular Expression\validate.py"

        # Headers
        regex_title = fig_RED + pyfiglet.figlet_format(
            "Python Regular Expressions"
        )  # Change Title and variable
        regex_subtitle = f"{RED}What Program Would You Like To Open?{RESET}".center(
            75
        )  # change variable

        clear_console()
        print(regex_title, end="")
        print("\n", regex_subtitle)
        print(
            f"""   
{RED}1. Color HEX - Regex{RESET}\n
{RED}2. Name - Regex and Regex Groups{RESET}\n
{RED}3. Phone - Numbers Regex and Groups{RESET}\n
{RED}4. URL - Regex{RESET}\n
{RED}5. Email - Regex{RESET}\n
. Back\n
\n\n
            """
        )  # Change Menu Choices
        self.week_select = input("> ").strip().lower()
        if self.week_select in [
            "1",
            "1.",
            "color hex",
            "color",
            "hex",
            "color hex - regex",
        ]:  # change
            try:
                openpy(colors)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.regex_programs()  # change name

        elif self.week_select in [
            "2",
            "2.",
            "name",
            "name - regex",
            "name - regex and regex groups",
        ]:  # change
            try:
                openpy(format)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.regex_programs()  # change name

        elif self.week_select in [
            "3",
            "3.",
            "phone",
            "numbers regex",
            "phone - numbers regex",
            "phone - numbers regex and groups",
        ]:  # change
            try:
                openpy(phone)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.regex_programs()  # change name

        elif self.week_select in ["4", "4.", "url", "url - regex"]:  # change
            try:
                openpy(twitter_validate)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.regex_programs()  # change name

        elif self.week_select in ["5", "5.", "email", "email - regex"]:  # change
            try:
                openpy(email_validate)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.regex_programs()  # change name

        elif self.week_select in [".", "back"]:  # change if needed
            self.page_regex()  # change name

        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.regex_programs()  # change name

    def regex_assignments(self):  # change name
        # Assignments
        numbers = rf"{assets_path}\Week 7 Regular Expression\Assignments\numb3rs\numb3rs.py"
        numbers_test = rf"{assets_path}\Week 7 Regular Expression\Assignments\numb3rs\test_numb3rs.py"
        response = rf"{assets_path}\Week 7 Regular Expression\Assignments\response\response.py"
        um = rf"{assets_path}\Week 7 Regular Expression\Assignments\um\um.py"
        um_test = rf"{assets_path}\Week 7 Regular Expression\Assignments\um\test_um.py"
        working = rf"{assets_path}\Week 7 Regular Expression\Assignments\working\working.py"
        working_test = rf"{assets_path}\Week 7 Regular Expression\Assignments\working\test_working.py"
        watch = rf"{assets_path}\Week 7 Regular Expression\Assignments\YouTube\watch.py"

        # Headers
        regex_title = fig_LIGHT_PURPLE + pyfiglet.figlet_format(
            "Python Regular Expressions"
        )  # change
        regex_subtitle = (
            f"{LIGHT_PURPLE}What Assignment Would You Like To Open?{RESET}".center(75)
        )

        clear_console()
        print(regex_title, end="")
        print("\n", regex_subtitle)
        print(
            f"""
{LIGHT_PURPLE}1. IPv4 Filter - Numbers Regex{RESET}\n
{LIGHT_PURPLE}2. Email - Validators and Checkers{RESET}\n
{LIGHT_PURPLE}3. Counter - Re Find All{RESET}\n
{LIGHT_PURPLE}4. Time Converter - Naming Groups{RESET}\n
{LIGHT_PURPLE}5. HTML Parse - Groups and if Match{RESET}\n
. Back\n
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in [
            "1",
            "1.",
            "ipv4",
            "ipv4 filter",
            "numbers regex",
            "numbers",
            "ipv4 filter - numbers regex",
        ]:  # change
            try:
                openpyfiles(numbers, numbers_test)  # change
            except Exception as e:
                print(f"{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.regex_assignments()  # change

        elif self.week_select in [
            "2",
            "2.",
            "email",
            "validators",
            "checkers",
            "email - validators and checkers",
            "validators and checkers",
        ]:  # change
            try:
                openpy(response)  # change
            except Exception as e:
                print(f"{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.regex_assignments()  # change

        elif self.week_select in [
            "3",
            "3.",
            "counter",
            "re find all",
            "find all",
            "counter - re find all",
            "counter re find all",
        ]:  # change
            try:
                openpyfiles(um, um_test)  # change
            except Exception as e:
                print(f"{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.regex_assignments()  # change

        elif self.week_select in [
            "4",
            "4.",
            "time",
            "time converter",
            "naming",
            "naming groups",
            "time converter naming groups",
            "time converter - naming groups",
        ]:  # change
            try:
                openpyfiles(working, working_test)  # change
            except Exception as e:
                print(f"{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.regex_assignments()  # change

        elif self.week_select in [
            "5",
            "5.",
            "html",
            "html parse",
            "match",
            "groups and if match",
            "html parse groups and if match",
            "html parse - groups and if match",
        ]:  # change
            try:
                openpy(watch)  # change
            except Exception as e:
                print(f"{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.regex_assignments()  # change

        elif self.week_select in [".", "back"]:  # change if needed
            self.page_regex()  # change

        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.regex_assignments()  # change

    # ---- OOP PAGE ----

    def page_oop(self):
        oop_title = fig_CYAN + pyfiglet.figlet_format(
            "Python Object Orientated Programming"
        )  # Change Title
        oop_subtitle = f"{CYAN}What Would You Like To View?{RESET}".center(
            75
        )  # change variable name
        clear_console()
        print(oop_title, end="")  # change
        print("\n", oop_subtitle)  # change
        print(
            f"""
{CYAN}1. Written Notes{RESET}\n
{CYAN}2. Example Programs{RESET}\n
{CYAN}3. Assignments{RESET}\n
. Back
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "written notes"]:
            self.oop_notes()  # Change page
        elif self.week_select in ["2", "2.", "example programs", "programs"]:
            self.oop_programs()  # Change page
        elif self.week_select in ["3", "3.", "assignment", "assignments"]:
            self.oop_assignments()  # Change page
        elif self.week_select in [".", "back"]:
            self.home()
        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.page_oop()  # Change page

    def oop_notes(self):  # change name
        clear_console()
        oop_title = fig_GREEN + pyfiglet.figlet_format(
            "Python Object Orientated Programming"
        )  # Change Title and variable name
        oop_pdf = rf"{assets_path}\PDFs\Week 8 - Object Orientated Programming.pdf"  # Change pdf and name
        print(oop_title)
        try:
            os.startfile(oop_pdf)  # change argument name
            print(
                f"PDF Week 8 - Python Object Orientated Programming {GREEN}Open{RESET}"
            )  # Change naming
        except Exception:
            print(
                f"PDF Week 8 - Python Object Orientated Programming {RED}Failed to Open{RESET}"
            )  # change naming
        input(f"\nPress {GREEN}Enter{RESET} to continue")
        self.page_oop()  # change name

    def oop_programs(self):  # change name
        # Programs
        class_method = rf"{assets_path}\Week 8 OOP\hat.py"
        gettersetter = (
            rf"{assets_path}\Week 8 OOP\student.py"
        )
        str_method = (
            rf"{assets_path}\Week 8 OOP\student2.py"
        )
        add_method = rf"{assets_path}\Week 8 OOP\vault.py"
        parent_method = (
            rf"{assets_path}\Week 8 OOP\wizard.py"
        )

        # Headers
        oop_title = fig_RED + pyfiglet.figlet_format(
            "Python Object Orientated Programming"
        )  # Change Title and variable
        oop_subtitle = f"{RED}What Program Would You Like To Open?{RESET}".center(
            75
        )  # change variable

        clear_console()
        print(oop_title, end="")
        print("\n", oop_subtitle)
        print(
            f"""   
{RED}1. Class Method{RESET}\n
{RED}2. Getter and Setter{RESET}\n
{RED}3. Str Method{RESET}\n
{RED}4. Add Method{RESET}\n
{RED}5. Parent Class and Super{RESET}\n
. Back\n
\n\n
            """
        )  # Change Menu Choices
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "class method"]:  # change
            try:
                openpy(class_method)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.oop_programs()  # change name

        elif self.week_select in [
            "2",
            "2.",
            "getter",
            "getter and setter",
            "setter",
        ]:  # change
            try:
                openpy(gettersetter)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.oop_programs()  # change name

        elif self.week_select in ["3", "3.", "str", "str method"]:  # change
            try:
                openpy(str_method)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.oop_programs()  # change name

        elif self.week_select in ["4", "4.", "add", "add method"]:  # change
            try:
                openpy(add_method)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.oop_programs()  # change name

        elif self.week_select in [
            "5",
            "5.",
            "parent",
            "super",
            "parent class",
            "parent class and super",
        ]:  # change
            try:
                openpy(parent_method)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.oop_programs()  # change name

        elif self.week_select in [".", "back"]:  # change if needed
            self.page_oop()  # change name

        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.oop_programs()  # change name

    def oop_assignments(self):  # change name
        # Assignments
        jar = rf"{assets_path}\Week 8 OOP\Assignments\jar\jar.py"
        jar_test = rf"{assets_path}\Week 8 OOP\Assignments\jar\test_jar.py"
        seasons = rf"{assets_path}\Week 8 OOP\Assignments\seasons\seasons.py"
        seasons_test = rf"{assets_path}\Week 8 OOP\Assignments\seasons\test_seasons.py"
        shirt = rf"{assets_path}\Week 8 OOP\Assignments\shirtificate\shirtificate.py"

        # Headers
        regex_title = fig_LIGHT_PURPLE + pyfiglet.figlet_format(
            "Python Object Orientated Programming"
        )  # change
        regex_subtitle = (
            f"{LIGHT_PURPLE}What Assignment Would You Like To Open?{RESET}".center(75)
        )

        clear_console()
        print(regex_title, end="")
        print("\n", regex_subtitle)
        print(
            f"""
{LIGHT_PURPLE}1. Jar - Str Method{RESET}\n
{LIGHT_PURPLE}2. Seasons - Modifying Dates w/ Inflect{RESET}\n
{LIGHT_PURPLE}3. Shirtificate - Making PDFs w/ FPDF{RESET}\n
. Back\n
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in [
            "1",
            "1.",
            "jar",
            "str",
            "str method",
            "jar str method",
            "jar - str method",
        ]:  # change
            try:
                openpyfiles(jar, jar_test)  # change
            except Exception as e:
                print(f"{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.oop_assignments()  # change

        elif self.week_select in [
            "2",
            "2.",
            "seasons",
            "season",
            "dates",
            "inflect",
            "seasons - modifying dates w/ inflect",
            "modifying dates w/ inflect",
        ]:  # change
            try:
                openpyfiles(seasons, seasons_test)  # change
            except Exception as e:
                print(f"{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.oop_assignments()  # change

        elif self.week_select in [
            "3",
            "3.",
            "shirt",
            "shirtificate",
            "pdf",
            "pdfs",
            "fpdf",
            "making pdfs",
            "making pdfs w/ fpdf",
            "shirtificate - making pdfs w/ fpdf",
        ]:  # change
            try:
                openpy(shirt)  # change
            except Exception as e:
                print(f"{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.oop_assignments()  # change

        elif self.week_select in [".", "back"]:  # change if needed
            self.page_oop()  # change

        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.oop_assignments()  # change

    # ---- Et Cetera PAGE ----

    def page_cetera(self):
        cetera_title = fig_CYAN + pyfiglet.figlet_format(
            "Python Et Cetera"
        )  # Change Title and variable name
        cetera_subtitle = f"{CYAN}What Would You Like To View?{RESET}".center(
            75
        )  # change variable name
        clear_console()
        print(cetera_title, end="")  # change
        print("\n", cetera_subtitle)  # change
        print(
            f"""
{CYAN}1. Written Notes{RESET}\n
{CYAN}2. Example Programs{RESET}\n
{CYAN}3. Assignments{RESET}\n
. Back
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "written notes"]:
            self.cetera_notes()  # Change page
        elif self.week_select in ["2", "2.", "example programs", "programs"]:
            self.cetera_programs()  # Change page
        elif self.week_select in ["3", "3.", "assignment", "assignments"]:
            self.cetera_assignments()  # Change page
        elif self.week_select in [".", "back"]:
            self.home()
        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.page_cetera()  # Change page

    def cetera_notes(self):  # change name
        clear_console()
        cetera_title = fig_GREEN + pyfiglet.figlet_format(
            "Python Et Cetera"
        )  # Change Title and variable name
        cetera_pdf = rf"{assets_path}\PDFs\Week 9 - Et Cetera.pdf"  # Change pdf and name
        print(cetera_title)
        try:
            os.startfile(cetera_pdf)  # change argument name
            print(f"PDF Week 9 - Python Et Cetera {GREEN}Open{RESET}")  # Change naming
        except Exception:
            print(
                f"PDF Week 9 - Python Et Cetera {RED}Failed to Open{RESET}"
            )  # change naming
        input(f"\nPress {GREEN}Enter{RESET} to continue")
        self.page_cetera()  # change name

    def cetera_programs(self):  # change name
        # Programs
        prog_filters = (
            rf"{assets_path}\Week 9 Et Cetera\filters.py"
        )
        prog_global = (
            rf"{assets_path}\Week 9 Et Cetera\global.py"
        )
        prog_argparse = rf"{assets_path}\Week 9 Et Cetera\how_argparse.py"
        prog_yield = rf"{assets_path}\Week 9 Et Cetera\how_yield.py"
        prog_math = (
            rf"{assets_path}\Week 9 Et Cetera\math.py"
        )
        prog_say = (
            rf"{assets_path}\Week 9 Et Cetera\say.py"
        )
        prog_sets = (
            rf"{assets_path}\Week 9 Et Cetera\sets.py"
        )
        prog_unpack = (
            rf"{assets_path}\Week 9 Et Cetera\unpack.py"
        )

        # Headers
        cetera_title = fig_RED + pyfiglet.figlet_format(
            "Python Et Cetera"
        )  # Change Title and variable
        cetera_subtitle = f"{RED}What Program Would You Like To Open?{RESET}".center(
            75
        )  # change variable

        clear_console()
        print(cetera_title, end="")
        print("\n", cetera_subtitle)
        print(
            f"""   
{RED}1. Filters{RESET}\n
{RED}2. Global{RESET}\n
{RED}3. Argparse{RESET}\n
{RED}4. Yield{RESET}\n
{RED}5. Math{RESET}\n
{RED}6. Say{RESET}\n
{RED}7. Sets{RESET}\n
{RED}8. Unpack{RESET}\n
. Back\n
\n\n
            """
        )  # Change Menu Choices
        self.week_select = input("> ").strip().lower()
        if self.week_select in ["1", "1.", "filter", "filters"]:  # change
            try:
                openpy(prog_filters)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.cetera_programs()  # change name

        elif self.week_select in ["2", "2.", "gloabl"]:  # change
            try:
                openpy(prog_global)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.cetera_programs()  # change name

        elif self.week_select in ["3", "3.", "argparse", "arg", "parse"]:  # change
            try:
                openpy(prog_argparse)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.cetera_programs()  # change name

        elif self.week_select in ["4", "4.", "yield"]:  # change
            try:
                openpy(prog_yield)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.cetera_programs()  # change name

        elif self.week_select in ["5", "5.", "math"]:  # change
            try:
                openpy(prog_math)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.cetera_programs()  # change name

        elif self.week_select in ["6", "6.", "say"]:  # change
            try:
                openpy(prog_say)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.cetera_programs()  # change name

        elif self.week_select in ["7", "7.", "set", "sets"]:  # change
            try:
                openpy(prog_sets)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.cetera_programs()  # change name

        elif self.week_select in ["8", "8.", "unpack"]:  # change
            try:
                openpy(prog_unpack)  # change arg
            except Exception as e:
                print(f"\n{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.cetera_programs()  # change name

        elif self.week_select in [".", "back"]:  # change if needed
            self.page_cetera()  # change name

        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.cetera_programs()  # change name

    def cetera_assignments(self):  # change name
        # Assignments
        project_path = os.path.dirname(os.path.abspath(__file__))
        final_project = fr"{project_path}\project.py"

        # Headers
        cetera_title = fig_LIGHT_PURPLE + pyfiglet.figlet_format(
            "Python Et Cetera"
        )  # change
        cetera_subtitle = (
            f"{GREEN}This is the program you are currently using!{RESET}".center(75)
        )

        clear_console()
        print(cetera_title, end="")
        print("\n", cetera_subtitle)
        print(
            f"""
{LIGHT_PURPLE}1. Final Project{RESET} - {GREEN}This Program{RESET}\n
. Back\n
\n\n
            """
        )
        self.week_select = input("> ").strip().lower()
        if self.week_select in [
            "1",
            "1.",
            "final",
            "project",
            "final project",
            "this program",
            "final project this program",
            "final project - this program",
        ]:  # change
            try:
                open_read_only(final_project)  # change
            except Exception as e:
                print(f"{RED}Failed to open{RESET}")
                input(f"press {GREEN}Enter{RESET} to continue")
            self.cetera_assignments()  # change

        elif self.week_select in [".", "back"]:  # change if needed
            self.page_cetera()  # change

        else:
            print(f"\n{RED}invalid selection{RESET}")
            input(f"press {GREEN}Enter{RESET} to continue")
            self.cetera_assignments()  # change


# Colors Ansi for Basic Text
RED = "\033[0;31m"
GREEN = "\033[0;32m"
CYAN = "\033[0;36m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"
LIGHT_PURPLE = "\033[1;35m"

text_colors = [RED, GREEN, CYAN, YELLOW, LIGHT_PURPLE]


def random_Textcolor():
    return random.choice(text_colors)


# Colorama Colors for Figlet
fig_RED = Fore.RED
fig_GREEN = Fore.GREEN
fig_YELLOW = Fore.YELLOW
fig_BLUE = Fore.BLUE
fig_MAGENTA = Fore.MAGENTA
fig_CYAN = Fore.CYAN
fig_LIGHT_PURPLE = Fore.LIGHTMAGENTA_EX

fig_colors = [
    fig_RED,
    fig_GREEN,
    fig_YELLOW,
    fig_BLUE,
    fig_MAGENTA,
    fig_CYAN,
    fig_LIGHT_PURPLE,
]


def random_FIGcolor():
    return random.choice(fig_colors)


# FULLSCREEN CMD
fullscreen = win32gui.GetForegroundWindow()

assets_path = ""
# ---- Get User Directory for Files ----
def get_assets():
    global assets_path
    try:
        with open("config.txt", "x") as file:
            new_path = input("Copy and Paste path of 'Assets' Folder: ").strip()
            assets_path = new_path.replace("\"", "")
            with open("config.txt", "w") as new_config:
                new_config.write(assets_path)
    except FileExistsError:
        with open("config.txt", "r") as file:
            first_line = file.readline().strip("\n")
            assets_path = first_line.replace("\"", "")
    return assets_path

def fix_files():
    global assets_path
    new_path = input("Copy and Paste path of 'Assets' Folder: ").strip()
    assets_path = new_path.replace("\"", "")
    with open("config.txt", "w") as new_config:
        new_config.write(assets_path)



# ---- MAIN ----
def main():
    get_assets()
    cursor.hide()
    try:
        win32gui.ShowWindow(fullscreen, win32con.SW_MAXIMIZE)
    except Exception:
        pass
    pages = Pages()
    pages.intro()
    while True:
        pages.home()
        pages.change_page()


def openpy(file):
    if not os.path.exists(file):
        raise FileNotFoundError(f"File {file} Not Found")
    subprocess.run(["python", "-m", "idlelib.idle", file])


def open_read_only(file):
    if not os.path.exists(file):
        raise FileNotFoundError(f"File {file} Not Found")
    os.chmod(file, stat.S_IREAD)
    subprocess.run(["python", "-m", "idlelib.idle", file])


def openpyfiles(file1, file2):
    thread1 = threading.Thread(target=openpy, args=([file1]))
    thread2 = threading.Thread(target=openpy, args=([file2]))

    if os.path.exists(file1):
        thread1.start()
    else:
        raise FileNotFoundError(f"File {file1} Not Found")

    if os.path.exists(file2):
        thread2.start()
    else:
        raise FileNotFoundError(f"File {file2} Not Found")


def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":
    main()
