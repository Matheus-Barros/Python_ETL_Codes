from itertools import combinations

'''
@Author: Matheus Barros
Date: 29/12/2020

'''
#========== COMBINIG USING ZIP ==========
names = ['Bulbasaur','Charmander','Squirtle']
hps = [45, 39, 44]

combined_zip_lst = [*zip(names,hps)]

print('Zip:',combined_zip_lst,sep='\n')

#========== MAKING COMBINATIONS ==========
poke_types = ['Bug','Fire','Ghost','Grass','Water']

combos_obj = [*combinations(poke_types, 2)]
print('\nCombinations:',combos_obj,sep='\n')

duplicated_values = ['Pikachu','Pikachu']
non_duplicated_values = set(duplicated_values)

#========== GETTING UNIQUE VALUES ==========
print('\nNon duplicated values:',non_duplicated_values,sep='\n')


ash_pokedex = ['Pikachu', 'Bulbasaur', 'Koffing', 'Spearow', 'Vulpix', 'Wigglytuff', 'Zubat', 'Rattata', 'Psyduck', 'Squirtle']
misty_pokedex  = ['Krabby', 'Horsea', 'Slowbro', 'Tentacool', 'Vaporeon', 'Magikarp', 'Poliwag', 'Starmie', 'Psyduck', 'Squirtle']

#========== Convert both lists to sets ==========
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

#========== Find the Pokémon that exist in both sets ==========
both = ash_set.intersection(misty_set)
print('\nValues in both sets:',both,sep='\n')

#========== Find the Pokémon that Ash has and Misty does not have ==========
ash_only = ash_set.difference(misty_set)
print('\nDifferences between two sets:',ash_only,sep='\n')

#========== Find the Pokémon that are in only one set (not both) ==========
unique_to_set = ash_set.symmetric_difference(misty_set)
print('\nValues at only one set:',unique_to_set,sep='\n')
