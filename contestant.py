from userinterface import UserInterface


class Contestant:
    """, I want to create a Contestant class that has a first name, last name, email address, and registration number."""
    def __init__(self):
        self.first_name = UserInterface.get_user_input_string("Enter first name")
        self.last_name = UserInterface.get_user_input_string("Enter last name")
        self.email = UserInterface.get_user_input_string("Enter email address")
        self.registration_number = 0
    pass

    def notify(self, is_winner):
        """, I want to use the observer design pattern to notify all users of the winning contestant,
        with the winner of the sweepstakes receiving a different message specifically congratulating
        them on being the winner. This notification will be triggered within the sweepstakes pick_winner method. """
        pass