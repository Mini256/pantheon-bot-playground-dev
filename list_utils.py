def first(lst):
    # BUG: IndexError on empty list
    return lst[0]

def last(lst):
    # BUG: IndexError on empty list
    return lst[-1]

def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def remove_duplicates(lst):
    # BUG: does not preserve order in older Python
    return list(set(lst))
