# import re
#
# x = input()
# y = re.search('^(IF [0-9]+ THEN( [_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z]+[_a-zA-Z0-9]*|[0-9]+);)+'
#               '( ELSE IF NUM THEN ([_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z][_a-zA-Z0-9]|[0-9]+);)+)*'
#               '( ELSE ([_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z][_a-zA-Z0-9]*|[0-9]+);)+)? END)+$', x)
#
# if y is not None:
#     print(f'The recognized expression: "{y.string}"')
#     print(f"Its tokens are:")
#     tokens = re.findall('IF|[0-9]+|THEN|ELSE|END|[_a-zA-Z][_a-zA-Z0-9]*|:=|;', y.string)
#     for i in range(len(tokens)):
#         print(f'{i + 1} : {tokens[i]}')
#
# else :
#     print('Invalid Input')
import re


def get_tokens_list(input_code):
    y = re.search('^(IF [0-9]+ THEN( [_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z]+[_a-zA-Z0-9]*|[0-9]+);)+'
                  '( ELSE IF NUM THEN ([_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z][_a-zA-Z0-9]|[0-9]+);)+)*'
                  '( ELSE ([_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z][_a-zA-Z0-9]*|[0-9]+);)+)? END)+$', input_code)

    if y is not None:
        #print(f'The recognized expression: "{y.string}"')
        #print(f"Its tokens are:")
        tokens_list = []
        tokens = re.findall('IF|[0-9]+|THEN|ELSE|END|[_a-zA-Z][_a-zA-Z0-9]*|:=|;', y.string)
        for token in tokens:
            if token == "IF":
                tokens_list.append({"token": token, "type": "IF"})
            elif token == "THEN":
                tokens_list.append({"token": token, "type": "THEN"})
            elif token == "ELSE":
                tokens_list.append({"token": token, "type": "ELSE"})
            elif token == "END":
                tokens_list.append({"token": token, "type": "END"})
            elif token == ":=":
                tokens_list.append({"token": token, "type": ":="})
            elif token == ";":
                tokens_list.append({"token": token, "type": ";"})
            elif re.search("[0-9]+", token) is not None:
                tokens_list.append({"token": token, "type": "NUM"})
            elif re.search("[_a-zA-Z][_a-zA-Z0-9]*", token) is not None:
                tokens_list.append({"token": token, "type": "ID"})
            else:
                raise Exception("Invalid token returned from tokenization")

        return tokens_list

    else:
        print("Invalid IF statement")
        return None
