from pyfiglet import figlet_format
from halo import Halo
import time
from datetime import datetime, timedelta
import pygame
#from functions.get_conjectures import get_conjectures, remove_duplicates
import pickle
from main import *
from tnp.functions.Theo import Theo


__version__ = '0.0.1'

def main():
    print(figlet_format('Conjecture with TNP', font='slant'))
    #print(figlet_format(' - LIGHT', font='slant'))
    print('Version ' + __version__)
    print('Copyright ' + u'\u00a9' + ' 2019 Randy Davila')
    print()

    print()
    invariant = input('Invariant: ')
    print()


    print()
    print(figlet_format('Conjecture with TNP', font='slant'))
    #print(figlet_format(' - LIGHT', font='slant'))

    print('Version ' + __version__)
    print('Copyright ' + u'\u00a9' + ' 2019 Randy Davila')
    print()

    U = []
    L = []

    L1 = list(filter(None, make_conjectures_one(invariant)))
    L2 = list(filter(None, make_conjectures_two(invariant)))
    L3 = list(filter(None, make_conjectures_three(invariant)))
    for x in L1:
        if x.inequality == ' <= ':
            U.append(x)
        else:
            L.append(x)
    for x in L2:
        if x.inequality == ' <= ':
            U.append(x)
        else:
            L.append(x)

    for x in L3:
        if x.inequality == ' <= ':
            U.append(x)
        else:
            L.append(x)
    U, L = Theo(U), Theo(L)

    print('Upper Bounds')
    for i in range(1, 20):
        print(f'Conjecture {i}. {U[i]}')
        print('')
    print()
    print('Lower Bounds')
    for i in range(1, 20):
        print(f'Conjecture {i}. {L[i]}')
        print('')
    print()

    work = input('Remove conjectures? (y/n) ')
    while work == 'y':
        type = input('Upper or lower? (U/L) ')
        index = int(input('Conjecture label? '))
        if type == 'U':
            U.pop(index)
        else:
            L.pop(index)
        print('Upper Bounds')
        for i in range(1, 20):
            print(f'Conjecture {i}. {U[i]}')
            print('')
        print()
        print('Lower Bounds')
        for i in range(1, 20):
            print(f'Conjecture {i}. {L[i]}')
            print('')
        print()


    return 0


if __name__ == '__main__':
    main()
