###
### Author: Arsene Bwasisi
### Description: This program will read in a LEGO-set data files, and process various
###              searches on the LEGO set data. Using the program, users will be able
###              to search through various LEGO sets and figure out which sets do and
###              do not have compatible pieces.

def read_file(file):
    '''
    This function reads in an inputed file and processes into
    a dictionary, with lego set and id as key tuple and a set
    of pieces ids as the value.
    file: A user inputed file
    '''

    open_file = open(file, 'r')
    lego_sets = dict()

    # Iterate through each line and split line by |||
    # Add line into lego_sets
    for line in open_file:
        split_line = line.strip('\n').split(' ||| ')
        key_tuple = tuple(split_line[0].split(','))
        value_set = set(split_line[1].split(','))

        lego_sets[key_tuple] = value_set

    return lego_sets

def subset(lego_dic, search_ids):
    '''
    This function searches for all LEGO sets from the data file whose
    pieces are a subset of the pieces specified by the user to search for.
    lego_dic: Dictionary of all the LEGO sets and ids
    search_ids: Set ids or piece ids specified by the user
    '''

    results = list()
    for keys in lego_dic:
        # Check whether lego_dic set is subset of search_ids
        if lego_dic[keys].issubset(search_ids):
            results.append(keys)# append to result if true

    return results

def superset(lego_dic, search_ids):
    '''
    This function searches for all LEGO sets that contain all
    of the pieces specified by the user to search for.
    lego_dic: Dictionary of all the LEGO sets and ids
    search_ids: Set ids or piece ids specified by the user
    '''

    results = list()
    for keys in lego_dic:
        # Check whether lego_dic set is superset of search_ids
        if lego_dic[keys].issuperset(search_ids):
            results.append(keys)# append to result if true

    return results

def none(lego_dic, search_ids):
    '''
    This function searches for all LEGO sets that contain none of
    the pieces specified by the user to search for.
    lego_dic: Dictionary of all the LEGO sets and ids
    search_ids: Set ids or piece ids specified by the user
    '''

    results = list()
    for keys in lego_dic:
        # Check for any intersection between lego_dic set and search_ids
        if len(lego_dic[keys].intersection(search_ids)) == 0:
            results.append(keys)# if no intersection, append to results

    return results

def sets(lego_dic, search_type, set_ids):
    '''
    This function will peform a search on the Lego sets.
    lego_dic: Dictionary of all the LEGO sets and ids
    search_type: The search to peform, subset, superset or none
    set_ids: Set ids or piece ids specified by the user
    '''

    # Use the sets to access the pieces
    # iterate through lego_dic to find the set pieces
    # add the set pieces to search_ids
    search_ids = set()
    for ids in set_ids:
        for keys in lego_dic:
            if ids in keys:
                search_ids.update(lego_dic[keys])

    if search_type == 'subset':
        results = subset(lego_dic, search_ids)
        print_results(results)
    elif search_type == 'superset':
        results = superset(lego_dic, search_ids)
        print_results(results)
    elif search_type == 'none':
        results = none(lego_dic, search_ids)
        print_results(results)

def pieces(lego_dic, search_type, set_ids):
    '''
    This function will peform a search on the Lego pieces.
    lego_dic: Dictionary of all the LEGO sets and ids
    search_type: The search to peform, subset, superset or none
    set_ids: Set ids or piece ids specified by the user
    '''

    search_ids = set(set_ids)
    
    # Call each function depending on the inputed search type
    # Print results
    if search_type == 'subset':
        results = subset(lego_dic, search_ids)
        print_results(results)
    elif search_type == 'superset':
        results = superset(lego_dic, search_ids)
        print_results(results)
    elif search_type == 'none':
        results = none(lego_dic, search_ids)
        print_results(results)

def print_results(results):
    ''' Print the results in sorted order.
    Students should use this function to print out the search results.
    results: A set of pairs of elements to print in sorted order.
             The pairs of elements will be tuples/lists of set name, then set ID.
    '''
    print()
    results = list(results)
    results.sort()
    for e in results:
        print(e[1] + ' : ' + e[0])

def main():

    file_name = input('LEGO set file name:\n')
    search_value = input('Search by sets or pieces?:\n')
    search_type = input('Search type (subset or superset or none):\n')
    search_ids = input('Search IDs:\n').split()

    dic = read_file(file_name)

    if search_value == 'sets':
        sets(dic, search_type, search_ids)
    else:
        pieces(dic, search_type, search_ids)

main()