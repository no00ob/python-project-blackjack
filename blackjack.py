from random import randint
from participant import participantData
import strings
import json

# C# to Python ease of use
false = False
true = True

playerData = participantData()
aiData = participantData()

# Internal Game Vars
goalAmount = 21
drawAnotherCard = ""
playAgain = ""
gameEnded = False
roundEnded = False
totalBet = 0
firstDraw = True

# ------------------------------------------------
# ----------------- Main Program -----------------
# ------------------------------------------------
#
# Function where we convert randomised 'card' from the last function into it's value based on blackjack rules
#
# (1) 2 through 10 count at face value, i.e. a 2 counts as two, a 9 counts as nine.
# (2) Face cards (J,Q,K) count as 10.
# (3) Ace can count as a 1 or an 11 depending on which value helps the hand the most. (At the moment the game only uses 1)
#
# Source: https://www.blackjackapprenticeship.com/how-to-play-blackjack/
#
def IntToCard(var):
    if (var == 1 or var == 14 or var == 27 or var == 40):
        var = 1
    elif (var >= 2 and var <= 10):
        var = var
    elif (var >= 15 and var <= 23):
        var = var - 13
    elif (var >= 28 and var <= 36):
        var = var - 13 * 2
    elif (var >= 41 and var <= 49):
        var = var - 13 * 3
    return var

# Function where we draw a random card. Each card from a suit corresponds to a number between 1 and 52. 52 being the amount of cards in a standard deck of cards.
#
# (1) cards that are 2 through 10 correspond to 2-10, 15-23, 28-36, 41-49
# (2) Face cards (J,Q,K) correspond to 11, 12, 13, 24, 25, 26, 37, 38, 39, 50, 51, 52
# (3) Aces correspond to 1, 14, 27 and 40
#
def DrawCard():
    global playerData
    global aiData
    global goalAmount

    # Player
    playerData.drawnCardValue = randint(1,52)
    playerData.drawnCardValue = IntToCard(playerData.drawnCardValue)
    playerData.cardValue += playerData.drawnCardValue
    if (playerData.cardValue > goalAmount):
        GameResults(True)
    # AI
    aiData.drawnCardValue = randint(1,52)
    aiData.drawnCardValue = IntToCard(aiData.drawnCardValue)
    aiData.cardValue += aiData.drawnCardValue
    if (aiData.cardValue > goalAmount):
        GameResults(True)
    

def GameResults(showStateInfo = False):
    global roundEnded
    global gameEnded
    global playerData
    global aiData
    global playAgain
    global firstDraw

    roundEnded = True
    if (playerData.cardValue > goalAmount or (playerData.cardValue < aiData.cardValue and aiData.cardValue <= goalAmount)):
        playerData.currency -= int(playerData.bet)
        aiData.currency += aiData.bet + int(playerData.bet)
        if (showStateInfo):
            print(strings.yourCard.format(playerData.drawnCardValue, playerData.cardValue), strings.whatAreWeWorkingToward.format(goalAmount))
            print(strings.opponentsCard.format(aiData.drawnCardValue, aiData.cardValue))
        else:
            print(strings.yourCardVal.format(playerData.cardValue), strings.whatAreWeWorkingToward.format(goalAmount))
            print(strings.opponentsCardVal.format(aiData.cardValue))
        print(strings.loseText.format(totalBet))
    elif ((playerData.cardValue > aiData.cardValue and playerData.cardValue <= goalAmount) or aiData.cardValue > goalAmount):
        playerData.currency += totalBet
        aiData.currency -= aiData.bet
        if (showStateInfo):
            print(strings.yourCard.format(playerData.drawnCardValue, playerData.cardValue), strings.whatAreWeWorkingToward.format(goalAmount))
            print(strings.opponentsCard.format(aiData.drawnCardValue, aiData.cardValue))
        else:
            print(strings.yourCardVal.format(playerData.cardValue), strings.whatAreWeWorkingToward.format(goalAmount))
            print(strings.opponentsCardVal.format(aiData.cardValue))
        print(strings.victoryText.format(totalBet))
    else:
        print(strings.undefined)

    if (playerData.currency <= 0):
        playerData.currency = 0
        print(strings.youLostAllMoney.format(playerData.currency))
        gameEnded = True
    elif (aiData.currency <= 0):
        aiData.currency = 0
        print(strings.opponentBroke)
        gameEnded = True
    else:
        gameEnded = False

    if (gameEnded == False):
        playAgain = input(strings.tryAgain.format(playerData.currency, aiData.currency))
        startNewGame = False
        while (startNewGame == False):
            if (strings.yesses.__contains__(playAgain)):
                startNewGame = True
                Start()
            elif (strings.nos.__contains__(playAgain)):
                startNewGame = True
                print(strings.thxForPlaying)
            else:
                print(strings.invalid)

def InputInt(msg = ""):
    while True:
        try:
            if (msg == ""):
                result = int(input())
            else:
                result = int(input(msg))
            break
        except:
            print(strings.invalid)
    return result

def SetBet():
    global playerData
    global aiData
    global totalBet

    print(strings.askForBet.format(playerData.currency))

    playerData.bet = InputInt()
    aiMaxBet = playerData.bet + (aiData.currency * aiData.maxBetPercent)
    aiMaxBet = round(aiMaxBet)
    aiMinBet = playerData.bet
    aiData.bet = randint(aiMinBet, aiMaxBet)
    if (aiData.bet > aiData.currency):
        aiData.bet = aiData.currency
    totalBet = playerData.bet + aiData.bet
    print(strings.betSet.format(aiData.bet, totalBet))

def GameState():
    global firstDraw
    global drawAnotherCard
    global goalAmount
    global playerData

    if (firstDraw == True):
        print(strings.firstDraw.format(playerData.drawnCardValue), strings.whatAreWeWorkingToward.format(goalAmount))
        print(strings.opponentFirstDraw.format(aiData.drawnCardValue))
        firstDraw = False
    else:
        print(strings.gsCardDrawn.format(playerData.drawnCardValue, playerData.cardValue), strings.whatAreWeWorkingToward.format(goalAmount))
        print(strings.gsOpCardDrawn.format(aiData.drawnCardValue, aiData.cardValue))

    advance = False
    while (advance == False):
        drawAnotherCard = input(strings.drawAgain)
        if (strings.yesses.__contains__(drawAnotherCard)):
            advance = True
            DrawCard()
        elif (strings.nos.__contains__(drawAnotherCard)):
            advance = True
            GameResults()
        else:
            print(strings.invalid)

def Main(args = ""):
    while (roundEnded == False):
        GameState()
        
def Start():
    global firstDraw
    global playerData
    global aiData
    global roundEnded
    global gameEnded

    playerData = participantData()
    aiData = participantData()

    roundEnded = False
    gameEnded = False
    firstDraw = True
    SetBet()
    DrawCard()

Start()
Main()