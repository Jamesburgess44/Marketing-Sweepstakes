from userinterface import UserInterface

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
        pass

    def menu(self):
        """I want the marketing firm menu to provide a façade interface for selecting a sweepstakes,
        creating a sweepstakes, changing the marketing firm name, and exiting the application"""
        UserInterface.display_marketing_firm_menu_options()
        pass
