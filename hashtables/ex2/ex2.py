#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    start = hash_table_retrieve(hashtable, 'NONE')
    route[0] = start

    for i in range(length):
        print(route[i])
        destination = hash_table_retrieve(hashtable, route[i])
        if destination != 'NONE':
            route[i + 1] = destination

    return route
