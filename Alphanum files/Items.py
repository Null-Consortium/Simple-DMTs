def Get_Items(filename):
    """Convert plain text to class string"""
    L = []
    with open(filename, 'r') as file:
        items = file.readlines()
        for line in items:
            L.append(line[:-1])
    return L

#--- vestigial code
def repeat(txt):
    """"""
    data = []
    for i in txt:
        data.append(i)   
