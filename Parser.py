from ParsingTable import parsing_table, production_rules
class Parser:
    def __init__(self):
        self.table = parsing_table
        self.rule = production_rules
        self.parsing_stack = ['$', 0]

    def parse(self, input_stack):
        while len(input_stack) != 0:
            lookahead = input_stack[-1]
            current = int(self.parsing_stack[-1])
            actions = self.table[current]['actions']
            if lookahead in actions.keys():
                # action = actions[lookahead]  # action = ('s', 5)
                action = str(actions[lookahead][0])  # 's' | 'r'
                x = int(actions[lookahead][1])
                if action == 's':
                    input_stack.pop()
                    self.parsing_stack.append(lookahead)
                    self.parsing_stack.append(x)
                    print(self.parsing_stack)
                elif action == 'r':
                    if x == 1:  # acceptance rule
                        print("Input Accepted")
                        # pop and push s'
                        break
                    else:
                        left_symbol = str(self.rule[x][0])
                        right_symbols = list(self.rule[x][1])
                        for symbol in right_symbols[::-1]:
                            self.parsing_stack.pop()
                            if symbol == self.parsing_stack[-1]:
                                self.parsing_stack.pop()
                            else:
                                print("error4")  # Throw Exceptions
                                break
                        old_state = int(self.parsing_stack[-1])
                        if left_symbol in self.table[old_state]['goto'].keys():
                            next_state = int(self.table[old_state]['goto'][left_symbol])
                            self.parsing_stack.append(left_symbol)
                            self.parsing_stack.append(next_state)
                            print(self.parsing_stack)
                        else:
                            print("error3")  # Throw Exceptions
                            break
                else:
                    print("error2")  # Throw Exceptions
                    break
            else:
                print("error1")  # Throw Exceptions
                break


if __name__ == "__main__":
    input_stack = ['$', 'end', ';', 'NUM', ':=', 'ID', 'end', ';', 'ID', ':=', 'ID', ';', 'NUM', ':=', 'ID', 'then',
                   'NUM', 'if', 'then', 'NUM', 'if']
    # input_stack = ['$', 'end', ';', 'NUM', ':=', 'ID', 'then', 'NUM', 'if']
    # input_stack = ['$', ';', 'NUM', ':=', 'ID']
    parser = Parser()
    parser.parse(input_stack)
