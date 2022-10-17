from random import randint
from random import uniform
from participant import participantData
import strings

# Dynamic data classes
playerData = participantData
aiData = participantData

# Internal Game Vars
goalAmount = 21
drawAnotherCard = ""
playAgain = ""
gameEnded = False
roundEnded = False
totalBet = 0
firstDraw = True
firstGame = True
aiBetP = 0.2
startC = 1000

# ------------------------------------------------
# ----------------- Main Program -----------------
# ------------------------------------------------
#
# Function where we convert randomised 'card' from the last function into it's value based on standard blackjack rules
#
# (1) 2 through 10 count at face value, i.e. a 2 counts as two, a 9 counts as nine.
# (2) Face cards (J,Q,K) count as 10.
# (3) Ace can count as a 1 or an 11 depending on which value helps the hand the most. (At the moment the game only uses 1)
#
# Source: https://www.blackjackapprenticeship.com/how-to-play-blackjack/
#
faceCards = [11, 12, 13, 24, 25, 26, 37, 38, 39, 50, 51, 52]
aceCards = [1, 14, 27, 40]

def IntToCard(var):
    global faceCards
    global aceCards
    
    if (var >= 2 and var <= 10):
        var = var
    elif (var >= 15 and var <= 23):
        var = var - 13
    elif (var >= 28 and var <= 36):
        var = var - 13 * 2
    elif (var >= 41 and var <= 49):
        var = var - 13 * 3
    elif (faceCards.__contains__(var)):
        var = 10
    elif (aceCards.__contains__(var)):
        var = 1
    else:
        var = 2
        raise Exception(strings.integerException)
    return var

# Function where we draw a random card. Each card from a suit corresponds to a number between 1 and 52. 52 being the amount of cards in a standard deck of cards.
#
# (1) cards that are 2 through 10 correspond to 2-10, 15-23, 28-36, 41-49
# (2) Face cards (J,Q,K) correspond to 11, 12, 13, 24, 25, 26, 37, 38, 39, 50, 51, 52
# (3) Aces correspond to 1, 14, 27 and 40
#
# Takes in inputs on who drew a card and a special flag for wether to give the AI a little boost :)
def DrawCard(ai = False, player = False, aiSpecial = False):
    global playerData
    global aiData
    global goalAmount
    fatal = False
    
    # Logic for the Player
    if (player == True):
        playerData.drawnCardValue = randint(1,52)
        playerData.drawnCardValue = IntToCard(playerData.drawnCardValue)
        playerData.cardValue += playerData.drawnCardValue
        playerData.drewCard = True
        if (playerData.cardValue > goalAmount):
            fatal = True
    else:
        playerData.drewCard = False
    # Logic for the AI
    if (ai == True):
        aiData.drawnCardValue = randint(1,52)
        aiData.drawnCardValue = IntToCard(aiData.drawnCardValue)
        if (aiSpecial and ((aiData.cardValue + aiData.drawnCardValue) > goalAmount)):
            r = randint(1,6)
            if (r < 5):
                r = 1
            else:
                r = 2
            aiData.drawnCardValue = r
        aiData.cardValue += aiData.drawnCardValue
        aiData.drewCard = True
        if (aiData.cardValue > goalAmount):
            fatal = True
    else:
        aiData.drewCard = False
    
    # If either the Player or AI went above the goal amount the game ends
    # has to be done here so both of them still get their cards and they display correctly in the game results screen
    if (fatal == True):
        GameResults(True)

