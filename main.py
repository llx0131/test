# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def test(a, b):
    print("test")
    c = a + b
    return c

class Cat:
    def __init__(self, name_, sex_):
        self.name = name_
        self.sex = sex_

    def __str__(self):
        return self.name+",,,"+self.sex


    def print_name(self):
        print(self.name)

    def set_name(self,name):
        self.name = name

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    c = test(1, 2)
    print(c)


    cat = Cat ("Tom", "Male")
    print(cat)
    print(cat.sex)


    cat.print_name()
    cat.set_name("Jerry")
    cat.print_name()