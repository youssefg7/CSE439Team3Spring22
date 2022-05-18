parsing_table = [
    # State 0
    {
        'actions': {
            'ID': ('s', 6),
            'if': ('s', 5)
        },
        'goto': {
            'stmt-seq': 1,
            'statement': 2,
            'if-stmt': 3,
            'assign-stmt': 4,
        }
    },

    # State 1
    {
        'actions': {
            'ID': ('s', 6),
            'if': ('s', 5),
            '$': ('r', 1)       # acceptance
        },
        'goto': {
            'statement': 7,
            'if-stmt': 3,
            'assign-stmt': 4
        }
    },

    # State 2
    {
        'actions': {
            'ID': ('r', 3),
            'if': ('r', 3),
            'end': ('r', 3),
            '$': ('r', 3)
        },
        'goto': {}
    },

    # State 3
    {
        'actions': {
            'ID': ('r', 4),
            'if': ('r', 4),
            'end': ('r', 4),
            '$': ('r', 4)
        },
        'goto': {}
    },

    # State 4
    {
        'actions': {
            'ID': ('r', 5),
            'if': ('r', 5),
            'end': ('r', 5),
            '$': ('r', 5)
        },
        'goto': {}
    },

    # State 5
    {
        'actions': {
            'NUM': ('s', 8)
        },
        'goto': {}
    },

    # State 6
    {
        'actions': {
            ':=': ('s', 9)
        },
        'goto': {}
    },

    # State 7
    {
        'actions': {
            'ID': ('r', 2),
            'if': ('r', 2),
            'end': ('r', 2),
            '$': ('r', 2)
        },
        'goto': {}
    },

    # State 8
    {
        'actions': {
            'then': ('s', 10)
        },
        'goto': {}
    },

    # State 9
    {
        'actions': {
            'NUM': ('s', 13),
            'ID': ('s', 12)
        },
        'goto': {
            'factor': 11
        }
    },

    # State 10
    {
        'actions': {
            'ID': ('s', 6),
            'if': ('s', 5)
        },
        'goto': {
            'stmt-seq': 14,
            'statement': 2,
            'if-stmt': 3,
            'assign-stmt': 4
        }
    },

    # State 11
    {
        'actions': {
            ';': ('s', 15)
        },
        'goto': {}
    },

    # State 12
    {
        'actions': {
            ';': ('r', 8)
        },
        'goto': {}
    },

    # State 13
    {
        'actions': {
            ';': ('r', 9)
        },
        'goto': {}
    },

    # State 14
    {
        'actions': {
            'ID': ('s', 6),
            'if': ('s', 5),
            'end': ('s', 16)
        },
        'goto': {
            'statement': 7,
            'if-stmt': 3,
            'assign-stmt': 4
        }
    },

    # State 15
    {
        'actions': {
            'ID': ('r', 7),
            'if': ('r', 7),
            'end': ('r', 7),
            '$': ('r', 7)
        },
        'goto': {}
    },

    # State 16
    {
        'actions': {
            'ID': ('r', 6),
            'if': ('r', 6),
            'end': ('r', 6),
            '$': ('r', 6)
        },
        'goto': {}
    }
]

production_rules = [
    (),
    # Rule 1
    ("s'", ['stmt-seq']),
    # Rule 2
    ('stmt-seq', ['stmt-seq', 'statement']),
    # Rule 3
    ('stmt-seq', ['statement']),
    # Rule 4
    ('statement', ['if-stmt']),
    # Rule 5
    ('statement', ['assign-stmt']),
    # Rule 6
    ('if-stmt', ['if', 'NUM', 'then', 'stmt-seq', 'end']),
    # Rule 7
    ('assign-stmt', ['ID', ':=', 'factor', ';']),
    # Rule 8
    ('factor', ['ID']),
    # Rule 9
    ('factor', ['NUM']),
]