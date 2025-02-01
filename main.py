import rich, os, random, length, json, sys
from rich import print as rprint
def wordGen():
    global word
    global letter3, letter1, letter2, letter4, letter5, trycounter, wordsList
    with open('words.json', 'r') as file:
        wordsList = json.load(file)
    word = random.choice(data['words'])
    print(word)
    letter1, letter2, letter3, letter4, letter5 = word
    trycounter = 0
def wordCheck(Guess):
    global trycounter
    if len(Guess) == 5:
        if Guess == word:
            trycounter = trycounter + 1
            rprint("[green]Good Job! You guessed the word in ", trycounter, " tries!")
            print("🟩🟩🟩🟩🟩")
        elif Guess in wordsList['words']:
            trycounter = trycounter + 1
            ## 0 = Not in word, 1 = In word, wrong spot, 2 = In right spot ##
            rprint("[yellow]Incorrect Word.")
            ## breaks down into letters ##
            guessl1, guessl2, guessl3, guessl4, guessl5 = Guess
            #LETTER1
            if guessl1 == letter1:
                #L1HINT = 2
                L1HINT = "🟩"
            elif guessl1 == letter2 or guessl1 == letter3 or guessl1 == letter4 or guessl1 == letter5:
                L1HINT = "🟨"
            else:
                L1HINT = "⬜"
            #LETTER2
            if guessl2 == letter2:
                L2HINT = "🟩"
            elif guessl2 == letter1 or guessl2 == letter3 or guessl2 == letter4 or guessl2 == letter5:
                L2HINT = "🟨"
            else:
                L2HINT = "⬜"
            #LETTER3
            if guessl3 == letter3:
                L3HINT = "🟩"
            elif guessl3 == letter1 or guessl3 == letter2 or guessl3 == letter4 or guessl3 == letter5:
                L3HINT = "🟨"
            else:
                L3HINT = "⬜"
            #LETTER4
            if guessl4 == letter4:
                L4HINT = "🟩"
            elif guessl4 == letter1 or guessl4 == letter2 or guessl4 == letter3 or guessl4 == letter5:
                L4HINT = "🟨"
            else:
                L4HINT = "⬜"
            #LETTER5
            if guessl5 == letter5:
                L5HINT = "🟩"
            elif guessl5 == letter1 or guessl5 == letter2 or guessl5 == letter4 or guessl5 == letter3:
                L5HINT = "🟨"
            else:
                L5HINT = "⬜"
            print(L1HINT, L2HINT, L3HINT, L4HINT, L5HINT)
            if trycounter == 1:
                try1answer = L1HINT + L2HINT + L3HINT + L4HINT + L5HINT
            elif trycounter == 2:
                try2answer = L1HINT + L2HINT + L3HINT + L4HINT + L5HINT
            elif trycounter == 3:
                try3answer = L1HINT + L2HINT + L3HINT + L4HINT + L5HINT
            elif trycounter == 4:
                try4answer = L1HINT + L2HINT + L3HINT + L4HINT + L5HINT
            elif trycounter == 5:
                try5answer = L1HINT + L2HINT + L3HINT + L4HINT + L5HINT
            else:
                rprint("[red]Error! You have surpassed the 5 try limit. Quiting Program...")
                sys.exit()
        else:
            print("Not in word list.")
    else:
        rprint("[red]Please enter a valid, 5 letter word.")
with open('words.json', 'r') as file:
    data = json.load(file)
word = random.choice(data['words'])


wordGen()
print(word)
print(letter3)
while trycounter <= 5:
    Relations = input("Guess!")
    wordCheck(Relations)
print("Ran out of guesses.")
print("The word was ", word, ".")