# Function where we handle the game results or ending state based on various rules and definitions
def GameResults(showStateInfo = False):
    global roundEnded
    global gameEnded
    global playerData
    global aiData
    global playAgain
    global firstDraw

    # Round ending logic, what information to display and new game prompt display 
    # if the player or AI hasn't lost all of their money yet
    roundEnded = True
    # Lose conditions
    if (playerData.cardValue > goalAmount or (playerData.cardValue < aiData.cardValue and aiData.cardValue <= goalAmount)):
        playerData.currency -= int(playerData.bet)
        aiData.currency += int(playerData.bet)
        if (showStateInfo):
            if (playerData.drewCard):
                print(strings.yourCard.format(playerData.drawnCardValue, playerData.cardValue), strings.goalPast.format(goalAmount))
            else:
                print(strings.yourCardStand.format(playerData.cardValue), strings.goalPast.format(goalAmount))
            if (aiData.drewCard):
                print(strings.opponentsCard.format(aiData.drawnCardValue, aiData.cardValue))
            else:
                print(strings.opponentsCardStand.format(aiData.cardValue))
        else:
            print(strings.yourCardVal.format(playerData.cardValue), strings.goalPast.format(goalAmount))
            print(strings.opponentsCardVal.format(aiData.cardValue))
        print(strings.loseText.format(playerData.bet))
    # Victory conditions
    elif ((playerData.cardValue > aiData.cardValue and playerData.cardValue <= goalAmount) or aiData.cardValue > goalAmount):
        playerData.currency += aiData.bet
        aiData.currency -= aiData.bet
        if (showStateInfo):
            if (playerData.drewCard):
                print(strings.yourCard.format(playerData.drawnCardValue, playerData.cardValue), strings.goalPast.format(goalAmount))
            else:
                print(strings.yourCardStand.format(playerData.cardValue), strings.goalPast.format(goalAmount))
            if (aiData.drewCard):
                print(strings.opponentsCard.format(aiData.drawnCardValue, aiData.cardValue))
            else:
                print(strings.opponentsCardStand.format(aiData.cardValue))
        else:
            print(strings.yourCardVal.format(playerData.cardValue), strings.goalPast.format(goalAmount))
            print(strings.opponentsCardVal.format(aiData.cardValue))
        print(strings.victoryText.format(aiData.bet))
    # Draw conditions
    elif (playerData.cardValue == aiData.cardValue):
        if (showStateInfo):
            if (playerData.drewCard):
                print(strings.yourCard.format(playerData.drawnCardValue, playerData.cardValue), strings.goalPast.format(goalAmount))
            else:
                print(strings.yourCardStand.format(playerData.cardValue), strings.goalPast.format(goalAmount))
            if (aiData.drewCard):
                print(strings.opponentsCard.format(aiData.drawnCardValue, aiData.cardValue))
            else:
                print(strings.opponentsCardStand.format(aiData.cardValue))
        else:
            print(strings.yourCardVal.format(playerData.cardValue), strings.goalPast.format(goalAmount))
            print(strings.opponentsCardVal.format(aiData.cardValue))
        print(strings.drawText.format(playerData.bet))
    # And in-case something goes wrong of course
    else:
        print(strings.undefined)

    # Handle all money lost aka game end state, if either one of you run out of money that's the end of the game :)
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

    # If the whole game hasn't ended ask for a new round
    if (gameEnded == False):
        startNewGame = False
        while (startNewGame == False):
            playAgain = input(strings.tryAgain.format(playerData.currency, aiData.currency))
            if (strings.yesses.__contains__(playAgain)):
                startNewGame = True
                Start()
            elif (strings.nos.__contains__(playAgain)):
                startNewGame = True
                print(strings.thxForPlaying)
            else:
                print(strings.invalid)
                startNewGame = False

# Function that makes sure you input an int, otherwise it just keeps asking for
# the user to re-input their answer
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

# Function where we set the bet of the AI and Player
def SetBet():
    global playerData
    global aiData
    global totalBet

    print(strings.askForBet.format(playerData.currency))

    # Clamp the players bet to max currency they have if it exceeds it
    pbet = InputInt()
    if (pbet > playerData.currency):
        playerData.bet = playerData.currency
    # The AI's bet is handled by this logic. First we set the maximum.
    # formula: [ p + c * m ] where p is players bet, c is AI's currency and m is the maximum percent the AI can take 
    # of their currency which is randomly chosen between 5% and the configure maximum
    # After that theres a random 80% chance that we apply an additional value to the maximum,
    # this being c * 0.85 + 30, where the c is the AI's currency
    aiMaxBet = playerData.bet + (aiData.currency * round(uniform(0.05, aiData.maxBetPercent), 2))
    r = randint(1,100)
    if (r > 20):
        aiMaxBet + round(aiData.currency * 0.85) + 30
    
    aiMaxBet = round(aiMaxBet)
    # The minimum bet is just 85% of what the player used
    aiMinBet = playerData.bet * 0.85
    aiMinBet = round(aiMinBet)
    aiData.bet = randint(aiMinBet, aiMaxBet)
    print(aiMinBet,aiMaxBet)
    # In-case the bet is more than available currency, clamp it back to the max amount of currency available
    if (aiData.bet > aiData.currency):
        aiData.bet = aiData.currency
    # Calculate the total combined bet
    totalBet = playerData.bet + aiData.bet
    print(strings.betSet.format(aiData.bet, totalBet))

