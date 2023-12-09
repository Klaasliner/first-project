#!/usr/bin/python

from betLogic import Betting
from sys import argv

stake : float = float(argv[1])
odds : float = float(argv[2])
total : float = float(argv[3])
days : int = int(argv[4])
myBet = Betting(stake,odds,total)
count = 1
while days:
    if total >= stake:
        myBet.calcPayout()
        print("ticket: %d\t\tHolder: R%.2f"%(count,myBet.hold))
        if myBet.stake < 10000:
            print("Stake: R%.2f\t\tPayout: R%.2f"%(myBet.stake,myBet.payout))
        else:
            print("Stake: R%.2f\tPayout: R%.2f"%(myBet.stake,myBet.payout))
        if days == 1:
            myBet.stake = 0
        else:
            myBet.calcStake()
        myBet.calcSaving()
        myBet.calcTotal()
        total_before = myBet.total - myBet.saving
        if total_before < 900:
            print("before: R%.2f\t\tsaving: R%.2f\nafter: R%.2f\n"%(myBet.total-myBet.saving,myBet.saving,myBet.total))
        else:
            print("before: R%.2f\tsaving: R%.2f\nafter: R%.2f\n"%(total_before,myBet.saving,myBet.total))
    days -= 1
    count += 1
print("R%.2f @ R%.2f/day for %d days\n"%(myBet.total,myBet.total /(count-1),count-1))
