"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    if items == []:
        return {}
    
    frequencies = {}
    # Your code goes here
    items = list(map(lambda item: str(item), items))
    items.sort()
    count = 1
    lastUnique = items[0]

    for i in range(1,len(items)):
        if items[i] == lastUnique:
            count += 1
        else:
            frequencies[str(items[i-1])] = count
            lastUnique = items[i]
            count = 1
    frequencies[str(items[i])] = count

    return frequencies