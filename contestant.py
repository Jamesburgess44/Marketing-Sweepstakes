from userinterface import UserInterface


class Contestant:
    def __init__(self):
        self.first_name = UserInterface.get_user_input_string("Enter first name")
        self.last_name = UserInterface.get_user_input_string("Enter last name")
        self.email = UserInterface.get_user_input_string("Enter email address")
        self.registration_number = 0
    pass

    def notify(self, is_winner):
        pass