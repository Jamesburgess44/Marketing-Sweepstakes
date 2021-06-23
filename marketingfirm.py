from userinterface import UserInterface
from sweepstakes import Sweepstakes

class MarketingFirm:

    def __init__(self):
        self.name = "name"
        self.sweepstakes_dictionary = ["Publishers Clearing house", "Other sweepstakes"]

    def create_sweepstakes(self):
        new_sweepstakes = UserInterface.get_user_input_string("Enter name of new sweepstakes")
        self.sweepstakes_dictionary.append(new_sweepstakes)

    def select_sweepstakes(self):
        """once I select a sweepstakes from the select_sweepstakes method, I should be taken to that sweepstakes menu"""
        pass

    def change_marketing_firm_name(self):
        self.name = UserInterface.get_user_input_string("Enter your firm name")

    def menu(self):
        UserInterface.display_marketing_firm_menu_options()
        user_selection = UserInterface.get_user_input_int("Enter the number of your choice")
        if user_selection == 1:
            MarketingFirm.create_sweepstakes("")
        elif user_selection == 2:
            self.select_sweepstakes()
        elif user_selection == 3:
            self.change_marketing_firm_name()
        else:
            pass

