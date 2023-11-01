import networkx as nx
import matplotlib.pyplot as plt

ONE = 1
TWO = 2
THREE = 4
FOUR = 7
SIX = 13
EIGHT = 21

cities_names= ['Lisboa','Cadiz','Madrid','Barcelona','Pamplona',
              'Marseille','Paris','Brest','Dieppe', 'Zurich','London',
              'Edinburgh', 'Venezia','Roma', 'Munchen','Frankfurt','Bruxelles',
              'Amsterdam','Essen','Berlin', 'Wien','Berlin','Zagrab','Budapest',
              'Brindisi','Palermo','Sarajevo','Athina','Sofia','Smyrna',
              'Constantinople','Bucuresti','Kiev','Warzawa','Sevastopol',
              'Angora','Erzerum','Sochi','Rostov','Kharkov','Moskva','Smolensk',
              'Wilno','Petrograd', 'Stockholm','Riga','Danzig','Khobenhaven']

cities_positions = {
    'Lisboa': (-9.1393, 38.7223),
    'Cadiz': (-6.2921, 36.5298),
    'Madrid': (-3.7038, 40.4168),
    'Barcelona': (2.1734, 41.3851),
    'Pamplona': (-1.6458, 42.8125),
    'Marseille': (5.3698, 43.2965),
    'Paris': (2.3522, 48.8566),
    'Brest': (-4.4861, 48.3904),
    'Dieppe': (1.0792, 49.9252),
    'Zurich': (8.5417, 47.3769),
    'London': (-0.1280, 51.5074),
    'Edinburgh': (-3.1883, 55.9533),
    'Venezia': (12.3155, 45.4408),
    'Roma': (12.4964, 41.9028),
    'Munchen': (11.5819, 48.1351),
    'Frankfurt': (8.6821, 50.1109),
    'Bruxelles': (4.3517, 50.8503),
    'Amsterdam': (4.8975, 52.3779),
    'Essen': (7.0146, 51.4584),
    'Berlin': (13.4050, 52.5200),
    'Wien': (16.3738, 48.2082),
    'Zagrab': (15.9819, 45.8150),
    'Budapest': (19.0402, 47.4979),
    'Brindisi': (17.9253, 40.6368),
    'Palermo': (13.3613, 38.1157),
    'Sarajevo': (18.4131, 43.8563),
    'Athina': (23.7275, 37.9838),
    'Sofia': (23.7275, 42.6977),
    'Smyrna': (27.1428, 38.4192),
    'Constantinople': (28.9795, 41.0082),
    'Bucuresti': (26.1025, 44.4268),
    'Kiev': (30.5238, 50.4501),
    'Warzawa': (21.0122, 52.2297),
    'Sevastopol': (33.5067, 44.6166),
    'Angora': (32.8597, 39.9334),
    'Erzerum': (41.2670, 39.9334),
    'Sochi': (39.7359, 43.5855),
    'Rostov': (39.6916, 47.2357),
    'Kharkov': (36.2304, 49.9935),
    'Moskva': (37.6176, 55.7558),
    'Smolensk': (32.0434, 54.7867),
    'Wilno': (25.2797, 54.6872),
    'Petrograd': (30.3351, 59.9343),
    'Stockholm': (18.0686, 59.3293),
    'Riga': (24.1052, 56.9496),
    'Danzig': (18.6466, 54.3520),
    'Khobenhaven': (12.5683, 55.6761),
}




for city, (x, y) in cities_positions.items():
    cities_positions[city] = (x, y * 1.6)

# Create a new graph
G = nx.Graph()

# Add nodes
for city in cities_names:
       G.add_node(city)

