import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
from dfa import DFA

tiny_symbols = {'IF', 'NUM', 'THEN', 'ID', 'ELSE', 'END', ';', ':='}
tiny_transitions = {
    '1': {'IF': '2'},
    '2': {'NUM': '3'},
    '3': {'THEN': '4'},
    '4': {'ID': '5'},
    '5': {':=': '6'},
    '6': {'ID': '7', 'NUM': '7'},
    '7': {';': '8'},
    '8': {'END': '15', 'ELSE': '9', 'ID': '5'},
    '9': {'ID': '11', 'IF': '10'},
    '10': {'NUM': '3'},
    '11': {':=': '12'},
    '12': {'ID': '13', 'NUM': '13'},
    '13': {';': '14'},
    '14': {'END': '15'},
    '15': {},
    '16': {}
}
S = DFA(states=list(str(n) for n in range(1, 17)),
        input_symbols=tiny_symbols,
        transitions=tiny_transitions,
        initial_state='1',
        final_states={'15'})

node_pos = {
    '1': (100, 200),
    '2': (200, 200),
    '3': (300, 200),
    '4': (400, 200),
    '5': (500, 200),
    '6': (600, 200),
    '7': (700, 200),
    '8': (700, 100),
    '9': (800, 100),
    '10': (400, 0),
    '11': (900, 200),
    '12': (1000, 200),
    '13': (1100, 200),
    '14': (1200, 200),
    '15': (800, 300),
    '16': (600, 400)
}

G = Network(height='100%', width='100%', directed=True)
G.hrepulsion()
for state in S.states:
    G.add_node(int(state), shape="ellipse", physics=False, x=node_pos[state][0], y=node_pos[state][1])
G.nodes[15]["label"] = 'D'

for k in S.states:
    for kk in S.transitions[k]:
        G.add_edge(int(k), int(S.transitions[k][kk]), label=kk)

G.set_options("""
var options = {
                  "edges": {
                    "smooth": {
                        "enabled" : true
                    }
                  }
                }
""")
G.save_graph("DFA.html")




# G = nx.DiGraph()
# G.add_nodes_from(S.states)
#
# edges_label = {}
# for k in S.transitions:
#     for kk in S.transitions[k]:
#         G.add_edge(k, S.transitions[k][kk])
#         edges_label[(k, S.transitions[k][kk])] = kk
#
# pos = nx.circular_layout(G)
# nx.draw_networkx_nodes(G, pos,
#                        cmap=plt.get_cmap('Greens'),
#                        node_size=500)
#
# nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
# nx.draw_networkx_edge_labels(
#     G, pos,
#     edge_labels=edges_label,
#     font_color='red'
# )
# nx.draw_networkx_labels(G, pos)
# plt.show()
