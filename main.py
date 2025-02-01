import rich, os, random, length
from rich import print as rprint
def wordGen():
    global Word
    global letter3, letter1, letter2, letter4, letter5, trycounter
    Word = random.choice(wordsList)
    letter1, letter2, letter3, letter4, letter5 = Word
    trycounter = 0
def wordCheck(Guess):
    global trycounter
    if len(Guess) == 5:
        if Guess == Word:
            trycounter = trycounter + 1
            rprint("[green]Good Job! You guessed the word in ", trycounter, " tries!")
            print("🟩🟩🟩🟩🟩")
        elif Guess in wordsList:
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
            print(L1HINT, L2HINT)
            print(wordsList)
        else:
            print("Not in word list.")
        
            
         
            
    else:
        rprint("[red]Please enter a valid, 5 letter word.")
wordsList = ["ABCDF", "BACDF", "FCDFA"]

wordGen()
print(Word)
print(letter3)
while trycounter <= 5:
    Relations = input("Guess!")
    wordCheck(Relations)
print("failure")