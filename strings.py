import json

translations = []

victoryText = ""
loseText = ""
tryAgain = ""
youLostAllMoney = ""
askForBet = ""
firstDraw  = ""
whatAreWeWorkingToward = ""
drawAgain = ""
invalid = ""
yesses = ""
nos = ""
thxForPlaying = ""
betSet = ""
opponentFirstDraw = ""
opponentBroke = ""
yourCard = ""
opponentsCard = ""
yourCardVal = ""
opponentsCardVal = ""
undefined = ""
gsCardDrawn = ""
gsOpCardDrawn = ""
integerException = ""

# Functions
def LoadTranslation(translationDict):
    global victoryText
    global loseText
    global tryAgain
    global youLostAllMoney
    global askForBet
    global firstDraw
    global whatAreWeWorkingToward
    global drawAgain
    global invalid
    global yesses
    global nos
    global thxForPlaying
    global betSet
    global opponentFirstDraw
    global opponentBroke
    global yourCard
    global opponentsCard
    global yourCardVal
    global opponentsCardVal
    global undefined
    global gsCardDrawn
    global gsOpCardDrawn
    global integerException
    
    victoryText = translationDict["victory"]
    loseText = translationDict["loss"]
    tryAgain = translationDict["newGame"]
    youLostAllMoney = translationDict["broke"]
    askForBet = translationDict["bet"]
    firstDraw = translationDict["firstDraw"]
    whatAreWeWorkingToward = translationDict["goal"]
    drawAgain = translationDict["newCard"]
    invalid = translationDict["invalid"]
    yesses = translationDict["yes"]
    nos = translationDict["no"]
    thxForPlaying = translationDict["thanks"]
    betSet = translationDict["betDone"]
    opponentFirstDraw = translationDict["otherFirstDraw"]
    opponentBroke = translationDict["otherBroke"]
    yourCard = translationDict["yourCard"]
    opponentsCard = translationDict["otherCard"]
    yourCardVal = translationDict["yourCardValue"]
    opponentsCardVal = translationDict["otherCardValue"]
    undefined = translationDict["undefined"]
    gsCardDrawn = translationDict["midYourCard"]
    gsOpCardDrawn = translationDict["midOtherCard"]
    integerException = translationDict["integerException"]

def SelectTranslation(index):
    global translations
    LoadTranslation(translations[index])

def Start():
    global translations
    with open("config.json", "r") as configFile:
        configData = json.load(configFile)
        languages = configData["translations"]
        for lang in languages:
            with open("{0}.json".format(lang), "r") as langFile:
                translations.append(json.load(langFile))

# Program
Start()
SelectTranslation(int(input("Select language (0 English US, 1 Finnish FI) ")))