"""Alpha Numeric."""


alphabetnums = {
    'a': '1',
    'b': '2',
    'c': '3',
    'd': '4',
    'e': '5',
    'f': '6',
    'g': '7',
    'h': '8',
    'i': '9',
    'j': '10',
    'k': '11',
    'l': '12',
    'm': '13',
    'n': '14',
    'o': '15',
    'p': '16',
    'q': '17',
    'r': '18',
    's': '19',
    't': '20',
    'u': '21',
    'v': '22',
    'w': '23',
    'x': '24',
    'y': '25',
    'z': '26',
}


def AlphaNum_NumAlpha(string):
    string_to_list = [x for x in string]
    new_list = []
    for i in range(len(string_to_list) - 1):
        if ''.join(string_to_list[i:i + 2]).isnumeric():
            string_to_list[i] = ''.join(string_to_list[i:i + 2])
            del string_to_list[i + 1]
    for item in string_to_list:
        if item.isnumeric():
            for letter, number in alphabetnums.items():
                if number == item:
                    new_list.append(letter)
        else:
            new_list.append(alphabetnums.get(item))
    return ''.join(new_list)
