'''change.py'''
import math

def make_change(change, denominations):
    '''takes a list of denominations and an amount to make change out of. Returns the leftover change'''
    for amount in denominations:
        result = int(change // amount[1])
        if result > 0: print amount[0] , ':' , str(result)
        change = change % amount[1]
    return change

dollars = [['Hundreds', 100], ['Fifties', 50], ['Twenties', 20], ['Tens', 10], ['Fives',5], ['Ones',1]]
cents = [['Quarters', 25], ['Dimes', 10], ['Nickels', 5], ['Pennies', 1]]

if __name__ == '__main__':

    change = -1 * (input("What's the cost in dollars? ") - input("What's the amount of dollars given? ")) # get the change required
    if change < 0:
        print "The customer owes you", -change

    else:
        print "You owe the customer", change, "\n---------"
        # calculate whole dollar amounts 
        change = make_change(change, dollars)
        # convert remainder to whole cents and calculate
        change = int(math.floor(change * 100 + .5))
        make_change(change, cents)
