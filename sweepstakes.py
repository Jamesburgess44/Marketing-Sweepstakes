from userinterface import UserInterface
from contestant import Contestant

class Sweepstakes:
    def __init__(self):
        self.name = UserInterface.get_user_input_string("Enter the name of your sweepstakes.")
        self.contestants = []

    def register_contestant(self, contestant):
        pass

    def pick_winner(self):
        """should return a constant"""
        pass

    def view_contestant(self):
        pass

    def menu(self):
        """, I want the sweepstakes menu to provide a façade interface for viewing contestants, registering a new contestant,
         picking a winner, and exiting the sweepstakes menu"""
        UserInterface.display_sweepstakes_menu_options()
        pass