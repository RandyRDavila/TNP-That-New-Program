from pyfiglet import figlet_format
from halo import Halo
import time
from datetime import datetime, timedelta
import pygame
#from functions.get_conjectures import get_conjectures, remove_duplicates
import pickle
from main import *


__version__ = '0.0.1'

def main():
    print(figlet_format('TNP', font='slant'))
    #print(figlet_format(' - LIGHT', font='slant'))
    print('Version ' + __version__)
    print('Copyright ' + u'\u00a9' + ' 2019 Randy Davila')
    print()

    print()
    invariant = input('Invariant: ')
    print()


    print()
    print(figlet_format('TNP', font='slant'))
    #print(figlet_format(' - LIGHT', font='slant'))

    print('Version ' + __version__)
    print('Copyright ' + u'\u00a9' + ' 2019 Randy Davila')
    print()

    U = []
    L = []
    for x in make_conjectures(invariant):
        if x.inequality == ' <= ':
            U.append(x)
        else:
            L.append(x)
    

    print('Upper Bounds')
    for i in range(1, 15):
        print(f'Conjecture {i}. {U[i]}')
        print('')
    print()
    print('Lower Bounds')
    for i in range(1, 15):
        print(f'Conjecture {i}. {L[i]}')
        print('')
    print()

    
    return 0


if __name__ == '__main__':
    main()