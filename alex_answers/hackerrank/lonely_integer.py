
from collections import Counter



def lonelyinteger(a):

    my_counter = Counter(a)

    for k, count in my_counter:

        if count == 1:
            return k





if __name__ == "__main__":
    print(lonelyinteger([1,2,3,4,3,2,1,]))