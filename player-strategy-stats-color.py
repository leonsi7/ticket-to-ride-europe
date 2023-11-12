import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import multiprocessing

colors = ['red','blue','gold','black','orange','green','pink','engine']
repartition_wagons = {2: 0.37, 3: 0.29, 4: 0.28, 1: 0.03, 6: 0.02, 8: 0.01}
repartition_wagons = {1:1}
wagons = list(repartition_wagons.keys())
prob_wagons =  list(repartition_wagons.values())

def new_visible_cards(visible_cards_input):
    nb_cards_to_add = 4 - sum(visible_cards_input.values())
    new_visible_cards = visible_cards_input
    for _ in range(max(nb_cards_to_add,2)):
        random_key = np.random.choice(colors)
        new_visible_cards[random_key] += 1
    return new_visible_cards

def select_cards_one_turn(strategy, visible_cards, collection):
    is_2, is_1 = False, False
    new_visible_cards = visible_cards
    new_strategy = strategy
    new_collection = collection
    for index, row in new_strategy.loc[new_strategy['Completed'] == False].iterrows():
        color = row['Color']
        carriages_needed = row['Carriages']
        if collection[color] >= carriages_needed :
            new_strategy.loc[index,'Completed'] = True
            collection[color] -= carriages_needed
            new_strategy.loc[len(strategy.index)] = [np.random.choice(colors), np.random.choice(wagons, p=prob_wagons),False]
            return new_strategy, new_visible_cards,  new_collection
        if new_visible_cards[color] == 2:
            is_2 = True
            color2 = color
        if new_visible_cards[color] == 1:
            is_1 = True
            color1 = color
    if is_2:
        new_visible_cards[color2] -= 2
        new_collection[color2] += 2
        return new_strategy, new_visible_cards,  new_collection
    if is_1:
        new_visible_cards[color1] -= 1
        new_collection[color1] += 1
        random_color = np.random.choice(colors)
        new_collection[random_color] += 1
        return new_strategy, new_visible_cards,  new_collection
    else:
        random_color = np.random.choice(colors)
        new_collection[random_color] += 1
        random_color = np.random.choice(colors)
        new_collection[random_color] += 1
        return new_strategy, new_visible_cards,  new_collection
    
def one_game(nb):
    strategy = pd.DataFrame(columns= ['Color','Carriages','Completed'])
    for _ in range(4):
        color_chosen = np.random.choice(colors)
        strategy.loc[len(strategy.index)] = [color_chosen, np.random.choice(wagons, p=prob_wagons),False]

    visible_cards_current = {color: 0 for color in colors}
    for _ in range(4):
        random_key = np.random.choice(colors)
        visible_cards_current[random_key] += 1

    collection = {color: 0 for color in colors}

    for i in range(50):
        strategy, visible_cards_current, collection = select_cards_one_turn(strategy, visible_cards_current, collection)
        visible_cards_current = new_visible_cards(visible_cards_current)
    
    nb_completed_true = (strategy['Completed'] == True).sum()
    return nb_completed_true

if __name__ == "__main__":
    # Liste des valeurs sur lesquelles vous souhaitez appliquer la fonction
    valeurs = [1 for _ in range(1000)]

    # Nombre de processus à utiliser (ajustez selon le nombre de cœurs de votre CPU)
    nombre_de_processus = multiprocessing.cpu_count()

    # Utilisation de Pool pour créer un pool de processus
    with multiprocessing.Pool(processes=nombre_de_processus) as pool:
        # Utilisation de map pour appliquer la fonction de manière parallèle
        resultats = pool.map(one_game, valeurs)

    # Les résultats seront dans la même ordre que les valeurs d'entrée
    print("Résultats finaux:", resultats)
    print("Moyenne des resultats :", sum(resultats)/len(resultats))