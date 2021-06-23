from userinterface import UserInterface
from contestant import Contestant

class Sweepstakes:
    def __init__(self):
        self.name = UserInterface.get_user_input_string("Enter the name of your sweepstakes.")
        self.contestants = {}

    def register_contestant(self, contestant):
        contestant.registration_number = len(self.contestants)
        self.contestants.update({len(self.contestants): contestant})

    def pick_winner(self):
        """should return a constant"""
        pass

    def view_contestant(self):
        for contestant in self.contestants.values():
            UserInterface.display_contestant_info(contestant)

    def menu(self):
        UserInterface.display_sweepstakes_menu_options()
        user_selection = UserInterface.get_user_input_int("Enter the number of your choice")
        if user_selection == 1:
            Sweepstakes.register_contestant(Contestant())
        elif user_selection == 2:
            Sweepstakes.pick_winner("")
        elif user_selection == 3:
            Sweepstakes.view_contestant("")
        else:
            pass