# Add edges
G.add_edge('Lisboa', 'Cadiz', weight=TWO)
G.add_edge('Madrid', 'Lisboa', weight=THREE)
G.add_edge('Madrid', 'Cadiz', weight=THREE)
G.add_edge('Madrid', 'Pamplona', weight=THREE)
G.add_edge('Madrid', 'Barcelona', weight=TWO)
G.add_edge('Marseille', 'Pamplona', weight=FOUR)
G.add_edge('Marseille', 'Barcelona', weight=FOUR)
G.add_edge('Pamplona', 'Barcelona', weight=TWO)
G.add_edge('Pamplona', 'Brest', weight=FOUR)
G.add_edge('Paris', 'Pamplona', weight=FOUR)
G.add_edge('Paris', 'Marseille', weight=FOUR)
G.add_edge('Paris', 'Brest', weight=THREE)
G.add_edge('Paris', 'Dieppe', weight=ONE)
G.add_edge('Paris', 'Zurich', weight=THREE)
G.add_edge('Dieppe', 'London', weight=TWO)
G.add_edge('London', 'Edinburgh', weight=FOUR)
G.add_edge('Zurich', 'Marseille', weight=TWO)
G.add_edge('Zurich', 'Venezia', weight=TWO)
G.add_edge('Marseille', 'Roma', weight=FOUR)
G.add_edge('Venezia', 'Roma', weight=TWO)
G.add_edge('Zurich', 'Munchen', weight=TWO)
G.add_edge('Munchen', 'Venezia', weight=TWO)
G.add_edge('Munchen', 'Frankfurt', weight=TWO)
G.add_edge('Frankfurt', 'Paris', weight=THREE)
G.add_edge('Frankfurt', 'Bruxelles', weight=TWO)
G.add_edge('Bruxelles', 'Paris', weight=TWO)
G.add_edge('Bruxelles', 'Dieppe', weight=TWO)
G.add_edge('Bruxelles', 'Amsterdam', weight=ONE)
G.add_edge('Amsterdam', 'London', weight=TWO)
G.add_edge('Amsterdam', 'Frankfurt', weight=TWO)
G.add_edge('Frankfurt', 'Essen', weight=TWO)
G.add_edge('Amsterdam', 'Essen', weight=TWO)
G.add_edge('Munchen', 'Wien', weight=TWO)
G.add_edge('Berlin', 'Wien', weight=THREE)
G.add_edge('Berlin', 'Essen', weight=TWO)
G.add_edge('Berlin', 'Frankfurt', weight=THREE)
G.add_edge('Wien', 'Zagrab', weight=TWO)
G.add_edge('Zagrab', 'Venezia', weight=TWO)
G.add_edge('Roma', 'Brindisi', weight=TWO)
G.add_edge('Roma', 'Palermo', weight=FOUR)
G.add_edge('Brindisi', 'Palermo', weight=THREE)
G.add_edge('Budapest', 'Zagrab', weight=TWO)
G.add_edge('Budapest', 'Wien', weight=ONE)
G.add_edge('Zagrab', 'Sarajevo', weight=THREE)
G.add_edge('Sarajevo', 'Athina', weight=FOUR)
G.add_edge('Budapest', 'Sarajevo', weight=THREE)
G.add_edge('Brindisi', 'Athina', weight=FOUR)
G.add_edge('Athina', 'Sofia', weight=THREE)
G.add_edge('Sofia', 'Sarajevo', weight=TWO)
G.add_edge('Sofia', 'Constantinople', weight=THREE)
G.add_edge('Athina', 'Smyrna', weight=TWO)
G.add_edge('Smyrna', 'Constantinople', weight=TWO)
G.add_edge('Constantinople', 'Bucuresti', weight=THREE)
G.add_edge('Bucuresti', 'Sofia', weight=TWO)
G.add_edge('Bucuresti', 'Budapest', weight=FOUR)
G.add_edge('Budapest', 'Kiev', weight=SIX)
G.add_edge('Bucuresti', 'Kiev', weight=FOUR)
G.add_edge('Kiev', 'Warzawa', weight=FOUR)
G.add_edge('Warzawa', 'Berlin', weight=FOUR)
G.add_edge('Warzawa', 'Wien', weight=FOUR)
G.add_edge('Constantinople', 'Angora', weight=TWO)
G.add_edge('Smyrna', 'Angora', weight=THREE)
G.add_edge('Angora', 'Erzerum', weight=THREE)
G.add_edge('Sevastopol', 'Constantinople', weight=FOUR)
G.add_edge('Sevastopol', 'Erzerum', weight=FOUR)
G.add_edge('Sochi', 'Erzerum', weight=THREE)
G.add_edge('Sevastopol', 'Sochi', weight=TWO)
G.add_edge('Sochi', 'Rostov', weight=TWO)
G.add_edge('Sevastopol', 'Rostov', weight=FOUR)
G.add_edge('Rostov', 'Kharkov', weight=TWO)
G.add_edge('Kharkov', 'Kiev', weight=FOUR)
G.add_edge('Kharkov', 'Moskva', weight=FOUR)
G.add_edge('Sevastopol', 'Bucuresti', weight=FOUR)
G.add_edge('Moskva', 'Smolensk', weight=TWO)
G.add_edge('Moskva', 'Petrograd', weight=FOUR)
G.add_edge('Petrograd', 'Wilno', weight=FOUR)
G.add_edge('Petrograd', 'Riga', weight=FOUR)
G.add_edge('Petrograd', 'Stockholm', weight=EIGHT)
G.add_edge('Stockholm', 'Khobenhaven', weight=THREE)
G.add_edge('Khobenhaven', 'Essen', weight=THREE)
G.add_edge('Riga', 'Danzig', weight=THREE)
G.add_edge('Danzig', 'Berlin', weight=THREE)
G.add_edge('Danzig', 'Warzawa', weight=TWO)
G.add_edge('Warzawa', 'Wilno', weight=THREE)
G.add_edge('Wilno', 'Riga', weight=FOUR)
G.add_edge('Wilno', 'Smolensk', weight=THREE)
G.add_edge('Wilno', 'Kiev', weight=TWO)
G.add_edge('Smolensk', 'Kiev', weight=THREE)


#Show graph

pos = cities_positions

#Affichage du graphe
nx.draw(G,pos,node_size=600,font_size = 6, node_color='#eab676',with_labels=True)

#Ecriture des poids
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6,font_color='black', label_pos=0.5)

plt.show()
