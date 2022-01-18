from lib2to3.pgen2.token import GREATER


def Get_Items(filename):
    """Convert plain text to class string"""
    L = []
    with open(filename, 'r') as file:
        items = file.readlines()
        for line in items:
            L.append(line[:-1])
    return L

def repeat(txt):
    """"""
    data = []
    for i in txt:
        data.append(i)

    