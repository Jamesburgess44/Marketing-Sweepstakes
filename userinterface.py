class UserInterface:
    """I want to create a user interface for any information the application would need
    to get or display for the user. One example would be to create a method called
    “get_user_input_string” that takes in a prompt and returns the user’s entered input"""
    @staticmethod
    def display_message(message):
        pass

    @staticmethod
    def get_user_input_string(prompt):
        user_input = imput(prompt)
        return user_input

    @staticmethod
    def get_user_input_int(prompt):
        user_input = int(input(prompt))
        return user_input

    @staticmethod
    def display_contestant_info(contestant):
        pass

    @staticmethod
    def display_sweepstakes_info(sweepstakes):
        pass

    @staticmethod
    def display_sweepstakes_selection_menu(all_sweepstakes):
        pass

    @staticmethod
    def display_marketing_firm_menu_options(marketing_firm_name):
        pass

    @staticmethod
    def display_sweepstakes_menu_options(sweepstakes):
        pass