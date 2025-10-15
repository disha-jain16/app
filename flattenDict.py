def flatten_dict(d, parent_key='', sep='.'):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep))
        else:
            items[new_key] = v
    return items

# Test
nested = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
print(flatten_dict(nested))
# Output: {'a': 1, 'b.c': 2, 'b.d.e': 3}
