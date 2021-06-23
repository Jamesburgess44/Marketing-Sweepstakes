from marketingfirm import MarketingFirm
from sweepstakes import Sweepstakes
from userinterface import UserInterface

UserInterface.welcome_to_app()
user_selection = UserInterface.get_user_input_int("Enter the number of your choice")
if user_selection == 1:
    MarketingFirm.menu("")
elif user_selection == 2:
    Sweepstakes.menu("")
else:
    pass