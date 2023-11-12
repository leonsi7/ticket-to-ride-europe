import networkx as nx
import pandas as pd
import matplotlib.pylab as plt
import numpy as np


G = nx.Graph()
cities = pd.read_csv('cities.csv', index_col=0).to_dict(orient='index')
positions = {city:(pos['Longitude'],pos['Latitude']) for city,pos in cities.items()}
routes = pd.read_csv('routes.csv')
destinations = pd.read_csv('destinations.csv')

cost_dict = {1:1, 2:0.71, 3:0.53,4:0.43,6:0.29,8:0.21}

def cost(carriages,colored,tunnel,engines):
    r_engines = engines/carriages
    loss_engines = 1+0.5*r_engines
    loss_tunnel = 1.25 if tunnel else 1
    gain_gray = 1.3 if not colored else 1
    inv_cost = cost_dict[carriages]*gain_gray/loss_engines/loss_tunnel
    return 1/inv_cost

gain_dict = {1:1,2:2,3:4,4:7,6:13,8:21}

def proficency(carriages,colored,tunnel,engines):
    cost_value = cost(carriages,colored,tunnel,engines)
    gain_value = gain_dict[carriages]
    return gain_value/cost_value

# Parcourir les lignes du DataFrame
for index, row in routes.iterrows():
    source = row['Source']
    target = row['Target']
    carriages = row['Carriages']
    colored = row['Colored']
    tunnel = row['Tunnel']
    engines = row['Engine']
    proficency_value = proficency(carriages,colored,tunnel,engines)
    cost_value = cost(carriages,colored,tunnel,engines)
    G.add_edge(source, target, carriages=carriages, 
               colored=colored, tunnel=tunnel, engines=engines, 
               proficecncy=proficency_value,
               cost=cost_value, utility=0)

weight_value = {1:1,2:2,3:4,4:7,6:13,8:21}

max_proficecncy = max(nx.get_edge_attributes(G, "proficecncy").values())
max_cost = max(nx.get_edge_attributes(G, "cost").values())
for u, v, attrs in G.edges(data=True):
    attrs['cost'] = attrs['cost']/max_cost
    attrs['proficecncy'] = attrs['proficecncy']/max_proficecncy

def utility(min_dist, opt_dist, points):
    return np.exp(-opt_dist/min_dist)*points


for _ , row in destinations.iterrows():
    source = row['Source']
    target = row['Target']
    points = row['Points']
    min_lengths_source, _ = nx.single_source_dijkstra(G, source=source, weight="cost")
    min_lengths_target, _ = nx.single_source_dijkstra(G, source=target, weight="cost")
    min_dist = min_lengths_source[target]
    for u, v, attrs in G.edges(data=True):
        opt_dist_edge = min(min_lengths_source[u]+min_lengths_target[v],min_lengths_source[v]+min_lengths_target[u])+attrs['cost']
        attrs['utility'] = attrs['utility'] + utility(min_dist, opt_dist_edge, points)

max_utility = max(nx.get_edge_attributes(G, "utility").values())
for u, v, attrs in G.edges(data=True):
    attrs['utility'] = attrs['utility']/max_utility
    attrs['valuability'] = 0.4*attrs['utility'] + 0.6*attrs['proficecncy']


#Affichage du graphe
nx.draw(G,positions,node_size=600,font_size = 6, node_color='#eab676',with_labels=True)

#Ecriture des poids
edge_labels = {(u, v): np.round(d['valuability'],2) for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, positions, edge_labels=edge_labels, font_size=6,font_color='black', label_pos=0.5)

plt.show()