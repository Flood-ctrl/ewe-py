#!/usr/bin/env python3

import random
import sys
import codecs
import platform
import time

w = 'w'                                                                        # Vocabulary file
DELAY_TIME = 3                                                                 # Time (seconds) for delaying beetwen two words

# Cheking for OS type
if platform.system() == "Windows":
    TEXT_DECODING = "'utf-8'"
else:
    TEXT_DECODING = None

# Opeping w file for reading and decoding to cp1251 if OS is Windows like
try:
    with codecs.open(w , 'r', TEXT_DECODING) as wBase:
        wList = [line.strip() for line in wBase]
except FileNotFoundError:
    sys.exit("ERROR: File \"{}\" not found!".format(w))

'''try:
    eweCykChoice = input("Choose the type: ")[0]
except KeyboardInterrupt:
    sys.exit("Exit by KeyboardInterrupt!")
'''
eweCykChoice = 's'

# Case of choosed mode
def ewe_cyk_type(choice):
    try:
        return {
            's': 0, 
            'b': 1,
        }[choice]
    except KeyError:
        sys.exit("Wrong key choosed, "
        "choose only from \"s\" or \"b\".")

# ewe function
def ewe_func(func):
    EWE_TYPE = ewe_cyk_type(eweCykChoice)
    dejaVu = None                                                              # dejaVu is variable for excluding same strings in a row
    uniqueStrings = {}                                                         # uniqueStrings for avoiding of repeating more then 3 same strings in the cycle
    intelligent = 0                                                            # Counter for showing last 30 entrys first

    if EWE_TYPE == 0:
        W0 = 0
        W1 = 1
    else:
        W0 = 1
        W1 = 0
    
    for cycleItteration in range(0, 99):      
        if intelligent <= 29:
            beginString = len(wList) - 30
        else:
            beginString = 0

        wListStr = wList[random.randint(beginString , len(wList) - 1)]
        if str(dejaVu) == wListStr:
            cycleItteration -= 1
            continue
        else:
            dejaVu = wListStr
        
        if not wListStr in uniqueStrings:
            uniqueStrings[wListStr] = int(1)
        elif uniqueStrings[wListStr] >= int(3):
            cycleItteration -= 1
            continue
        else:
            uniqueStrings[wListStr] += int(1)
        
        intelligent += 1
        print((wListStr.split(' - ')[W0])  , end=" ", flush=True)
        print("- ", end="")
        time.sleep(DELAY_TIME)
        print((wListStr.split(' - ')[W1]))
        time.sleep(1)
        print("")

# ewe function with arguments equals eweCykChoice                
ewe_func(ewe_cyk_type(eweCykChoice))


'''
print(type(ewe_cyk_type(eweCykChoice)))

def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "nothing")
'''