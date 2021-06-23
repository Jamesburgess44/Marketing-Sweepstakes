from userinterface import UserInterface
from sweepstakes import Sweepstakes

class MarketingFirm:
    def __init__(self):
        self.name = UserInterface.get_user_input_string("Enter the name of your marketing firm")
        self.sweepstakes_dictionary = []

    def create_sweepstakes(self):
        pass

    def select_sweepstakes(self):
        """once I select a sweepstakes from the select_sweepstakes method, I should be taken to that sweepstakes menu"""
        pass

    def change_marketing_firm_name(self):
        self.name()
        pass

    def menu(self):
        will_this_work = True
        while will_this_work:
            UserInterface.display_marketing_firm_menu_options()
            user_selection = UserInterface.get_user_input_int("Enter the number of your choice")
            if user_selection == 1:
                self.create_sweepstakes()
            elif user_selection == 2:
                self.select_sweepstakes()
            elif user_selection == 3:
                self.change_marketing_firm_name()
            else:
                pass

