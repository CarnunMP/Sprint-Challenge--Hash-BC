#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i, weight in enumerate(weights):
        existing_ht_entry = hash_table_retrieve(ht, weight)
        if existing_ht_entry == None:
            hash_table_insert(ht, weight, [i])
        else:
            hash_table_insert(ht, weight, existing_ht_entry + [i])

    for weight in weights:
        limit_minus_weight = hash_table_retrieve(ht, limit - weight)

        if limit_minus_weight != None:
            weight_index = hash_table_retrieve(ht, weight)[0]

            if limit - weight == weight:
                # print(limit_minus_weight)
                weight_index = limit_minus_weight[1]
            
            limit_minus_weight = limit_minus_weight[0]

            # print((max(limit_minus_weight, weight_index), min(limit_minus_weight, weight_index)))

            return (max(limit_minus_weight, weight_index), min(limit_minus_weight, weight_index))


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
