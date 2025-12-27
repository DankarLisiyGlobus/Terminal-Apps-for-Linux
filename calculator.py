import curses
import math

window = [
    "|             Калькулятор             |",
    "|                                     |",
    "|                                     |",
    "|                                     |",
    "[ del ] [     ] [     ] [ mod ] [  π  ]",
    "|                                     |",
    "[  7  ] [  8  ] [  9  ] [  ÷  ] [  √  ]",
    "|                                     |",
    "[  4  ] [  5  ] [  6  ] [  *  ] [  x² ]",
    "|                                     |",
    "[  1  ] [  2  ] [  3  ] [  -  ] [  =  ]",
    "|                                     |",
    "[  0  ] [  ,  ] [  %  ] [  +  ] [  =  ]",
]

result_line = 2

class Calculator:
    def __init__(self):
        self.result = ""
    def main(self,stdscr):
        self.stdscr = stdscr
        self.stdscr.clear()
        self.stdscr.refresh()
        for i,line in enumerate(window):
            self.stdscr.addstr(i,0,line)
        self.print_result()
        while True:
            key = self.get_key()

            if chr(key) == "0":
                if self.result == "0":
                    self.result = "0"
                else:
                    self.result += "0"
            elif chr(key) == "1":
                if self.result == "0":
                    self.result = "1"
                else:
                    self.result += "1"
            elif chr(key) == "2":
                if self.result == "0":
                    self.result = "2"
                else:
                    self.result += "2"
            elif chr(key) == "3":
                if self.result == "0":
                    self.result = "3"
                else:
                    self.result += "3"
            elif chr(key) == "4":
                if self.result == "0":
                    self.result = "4"
                else:
                    self.result += "4"
            elif chr(key) == "5":
                if self.result == "0":
                    self.result = "5"
                else:
                    self.result += "5"
            elif chr(key) == "6":
                if self.result == "0":
                    self.result = "6"
                else:
                    self.result += "6"
            elif chr(key) == "7":
                if self.result == "0":
                    self.result = "7"
                else:
                    self.result += "7"
            elif chr(key) == "8":
                if self.result == "0":
                    self.result = "8"
                else:
                    self.result += "8"
            elif chr(key) == "9":
                if self.result == "0":
                    self.result = "9"
                else:
                    self.result += "9"
            elif key == 46 or key == 44:
                if len(self.result) == 0:
                    self.result = "0."
                else:
                    if self.result[-1] != ".":
                        self.result += "."
                    else:
                        pass
            elif chr(key) == "+":
                self.result += "+"
            elif chr(key) == "-":
                self.result += "-"
            elif chr(key) == "/":
                self.result += "/"
            elif chr(key) == "*":
                self.result += "*"
            elif key == 186 or key == 114:
                self.result = str(int(self.result) ** 0.5)
            elif key == 109 or key == 140:
                if len(self.result) != 0 and self.result[-1] != "%":
                    self.result += "%"
            elif key == 135 or key == 120:
                if len(self.result) != 0:
                    self.result = str(int(self.result) ** 2)
            elif key == 112 or key == 183:
                self.result = str(math.pi)
            elif chr(key) == "=" or key == 10:
                if self.result != 0:
                    try:
                        self.result = str(eval(self.result))
                    except Exception as e:
                        self.result = str(e)
            elif key == 263 or key == 330:
                if len(self.result) > 0:
                    self.result = self.result[:-1]
                else:
                    pass
            
            self.print_result()

    def get_key(self):
        return self.stdscr.getch()
    def print_result(self):
        self.stdscr.addstr(result_line,0,"| "+(35-len(str(self.result)))*" "+str(self.result)+" |" if len(str(self.result)) <= 35 else "|   Error:Длина числа превышает 35    |")


calc = Calculator()

curses.wrapper(calc.main)
