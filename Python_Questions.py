month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month

num_days=days_in_month[month+1]
print(num_days)

----------------------------------
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])


----------------------------------------------------------
def compound_dictionary():
    elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
                'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
    elements["hydrogen"]["is_noble_gas"]=False
    elements["helium"]["is_noble_gas"]=True

    # todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
    # hint: helium is a noble gas, hydrogen isn't

    print(elements["hydrogen"]["is_noble_gas"])
    print(elements["helium"]["is_noble_gas"])

-------------------------------------------------------------
def count_unique_words():
    verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
    print(verse, '\n')

    # split verse into list of words
    verse_list = list(verse.split(" "))

    print(verse_list, '\n')

    # convert list to a data structure that stores unique elements
    verse_set = set(verse_list)
    print(verse_set, '\n')

    # print the number of unique words
    num_unique = len(verse_set)-1
    print(num_unique, '\n')
