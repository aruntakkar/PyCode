class Parent():

    def print_last_name(self):
        print('Takkar')


class Child(Parent):

    def print_first_name(self):
        print('Arun')

    # overriding the parent function
    def print_last_name(self):
        print('Kumar')

bucky = Child()
bucky.print_first_name()
bucky.print_last_name()
