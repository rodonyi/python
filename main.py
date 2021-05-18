from math import add_numbers
from person import Person

name = "Jamil"
name2 = "Jamila"


def hello(nam: str):
    print(nam.upper())


def hello2(ame: str):
    print(ame.upper())


def method_name(name="alex"):
    p = Person(name)  # default name: "alex"
    print(p)


if __name__ == '__main__':
    print("Pycharm is ...")
    print("Hello")
    print("%s" % "Ahmed")
    print("PYCHARM is ...")
    print(add_numbers(2, 3))
    method_name("Ali")
