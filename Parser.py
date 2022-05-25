from ParsingTable import parsing_table, production_rules
from pyvis.network import Network
from uuid import uuid4
from Scanner import Scanner


class Parser:
    def __init__(self):
        self.table = parsing_table
        self.rule = production_rules
        self.parsing_stack = ['$', 0]
        self.input_stack = ['$']
        self.nodes_stack = []
        self.parse_tree = Network(height='100%', width='100%', directed=True)
        self.__set_parse_tree_options()

    def parse(self, input_code):
        parsing_result = False
        error_message = "Parsing error"
        self.__init__()
        tokens = Scanner().get_tokens(input_code)
        [self.input_stack.append(token) for token in tokens[::-1]]
        while len(self.input_stack) != 0:
            lookahead = self.input_stack[-1]
            state = self.parsing_stack[-1]
            actions = self.table[state]['actions']
            if lookahead in actions.keys():
                action = actions[lookahead][0]  # 's' | 'r'
                if action == 's':
                    next_state = actions[lookahead][1]
                    self.__shift(lookahead, next_state)
                elif action == 'r':
                    rule_no = actions[lookahead][1]
                    self.__reduce(rule_no)
                    # Check if it is acceptance rule
                    if rule_no == 1:
                        parsing_result = True
                        error_message = "_________Parsing Complete__________"
                        break
            else:
                parsing_result = False
                error_message = f"Unexpected terminal!  Current state: {state}, Expected: {list(actions.keys())}, Found: {lookahead}"  # Throw Exceptions
                break
        self.parse_tree.save_graph("Parse Tree.html")
        print(error_message)
        return parsing_result, error_message

    def __shift(self, lookahead, next_state):
        self.input_stack.pop()
        self.parsing_stack.append(lookahead)
        self.parsing_stack.append(next_state)
        node_id = str(uuid4())
        self.nodes_stack.append(node_id)
        self.parse_tree.add_node(node_id, label=lookahead, group='terminal', shape='ellipse', color='white')
        print(self.parsing_stack)

    def __reduce(self, rule_no):
        left_symbol = self.rule[rule_no][0]
        right_symbols = list(self.rule[rule_no][1])

        for symbol in right_symbols[::-1]:
            self.parsing_stack.pop()
            if symbol == self.parsing_stack[-1]:
                self.parsing_stack.pop()
            else:
                print(
                    f"Reduction error in rule {rule_no}: Expected {symbol}, found {self.parsing_stack[-1]}")  # Throw Exceptions
                break
        old_state = self.parsing_stack[-1]
        if left_symbol in self.table[old_state]['goto'].keys():
            next_state = self.table[old_state]['goto'][left_symbol]
            self.parsing_stack.append(left_symbol)
            self.parsing_stack.append(next_state)
            print(self.parsing_stack)
        # else:
        #     print("error3")  # Throw Exceptions
        #     break

        n = len(right_symbols)
        child_nodes_ids = self.nodes_stack[-n:]
        parent_id = str(uuid4())
        self.parse_tree.add_node(parent_id, label=left_symbol, group='non-terminal', shape='ellipse')
        for child_id in child_nodes_ids:
            self.parse_tree.add_edge(parent_id, child_id)
            self.nodes_stack.pop()
        self.nodes_stack.append(parent_id)

    def __set_parse_tree_options(self):
        self.parse_tree.set_options(
        """
            {
                "nodes": {
                    "color": {
                        "border": "#03dac8",
                        "background": "white"
                    },
                    "shape": "text"
                },
                "interaction": {
                    "keyboard": {
                        "enabled": true
                    },
                    "navigationButtons": true
                },
                "layout": {
                    "hierarchical": {
                        "sortMethod": "directed"
                    }
                },
                "groups": {
                    "terminal": {
                        "font": {
                            "color": "black",
                            "face": "bold",
                            "size": 24
                        }
                    },
                    "non-terminal": {
                        "shape": "database",
                        "font": {
                            "color": "lime",
                            "size": 24
                        }
                    }
                },
                "physics": {
                    "enabled": true,
                    "minVelocity": 0.75,
                    "solver": "repulsion"
                }
            }
        """
        )


if __name__ == "__main__":
    # input_stack = ['$', 'end', ';', 'NUM', ':=', 'ID', 'end', ';', 'ID', ':=', 'ID', ';', 'NUM', ':=', 'ID', 'then', 'NUM', 'if', 'then', 'NUM', 'if']
    # input_stack = ['$', 'end', ';', 'NUM', ':=', 'ID', 'then', 'NUM', 'if']
    #input_stack = ['$', ';', 'NUM', ':=', 'ID']
    parser = Parser()
    parser.parse("""
        x := 0 ;
        if 1 then
            x := 15 ;
            if 5 then
                x := dfg5 ;
                x := 78 ;
            end
            x := 132 ;
        end
                    """)
    #parser.parse_tree.show("Parse Tree.html")











    # def reduce(self, rule_no):
    #     left_symbol = self.rule[rule_no][0]
    #     right_symbols = list(self.rule[rule_no][1])
    #     for symbol in right_symbols[::-1]:
    #         self.parsing_stack.pop()
    #         if symbol == self.parsing_stack[-1]:
    #             self.parsing_stack.pop()
    #         else:
    #             print("error4")  # Throw Exceptions
    #             break
    #     old_state = self.parsing_stack[-1]
    #     if left_symbol in self.table[old_state]['goto'].keys():
    #         next_state = self.table[old_state]['goto'][left_symbol]
    #         self.parsing_stack.append(left_symbol)
    #         self.parsing_stack.append(next_state)
    #         print(self.parsing_stack)
    #     else:
    #         print("error3")  # Throw Exceptions
    #         break
