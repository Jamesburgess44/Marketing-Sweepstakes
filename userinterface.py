from marketingfirm import MarketingFirm
from sweepstakes import Sweepstakes
import marketingfirm




class UserInterface:
    """I want to create a user interface for any information the application would need
    to get or display for the user. One example would be to create a method called
    “get_user_input_string” that takes in a prompt and returns the user’s entered input"""
    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def get_user_input_string(prompt):
        user_input = input(prompt)
        return user_input

    @staticmethod
    def get_user_input_int(prompt):
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("please enter a number!")
            return UserInterface.get_user_input_int(prompt)

    @staticmethod
    def display_contestant_info(contestant):
        print(f"Contestant #{contestant.registration_number} is {contestant.first_name} {contestant.last_name} and their email is {contestant.email}")

    @staticmethod
    def display_sweepstakes_info(sweepstakes):
        pass

    @staticmethod
    def display_sweepstakes_selection_menu(all_sweepstakes):
        i = 1  # for displaying in terminal
        print("Which sweepstake would you like to interact with?:")
        for sweepstake in all_sweepstakes:
            print(f"{i}: {sweepstake.name}")
        
    @staticmethod
    def display_marketing_firm_menu_options():
        print("Enter -1- to create a sweepstakes.")
        print("Enter -2- to change the marketing firm name. ")
        print("Enter -3- to select a sweepstakes. ")
        user_selection = int(input("Enter number here:"))
        if user_selection == 1:
            MarketingFirm.create_sweepstakes()
        elif user_selection == 2:
            MarketingFirm.change_marketing_firm_name()
        elif user_selection == 3:
            MarketingFirm.select_sweepstakes()
        else:
            pass

    @staticmethod
    def display_sweepstakes_menu_options(sweepstakes):
        pass