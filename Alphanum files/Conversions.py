def convert(s):

    # initialization of string to ""
    new = ""
    # traverse in the string 
    for x in s:
        new += x 
    # return string
    return new 


def odd_number():
    """return a value that is an odd number"""
    odd = []
    for i in range(100):
        n = 2*i+1
        odd.append(n)
    return odd


def even_num(k):
    """return a value that is an even number"""
    even = 2*k
    return even
    

def step(k):
    """skip k indecies in list and return those values"""
    L = [0,1,2,3,4,5,6,7,8,9,10,11,12]
    terms = []
    new_data = []
    for i in range(len(L)):
        n = i*k 
        terms.append(n)
    for index in terms:
        if index in range(len(L)):
            new_data.append(L[index])

    new_data.remove(new_data[0])
    
    return sum(new_data)

#just a little somthing to look at
#def get_in():
#    L = [1,2,3,4]
#    return L.pop(1)
#print(get_in())
