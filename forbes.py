from forbes_file import billionaires


def forbes_function():
    """Function that takes file and returns information."""
    oldest = {
        'name': None,
        'age': 0,
        'net_worth': 0,
        'industry': None,
    }
    youngest = {
        'name': None,
        'age': 100,
        'net_worth': 0,
        'industry': None,
    }
    for person in billionaires:
        if person['age'] > oldest['age'] and person['age'] < 80:
            oldest['name'] = person['name']
            oldest['age'] = person['age']
            oldest['net_worth'] = person['net_worth (USD)']
            oldest['industry'] = person['source']
        if person['age'] < youngest['age'] and person['age'] > 0:
            youngest['name'] = person['name']
            youngest['age'] = person['age']
            youngest['net_worth'] = person['net_worth (USD)']
            youngest['industry'] = person['source']
    return [oldest, youngest]

