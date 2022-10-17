import json

# List where we keep all possible translations and list with all of the other numerical values from the config file.
# The config numbers are read and accessed from this file by cardgame.py because it's easy to save them in here at the same time
# whilst we read the translations from the config file.
translations = []
configs = [0.0, 0.0, 0.0]

# All of the global strings accessed by cardgame.py
victoryText = ""
loseText = ""
drawText = ""
tryAgain = ""
youLostAllMoney = ""
askForBet = ""
firstDraw  = ""
whatAreWeWorkingToward = ""
goalPast = ""
drawAgain = ""
invalid = ""
yesses = ""
nos = ""
thxForPlaying = ""
betSet = ""
opponentFirstDraw = ""
opponentBroke = ""
yourCard = ""
yourCardStand = ""
opponentsCard = ""
opponentsCardStand = ""
yourCardVal = ""
opponentsCardVal = ""
undefined = ""
gsCardDrawn = ""
gsCardDrawnStand = ""
gsOpCardDrawn = ""
gsOpCardDrawnStand = ""
integerException = ""

# Function that loads all translations from the translation dictionary obtained from the lang files 
# with their respective keys to the corresponding global variables defined just above.
def LoadTranslation(translationDict):
    global victoryText
    global loseText
    global drawText
    global tryAgain
    global youLostAllMoney
    global askForBet
    global firstDraw
    global whatAreWeWorkingToward
    global goalPast
    global drawAgain
    global invalid
    global yesses
    global nos
    global thxForPlaying
    global betSet
    global opponentFirstDraw
    global opponentBroke
    global yourCard
    global yourCardStand
    global opponentsCard
    global opponentsCardStand
    global yourCardVal
    global opponentsCardVal
    global undefined
    global gsCardDrawn
    global gsCardDrawnStand
    global gsOpCardDrawn
    global gsOpCardDrawnStand
    global integerException
    
    victoryText = translationDict["victory"]
    loseText = translationDict["loss"]
    drawText = translationDict["draw"]
    tryAgain = translationDict["newGame"]
    youLostAllMoney = translationDict["broke"]
    askForBet = translationDict["bet"]
    firstDraw = translationDict["firstDraw"]
    whatAreWeWorkingToward = translationDict["goal"]
    goalPast = translationDict["goalPast"]
    drawAgain = translationDict["newCard"]
    invalid = translationDict["invalid"]
    yesses = translationDict["yes"]
    nos = translationDict["no"]
    thxForPlaying = translationDict["thanks"]
    betSet = translationDict["betDone"]
    opponentFirstDraw = translationDict["otherFirstDraw"]
    opponentBroke = translationDict["otherBroke"]
    yourCard = translationDict["yourCard"]
    yourCardStand = translationDict["yourCardStand"]
    opponentsCard = translationDict["otherCard"]
    opponentsCardStand = translationDict["otherCardStand"]
    yourCardVal = translationDict["yourCardValue"]
    opponentsCardVal = translationDict["otherCardValue"]
    undefined = translationDict["undefined"]
    gsCardDrawn = translationDict["midYourCard"]
    gsCardDrawnStand = translationDict["midYourCardStand"]
    gsOpCardDrawn = translationDict["midOtherCard"]
    gsOpCardDrawnStand = translationDict["midOtherCardStand"]
    integerException = translationDict["integerException"]

# Function that chooses which translation dictionary from the translations list are we loading.
def SelectTranslation(index):
    global translations
    LoadTranslation(translations[index])

# Start function that runs when we 'start the game'.
# It loads all of the config file values and after that the defined translation files.
def Start():
    global translations
    # Open the config.json file and map it to a variable
    with open("config.json", "r") as configFile:
        # Load the json file
        configData = json.load(configFile)
        # Add all of the translations defined in the file to the languages list
        languages = configData["translations"]
        # Clear the config list
        configs.clear()
        # Append all of the numerical values from the config file
        configs.append(float(configData["goal"]))
        configs.append(float(configData["startingCurrency"]))
        configs.append(float(configData["maxBetPercentFromRemainingCurrency"]))
        # Loop through all of the language files and load their respective jsons and add the contents to the dictionary
        for lang in languages:
            # Open the {lang}.json with utf8 encoding to ensure stuff such as ä and € don't get lost
            with open("{0}.json".format(lang), "r", encoding='utf8') as langFile:
                translations.append(json.load(langFile))

# Main structure of the strings.py program
Start()
SelectTranslation(int(input("Select language (0 English US, 1 Finnish FI) ")))