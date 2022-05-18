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
    '14': {'END': '15', 'ID': '11'},
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
    '9': (800, 40),
    '10': (400, 0),
    '11': (900, 200),
    '12': (1000, 200),
    '13': (1100, 200),
    '14': (1200, 300),
    '15': (800, 300),
    '16': (600, 400)
}

G = Network(height='100%', width='100%', directed=True)
G.hrepulsion()
for state in S.states:
    G.add_node(int(state), shape="ellipse", physics=False, x=node_pos[state][0], y=node_pos[state][1])

G.nodes[0]["color"] = 'yellow'
G.nodes[0]["title"] = "Initial State"

G.nodes[14]["color"] = {"background": 'DodgerBlue', "border": 'blue'}
G.nodes[14]["borderWidth"] = 5
G.nodes[14]["borderWidthSelected"] = 5
G.nodes[14]["title"] = "Goal State"

G.nodes[15]["label"] = 'D'
G.nodes[15]["color"] = 'DarkGray'
G.nodes[15]["title"] = "Dead State"

for k in S.states:
    for kk in S.transitions[k]:
        G.add_edge(int(k), int(S.transitions[k][kk]), label=kk)

G.set_options("""
var options = {
                  "edges": {
                    "smooth": {
                        "enabled" : true
                    },
                    "color": {
                        "inherit" : false
                    }
                  },
                  "interaction": {
                    "hover": true,
                    "keyboard": {
                      "enabled": true
                    },
                    "multiselect": true,
                    "navigationButtons": true
                  }
                }
""")
G.save_graph("DFA.html")