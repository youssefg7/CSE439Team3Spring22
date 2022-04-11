#!/usr/bin/env python3
"""Classes and methods for working with deterministic finite automata."""
import copy
from collections import defaultdict


class DFA:
    """A deterministic finite automaton."""

    def __init__(self, *, states, input_symbols, transitions,
                 initial_state, final_states, allow_partial=False):
        """Initialize a complete DFA."""
        self.states = states.copy()
        self.input_symbols = input_symbols.copy()
        self.transitions = copy.deepcopy(transitions)
        self.initial_state = initial_state
        self.final_states = final_states.copy()
        self.allow_partial = allow_partial

    def __lt__(self, other):
        """Return True if this DFA is a strict subset of another DFA."""
        if isinstance(other, DFA):
            return self <= other and self != other
        else:
            raise NotImplementedError

    def __gt__(self, other):
        """Return True if this DFA is a strict superset of another DFA."""
        if isinstance(other, DFA):
            return self >= other and self != other
        else:
            raise NotImplementedError

    def _get_next_current_state(self, current_state, input_symbol):
        """
        Follow the transition for the given input symbol on the current state.

        Raise an error if the transition does not exist.
        """
        if input_symbol in self.transitions[current_state]:
            return self.transitions[current_state][input_symbol]

    def _make_graph(self):
        """
        Returns a simple graph representation of the DFA.
        """
        G = defaultdict(set)
        for k, v in self.transitions.items():
            for c, u in v.items():
                G[k].add(u)
        return G

    def _reachable_nodes(self, G, v, vis):
        """
        Computes the set of reachable nodes
        in the graph G starting at vertex v.
        """
        if v not in vis:
            vis.add(v)
            for u in G[v]:
                self._reachable_nodes(G, u, vis)
