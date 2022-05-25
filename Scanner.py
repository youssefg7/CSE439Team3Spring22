import re


def get_tokens_list(input_code):
    # y = re.search('^(IF [0-9]+ THEN ([_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z]+[_a-zA-Z0-9]*|[0-9]+);)+'
    #               '( ELSE IF [0-9]+ THEN ([_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z]+[_a-zA-Z0-9]*|[0-9]+);)+)*'
    #               '( ELSE ([_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z]+[_a-zA-Z0-9]*|[0-9]+);)+)? END)+$', input_code)
    NUM = "([0-9]+)"
    ID = "([_a-zA-Z]\w*)"
    STMT = f"({ID}\s*:=\s*({NUM}|{ID})\s*;\s*)"
    IFBODY = f"(IF\s+{NUM}\s+THEN\s+({STMT})+\s*)"
    REGEX = f"(^\s*{IFBODY}((ELSE\s+{IFBODY})+)?(ELSE\s+({STMT})+)?END\s*$)"
    ################

    if re.search(REGEX, input_code) is None:
        print("Invalid Input")

    tokens_list = []
    tokens = re.findall('IF|[0-9]+|THEN|ELSE|END|[_a-zA-Z][_a-zA-Z0-9]*|:=|;|.', input_code)
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
        elif re.fullmatch("[0-9]+", token) is not None:
            tokens_list.append({"token": token, "type": "NUM"})
        elif re.fullmatch("[_a-zA-Z][_a-zA-Z0-9]*", token) is not None:
            tokens_list.append({"token": token, "type": "ID"})
        elif token != " ":
            tokens_list.append({"token": token, "type": "error"})

    return tokens_list




# import re
#
#
# def get_tokens_list(input_code):
#     # y = re.search('^(IF [0-9]+ THEN ([_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z]+[_a-zA-Z0-9]*|[0-9]+);)+'
#     #               '( ELSE IF [0-9]+ THEN ([_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z]+[_a-zA-Z0-9]*|[0-9]+);)+)*'
#     #               '( ELSE ([_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z]+[_a-zA-Z0-9]*|[0-9]+);)+)? END)+$', input_code)
#     NUM = "([0-9]+)"
#     ID = "([_a-zA-Z]\w*)"
#     STMT = f"({ID}\s*:=\s*({NUM}|{ID})\s*;\s*)"
#     IFBODY = f"(IF\s+{NUM}\s+THEN\s+({STMT})+\s*)"
#     REGEX = f"(\s*{IFBODY}((ELSE\s+{IFBODY})+)?(ELSE\s+({STMT})+)?END\s*)"
#     ################
#     y = re.fullmatch(REGEX, input_code)
#
#     if y is None:
#         print("Invalid IF statement")
#         return None
#     else:
#         tokens_list = []
#         tokens = re.findall('IF|[0-9]+|THEN|ELSE|END|[_a-zA-Z][_a-zA-Z0-9]*|:=|;', y.string)
#         for token in tokens:
#             if token == "IF":
#                 tokens_list.append({"token": token, "type": "IF"})
#             elif token == "THEN":
#                 tokens_list.append({"token": token, "type": "THEN"})
#             elif token == "ELSE":
#                 tokens_list.append({"token": token, "type": "ELSE"})
#             elif token == "END":
#                 tokens_list.append({"token": token, "type": "END"})
#             elif token == ":=":
#                 tokens_list.append({"token": token, "type": ":="})
#             elif token == ";":
#                 tokens_list.append({"token": token, "type": ";"})
#             elif re.search("[0-9]+", token) is not None:
#                 tokens_list.append({"token": token, "type": "NUM"})
#             elif re.search("[_a-zA-Z][_a-zA-Z0-9]*", token) is not None:
#                 tokens_list.append({"token": token, "type": "ID"})
#             else:
#                 raise Exception("Invalid token returned from tokenization")
#
#         return tokens_list


class Scanner:
    def __init__(self):
        NUM = "([0-9]+)"
        ID = "([a-zA-Z_]\w*)"
        STMT = f"({ID}\s*:=\s*({NUM}|{ID})\s*;\s*)"
        IFBODY = f"(IF\s+{NUM}\s+THEN\s+({STMT})+\s*)"
        self.REGEX = f"(^\s*{IFBODY}((ELSE\s+{IFBODY})+)?(ELSE\s+({STMT})+)?END\s*$)"

    def is_valid_syntax(self, input_code):
        if re.search(self.REGEX, input_code) is None:
            return False
        return True
    
    def get_tokens(self, input_code):
        tokens = []
        found_tokens = re.findall('if|then|else|end|:=|;|[0-9]+|[a-zA-Z][_a-zA-Z0-9]*|.', input_code)
        for token in found_tokens:
            if token == "if":
                tokens.append(token)
            elif token == "then":
                tokens.append(token)
            elif token == "else":
                tokens.append(token)
            elif token == "end":
                tokens.append(token)
            elif token == ":=":
                tokens.append(token)
            elif token == ";":
                tokens.append(token)
            elif re.fullmatch("[0-9]+", token) is not None:
                tokens.append("NUM")
            elif re.fullmatch("[a-zA-Z][_a-zA-Z0-9]*", token) is not None:
                tokens.append("ID")
            elif token != " ":
                tokens.append(token)
        return tokens


    def get_tokens_list(self, input_code):
        tokens_list = []
        tokens = re.findall('if|then|else|end|:=|;|[0-9]+|[a-zA-Z][_a-zA-Z0-9]*|.', input_code)
        for token in tokens:
            if token == "if":
                tokens_list.append({"token": token, "type": "IF"})
            elif token == "then":
                tokens_list.append({"token": token, "type": "THEN"})
            elif token == "else":
                tokens_list.append({"token": token, "type": "ELSE"})
            elif token == "end":
                tokens_list.append({"token": token, "type": "END"})
            elif token == ":=":
                tokens_list.append({"token": token, "type": ":="})
            elif token == ";":
                tokens_list.append({"token": token, "type": ";"})
            elif re.fullmatch("[0-9]+", token) is not None:
                tokens_list.append({"token": token, "type": "NUM"})
            elif re.fullmatch("[a-zA-Z][_a-zA-Z0-9]*", token) is not None:
                tokens_list.append({"token": token, "type": "ID"})
            elif token != " ":
                tokens_list.append({"token": token, "type": "UNDEFINED"})
        return tokens_list
