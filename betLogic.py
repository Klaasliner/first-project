#!/usr/bin/python

class Betting:
    def __init__(self,stake,odds,total):
        self.stake: float = stake
        self.odds: float = odds
        self.total: float = total
        self.payout: float = 0
        self.hold: int = 10
        self.start: float = total
        self.max_payout: int = 1e6 
        self.firstBet()

    def firstBet(self)->float:
        if self.total >= self.stake:
            self.total -= self.stake
        else:
            print("you don't enough cash to wager!!!")
            return exit(0)
    def calcPayout(self)->float:
        self.payout = round(self.stake*self.odds,2)
        return self.payout
    def makeStake(self)->float:
        self.stake = self.payout
        self.stake += self.total
        if self.stake >= self.hold+1:
            self.stakeBefore()
        else:
            if(self.stake >= 0.5*self.hold+1):
                if self.total < 0.4*self.hold:
                    self.stake %= 0.5*self.hold
                else:
                    self.stake -= self.total
            else:
                self.stake = self.payout
        return round(self.stake,2)
    def stakeBefore(self)->None:
        if self.stake >= 5*self.hold+1:
            if(self.total < 4*self.hold):
                self.stake %= 5*self.hold
            else:
                self.stake = self.payout
        elif self.stake >= 4*self.hold+1:
            if self.total < 2.5*self.hold:
                self.stake %= 4*self.hold
            else:
                self.stake %= 2.5*self.hold
        elif self.stake >= 2.5*self.hold+1:
            if self.total < 2*self.hold:
                self.stake %= 2.5*self.hold
            else:
                self.stake -= self.total 
        elif self.stake >= 2*self.hold+1:
            self.stake %= 2*self.hold
        elif self.stake >= self.hold+1:
            if self.total < self.hold:
                self.stake %= self.hold
            else:
                self.stake = self.payout
            
    def calcStake(self)->float:
        self.findHold()
        if self.checkPayout() == True:
            self.makeStake()
        else:
            self.stake = self.payout % 100000
        self.stake = round(self.stake,2)
        return self.stake

    def findHold(self)->int:
        if self.total < self.max_payout:
            if self.total >= 4*self.hold:
                self.hold *= round(10,2)
        else:
            self.hold = 1e4
        self.hold = round(self.hold)
        return self.hold

    def calcSaving(self)->float:
        self.saving = round(self.payout - self.stake,2)
        if self.saving < 1:
            self.saving = 0
        return self.saving
    
    def calcTotal(self)->float:
        self.total += round(self.saving,2)
        return self.total
    def checkPayout(self)->bool:
        validity =  self.calcPayout() <= self.max_payout
        return validity
