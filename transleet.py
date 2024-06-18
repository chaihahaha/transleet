def transleet(s, unicode=False):
    changes = {
        'a': '4',
        'b': '6',
        'e': '3',
        'g': '9',
        'i': '1',
        'o': '0',
        's': '5',
        't': '7',
        'z': '2',
        'x': '8',
        'k': '%',
        'h': '#',
        "c": "(",
        "l": "|",
    }
    if unicode:
        unicode_changes = {
            "u": "µ",
            "v": "ν",
            "w": "ω",
            "r": "γ",
            "k": "κ",
            "f": "≠",
            'd': 'δ',
            'p': 'ρ',
        }
        changes = {**changes, **unicode_changes}
    inv_changes = {v: k for k, v in changes.items()}
    changes = {**changes, **inv_changes}
    tt = str.maketrans(changes)
    s = s.lower().translate(tt)
    return s