# Function that runs through every turn to ensure that either we move to the game results state or to a new turn
def GameState():
    global firstDraw
    global drawAnotherCard
    global goalAmount
    global playerData
    global aiData

    # Are we drawing the first cards? If so display the corresponding prompt
    # else just display the normal prompt choosing between two versions for wether the participant 
    # drew a card last round or not
    if (firstDraw == True):
        print(strings.firstDraw.format(playerData.drawnCardValue), strings.whatAreWeWorkingToward.format(goalAmount))
        print(strings.opponentFirstDraw.format(aiData.drawnCardValue))
        firstDraw = False
    else:
        if (playerData.drewCard):
            print(strings.gsCardDrawn.format(playerData.drawnCardValue, playerData.cardValue), strings.whatAreWeWorkingToward.format(goalAmount))
        else:
            print(strings.gsCardDrawnStand.format(playerData.cardValue), strings.whatAreWeWorkingToward.format(goalAmount))
        if (aiData.drewCard):
            print(strings.gsOpCardDrawn.format(aiData.drawnCardValue, aiData.cardValue))
        else:
            print(strings.gsOpCardDrawnStand.format(aiData.cardValue))

    # Loop that checks for wether the user wants to draw a new card or not this round
    # also handles the various choices the AI might make depending on the state of the game
    advance = False
    while (advance == False):
        drawAnotherCard = input(strings.drawAgain)
        # User has decided to draw a card
        # Contains possible choices the AI might make depending on certain factors or random values
        if (strings.yesses.__contains__(drawAnotherCard)):
            advance = True
            if (aiData.cardValue < playerData.cardValue):
                DrawCard(True, True)
            elif (aiData.cardValue > 9 and aiData.cardValue > playerData.cardValue):
                r = randint(1,100)
                if (r > 40):
                    DrawCard(False, True)
                else:
                    DrawCard(True, True)
            # Let's check if the AI is losing but really close to the goal amount, in which case we
            # give the AI a chance to only roll 1 or 2 giving it a slight advantage over the player
            elif (aiData.cardValue > 16 and aiData.cardValue < playerData.cardValue):
                r = randint(1,100)
                if (r > 20):
                    DrawCard(True, True, True)
                else:
                    DrawCard(True, True)
            else:
                DrawCard(True, True)
        # User has decided not to draw a card
        # Contains possible choices the AI might make depending on certain factors or random values
        # Might lead straight to the end results
        elif (strings.nos.__contains__(drawAnotherCard)):
            advance = True
            if (aiData.cardValue < 11 and aiData.cardValue < playerData.cardValue):
                DrawCard(True, False)
            elif (aiData.cardValue < 16 and aiData.cardValue < playerData.cardValue):
                r = randint(1,100)
                if (r > 10):
                    DrawCard(True, False)
                else:
                    playerData.drewCard = False
                    aiData.drewCard = False
                    GameResults()
            elif (aiData.cardValue < 16 and aiData.cardValue == playerData.cardValue):
                r = randint(1,100)
                if (r > 50):
                    DrawCard(True, False)
                else:
                    playerData.drewCard = False
                    aiData.drewCard = False
                    GameResults()
            else:
                playerData.drewCard = False
                aiData.drewCard = False
                GameResults()
        else:
            # Handling in-case nothing matches expected results
            print(strings.invalid)
            playerData.drewCard = False
            aiData.drewCard = False
            GameResults()

# The main function that calls the game state as long as the round is still going
def Main():
    while (roundEnded == False):
        GameState()

# Function that loads the configurable options from the strings.py file
def SetConfig():
    global goalAmount
    global aiBetP
    global startC
    goalAmount = int(strings.configs[0])
    startC = int(strings.configs[1])
    aiBetP = strings.configs[2]

# Start function that runs when we 'start the game'.
# Calls other functions like SetConfig and SetBet and DrawCard for the first time
# Sets various global flags to determine later on if we are running a fresh game or new round
def Start():
    global firstDraw
    global playerData
    global aiData
    global roundEnded
    global gameEnded
    global firstGame

    SetConfig()

    # If running the game for the first time, initialize the participants data classes
    # else just reset them
    if (firstGame):
        playerData = participantData(startC, aiBetP)
        aiData = participantData(startC, aiBetP)
        firstGame = False
    else:
        playerData.Reset()
        aiData.Reset()

    roundEnded = False
    gameEnded = False
    firstDraw = True
    SetBet()
    DrawCard(True, True)

# Main structure of the cardgame.py program
Start()
Main()