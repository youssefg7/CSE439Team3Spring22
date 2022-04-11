import re

x = input()
y = re.search('^(IF [0-9]+ THEN ([_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z]+[_a-zA-Z0-9]*|[0-9]+);)+'
              '(ELSE IF NUM THEN ([_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z][_a-zA-Z0-9]*|[0-9]+);)+)*'
              '(ELSE ([_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z][_a-zA-Z0-9]*|[0-9]+);)+)? END)+$', x)
if y is not None:
    print(f'The recognized expression: "{y.string}"')
    print(f"Its tokens are:")
    tokens = re.findall('IF|[0-9]+|THEN|ELSE|END|[_a-zA-Z][_a-zA-Z0-9]*|:=|;', y.string)
    for i in range(len(tokens)):
        print(f'{i + 1} : {tokens[i]}')

else :
    print('Invalid Input')