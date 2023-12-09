# first-project
name: BetMatrix

this is a passion project designed to simulate how much a gambler could make if they were to bet on a certain odds for a certain period of time with the outcome implied to be a win, then returning an certain total at the end of that period.

Components:
   betLogic(Betting)
     This is a class/module that is
     responsible for computing the
     stake/wager amount(from the
     second to last one, the first one
     is taken from user input), 
     the payout, the amount to be
     saved(called saving), the
     user's balance(called total).
     Methods:
        calcStake : float
           computes and returns
           stake/wager.
        calcSaving: float
           computes and returns saving
        calcPayout: float
           computes and returns payout
        calcTotal: float
           computes and returns total

   betAnalyser
      this module is a the one that visualises the payouts, stakes, and othe computed variables.
   
