import pyttsx3
import pandas as pd
import numpy as np
import click
import sys
import os

wds = pd.read_csv('words.csv',index_col = 'word')
en = pyttsx3.init()
en.setProperty('rate',100)

#for ea in wds.index:
#    en.say(ea)
#    en.runAndWait()
#    sp = input("spell: ")
#    if sp == ea:
#        print("Right!")
#        wds.loc[ea,'score']+=.05
#    else:
#        wds.loc[ea,'score']-=.05
lrate = 0.05
while(1):
    try:
        os.system('cls')
#        os.system('clear') #for linux
        wd = np.random.choice(wds.index,p=wds.score)
        en.say(wd)
        en.runAndWait()
        sp = input("Spell2: ")
        if sp == wd:
            wds.loc[wd,'right'] += 1
            print("Right!")
        else:
            wds.loc[wd,'right'] -= 1
            print("Wrong :(\n Ans:{ea} ")
            pb = wds.loc[wd,'score']
            wds['score'] -= lrate/(len(wds)-1)
            wds.loc[wd,'score'] = pb + lrate 
    except KeyboardInterrupt:
        wds.to_csv('words.csv')
        print("Shutdown requested...exiting")
        sys.exit(0)
#    except Exception:
#        traceback.print_exc(file=sys.stdout)
