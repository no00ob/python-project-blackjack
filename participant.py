class participantData:
    cardValue = 0
    currency = 0
    currencyBet = 0
    bet = ""
    drawnCardValue = 0
    maxBetPercent = 0
    
    def __init__(self, startingCurrency = 1000, maxBetPercent = 0.2):
        self.cardValue = 0
        self.currency = startingCurrency
        self.currencyBet = 0
        self.bet = ""
        self.drawnCardValue = 0
        self.maxBetPercent = maxBetPercent