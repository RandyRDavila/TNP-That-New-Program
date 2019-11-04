from pyfiglet import figlet_format
from halo import Halo
import time
from datetime import datetime, timedelta
import pygame
#from functions.get_conjectures import get_conjectures, remove_duplicates
import pickle
from main import *
from tnp.functions.Theo import Theo
from tnp.functions.get_conjectures import *


__version__ = '0.0.1'

valid_invariants = {1:'domination_number',
                    2:'total_domination_number',
                    3:'connected_domination_number',
                    4:'independence_number',
                    5:'power_domination_number',
                    6:'zero_forcing_number',
                    7:'matching_number', 
                    8:'harmonic_index',
                    9:'min_maximal_matching_number',
                    10:'independent_domination_number'}#,
                    #7:'total_zero_forcing_number',
                    #8:'connected_zero_forcing_number',
                    #9:'independent_domination_number',
                    #10:'chromatic_number',
                    #11:'matching_number',
                    #12:'min_maximal_matching_number',
                    #13:'clique_number'}

graph_properties = {1:'is_connected',
                  2:'is_cubic',
                  3:'triangle_free'}
                  #4:'claw_free',
                  #5:'triangulation',
                  #6:'polyhedral',
                  #7:'tree'}


def main():
    print(figlet_format('Conjecture with TNP', font='slant'))
    #print(figlet_format(' - LIGHT', font='slant'))
    print('Version ' + __version__)
    print('Copyright ' + u'\u00a9' + ' 2019 Randy Davila')
    print()

    print('The invariants you may conjecture against are: ')
    print('-----------------------------------------------')
    print()
    i = 1
    for x in valid_invariants:
        print(f'{i}. {valid_invariants[x]}')
        i+=1
        print()
    print('-----------------------------------------------')
    print()
    invariant = valid_invariants[int(input('Invariant: '))]
    print()

    try:
        with open(f'tnp/graph_data/{invariant}_conjectures', 'rb') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error, '. Please make desired database.')
        return None

    #parameter_quest = input('Would you like to specify a graph structural property to focus on? (y/n) ')
    #print()
    #if parameter_quest == 'y':
    #    for x in graph_properties:
    #        print(f'{x}. {graph_properties[x]}')
    #        print()
    #    parameter = graph_properties[int(input('Please specify the structural property you are interested in: '))]
        
    #    conjectures = get_conjectures(invariant)
    #    U = Theo([x for x in conjectures['upper'] if parameter in x.hyp.properties])
    #    L = Theo([x for x in conjectures['lower'] if parameter in x.hyp.properties])
    #    print()

    #else:
    conjectures = get_conjectures(invariant)
    U = Theo([x for x in conjectures['upper'] 
                if set(x.expression).issubset(valid_invariants.items()) == False])
    L = Theo([x for x in conjectures['lower'] 
                if set(x.expression).issubset(valid_invariants.items()) == False])
    print('Upper Bounds')
    for i in range(10):
        print(f'Conjecture {i}. {U[i]}')
        print('')
    print()
    print('Lower Bounds')
    for i in range(10):
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
        for i in range(10):
            print(f'Conjecture {i}. {U[i]}')
            print('')
        print()
        print('Lower Bounds')
        for i in range(10):
            print(f'Conjecture {i}. {L[i]}')
            print('')
        print()

        work = input('Remove conjectures? (y/n) ')

    f = open(f'tnp/graph_data/{invariant}_conjectures', 'wb')
    conj_dict = {'upper': U, 'lower': L}
    pickle.dump(conj_dict, f)
    f.close()
    return 0



if __name__ == '__main__':
    main()
