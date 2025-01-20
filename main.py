import time as t
import game_functions as game
import logging

month = 0
last_paid = 0
if not logging.output_log("intro_check"):
    game.begin()
    game.explain_parts()
    print('Congrats! You\'ve ordered all your parts needed to make your pet rocks!')
    game.sleep(3)
    print('While you wait for your parts to arrive, let\'s pay back off your first month of your loan to the bank!')
    game.pay_the_bank()

    print('Your parts look like they have arrived!')
    print('Let\'s get started with your business!')

    game.sleep(2)
    logging.log("intro_check",True)
print('Welcome to your main dashboard. This will be your main way to run your business.')

print('Choose an option from your dashboard.')
game.dashboard()





