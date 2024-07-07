
import random as r
import time
import time as t
first_manufacture = False
machinery_level = 0

min_credit_score = 1

credit_score = 5

# Global Variable Declaration
rock_price = r.randint(40,60)
rock_price+=0.99
bad_person_per_month_payment = 0
payments_remaining = 0

per_month_payment = 0
money = 0

def sleep(n):
    t.sleep(n)
def explain_parts():
    print(f'In order to manufacture your rocks, you\'ll need to order some parts.')
    t.sleep(2)
    print('Your first part in your pet rock manufacturing are rocks! They cost $' + str(rock_price) + ' per ton.')
    t.sleep(3)
    print('Your next part is paint. Paint will cost you $129.99 per gallon. You can save 3% to a max of 12% for each additional gallon when you order in bulk.')
    t.sleep(4)
    print('Your last part is googly eyes. Googly eyes cost $2.99 per 500ct. You can save 8% to a max of 32% for each additional 500 when you order in bulk.')
    time.sleep(4)
    order_parts()



def ask():
    return input('-> ')
def loan(time,amount):
    global per_month_payment, payments_remaining, credit_score, bad_person_per_month_payment
    # credit score is ranked on a scale of 1-10, and your chances of getting a better loan depend on it
    interest = round((20 - credit_score * 2) * 0.45, 2)
    luck = r.randint(1,5)
    payments_remaining = time
    if credit_score > 7:
        print('You have been granted a loan for ' + str(amount) + ' dollars and ' + str(interest) + '% interest for ' + str(time) + ' months.')
        add_money(amount-(luck/100)*amount)
        per_month_payment = round(int(amount-(luck/100)*amount),2)
    elif credit_score > 4:
        print('You have been granted a loan for ' + str(int(amount-(luck/100)*amount)) + ' dollars and ' + str(interest+luck/5) + '% interest for ' + str(time) + ' months.')
        add_money(int(amount-(luck/100)*amount))
        per_month_payment = round(int(amount-(luck/100)*amount)/time,2)
    elif credit_score > min_credit_score:
        print('You have been granted a loan for ' + str(int(amount-(luck/100)*amount*2)) + ' dollars and ' + str(interest+luck/5/2) + '% interest for ' + str(time) + ' months.')
        add_money(int(amount-(luck/100)*amount*2))
        per_month_payment = round(int(amount-(luck/100)*amount*2)/time,2)
    if credit_score <= min_credit_score:
        print('Your loan has been denied.')
    bad_person_per_month_payment = per_month_payment
        
    
        
def begin():
    print('WELCOME TO SELL SELL SELL!')
    print('The Buying and Selling Game')
    t.sleep(1)
    print('Today, you\'ll be starting the company Rockin\' Rascals, who sell customizable pet rocks.')
    
    loan_amount = r.randint(3,10)
    loan_amount *= 10000
    loan_time = r.randint(3,5)
    
    
    print('You need to take out a loan for $' + str(loan_amount) + ' and for ' + str(loan_time*12) + ' months to start your business.')
    print('Would you like to accept the loan terms? (y/n)')
    answer = input('-> ')
    if answer == 'y':
        print('The bank is evaluating your offer based on your credit history. They might not give you the loan you want.')
        t.sleep(r.randint(3,5))
        loan(loan_time*12,loan_amount)
        time.sleep(3)
    else: print('You attempted to start your business, but it couldn\'t take off due to insufficient funds. GAME OVER')
    
def add_money(amount):
    global money
    money += amount
def order_parts():
    global money
    
    
    print('How many tons of rocks would you like to order? You have $' + str(money) + ' left in your account.')
    rocks = ask() 
    money -= rock_price*int(rocks)
    print('Order complete, costing $' + str(int(rocks) * rock_price))
    
    
    print('How many gallons of paint would you like to order? You have $' + str(money) + ' left in your account.')
    paint = ask()
    discount = (int(paint) - 1)*3
    if discount > 12:
        discount = 12
    paint_money_spent = int(paint) * (129.99-(129.99*(discount/100))) # this looks confusing, but it isn't.
    paint_money_spent = round(paint_money_spent,2)
    money -= paint_money_spent
    print('Order complete, costing $' + str(paint_money_spent))
    
    
    print('How many 500cts of googly eyes would you like to order? You have $' + str(money) + ' left in your account.')
    eyes = ask()
    discount = (int(eyes) - 1)*8
    if discount > 32:
        discount = 32
    eyes_money_spent = int(eyes) * (2.99-(2.99*(discount/100))) # this looks confusing, but it isn't.
    eyes_money_spent = round(eyes_money_spent,2)
    money -= eyes_money_spent
    print('Order complete, costing $' + str(eyes_money_spent))
    t.sleep(2)
    


def pay_the_bank():
    global money, per_month_payment, credit_score, payments_remaining, bad_person_per_month_payment
    print('You need to pay $' + str(per_month_payment) + ' this month. Would you like to pay it? (y/n)')
    if ask() == 'y':
        money -= per_month_payment
        print('You\'ve paid the bank!')
        if r.randint(1,2) == 1:
            if credit_score < 10:
                credit_score += 1
        if payments_remaining > 1:
            payments_remaining -= 1
        bad_person_per_month_payment = per_month_payment
        if payments_remaining == 0:
            print('You have paid off your loan! Congratulations!')
    else:
        print('You have neglected to pay the bank. Your reliability goes down.')
        if credit_score > 1:
            credit_score -= 1
        bad_person_per_month_payment = bad_person_per_month_payment + per_month_payment

def manufacture():
    global machinery_level
    answer = ''
    if first_manufacture:
        print('To expand your business, you need to invest in some things.')
        sleep(1)
        print('Factory ($1,200,000)')
        sleep(1)
        print('Machinery ($45,000)')
        sleep(1)
        print('Employees ($85k per employee)')
        
        if money < 45000 or payments_remaining > 0:
            print('You cannot take further action because you don\'t have enough money and are still paying back your previous loan')
            sleep(1)
            print('Returning to dashboard...')
            sleep(r.randint(1,3))
            dashboard()
        if money < 45000:
            print('You cannot take action because of insufficient funds.')
            print('Would you like to take out a loan? (y/n)')
            while answer != 'y' or 'answer' != 'n':
                answer = ask()
                if answer != 'y' or answer != 'n':
                    print('Not an answer.')
            if answer == 'y':
                print('What would you take out a loan for?')
                print('Factory (f) or Machinery (m)')


           while answer != 'f' or 'answer' != 'm':
                answer = ask()
                if answer != 'f' or answer != 'm':
                    print('Not an answer.')
           if answer == 'f':
                print('Requesting a loan for 4 years for $1,200,000')
                loan(48, 1200000)
                if credit_score > 1:
                    print('Factory purchased!')
                    print('Your business barely stays alive while your factory is being built.')

           if answer == 'm':
                print('Requesting a loan for 1 year for $45,000')
                loan(12,45000)
                print('Machinery purchased!')
                machinery_level = 1



def sell():
    pass
def expand():
    pass
def dashboard():
    print('Pay off loan (l)')
    print('Manufacture products (m)')
    print('Sell products (s)')
    print('Develop business (d)')
    answer = ask()
    if answer == 'l':
        pay_the_bank()
    if answer == 'm':
        manufacture()
    if answer == 's':
        sell()
    if answer == 'd':
        expand()