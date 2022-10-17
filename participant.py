# Class that contains all of the dynamic data used by cardgame.py for it's players
class participantData:
    cardValue = 0
    currency = 0
    currencyBet = 0
    bet = ""
    drawnCardValue = 0
    maxBetPercent = 0
    drewCard = bool
    
    # Initialization function that just wipes everything
    def __init__(self, startingCurrency = 1000, maxBetPercent = 0.2):
        self.cardValue = 0
        self.currency += startingCurrency
        self.currencyBet = 0
        self.bet = ""
        self.drawnCardValue = 0
        self.maxBetPercent = maxBetPercent
        self.drewCard = True
    
    # Seperate reset function that only wipes the necessary stuff when starting a new match
    # for when you need to keep earned currency and such
    def Reset(self):
        self.cardValue = 0
        self.currencyBet = 0
        self.bet = 0
        self.drawnCardValue = 0
        self.drewCard = True