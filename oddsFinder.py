#!/usr/bin/python

from betLogic import Betting
from sys import argv

stake : float = float(argv[1])
odds : float = float(argv[2])
total : float = float(argv[3])
days : int = int(argv[4])
minPayout : int = int(argv[5])
balances = []
myOdds = []
minOdds = 1.10
maxOdds = odds
odds = minOdds

while odds <= maxOdds:
    x_count = 1
    bet = Betting(stake,odds,total)
    while x_count<=days:
        bet.calcPayout()
        if x_count<days:
            bet.calcStake()
        else:
            bet.stake = 0
        bet.calcSaving()
        bet.calcTotal()
        x_count += 1
    else:
        if len(balances)>0:
            if bet.total >= minPayout:
                if bet.total >= balances[len(myOdds)-1]+(odds-myOdds[len(myOdds)-1])*1000: 
                    balances.append(bet.total)
                    myOdds.append(bet.odds)
        else:
            if bet.total >= minPayout:
                balances.append(bet.total)
                myOdds.append(bet.odds)
    odds += 0.01
else:
    print("stake: R%.2f\tbalance: R%.2f\n"%(stake,total))
    if len(balances)>0:
        for x in range(len(balances)):
            if x>=1:
                if balances[x] < 100000:
                    print("odds: %.2f\ttotal: %.2f\n\t\tdiff: %.2f\n"%(myOdds[x],balances[x],(balances[x]-balances[x-1])))
                else:
                    print("odds: %.2f\ttotal: %.2f\n\t\tdiff: %.2f\n"%(myOdds[x],balances[x],(balances[x]-balances[x-1])))
            else:
                print("odds: %.2f\ttotal:%.2f\n"%(myOdds[x],balances[x]))
    else:
        print("no odds from %.2f to %.2f make R%.2f in %d days"%(minOdds,maxOdds,minPayout,days))
print("\n")
