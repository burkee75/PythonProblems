import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":
def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust

# Problem 2
def is_ascending(items):
    # how I would have really done it
    # check if list is empty, if it is thats True
    if not items:
        return True

    # compare items in the list
    is_true = True
    for i in range(len(items) - 1):
        if items[i] >= items[i+1]:
            return False
    return is_true

    # answers from stackexchange
    # return all(x<y for x, y in zip(items, items[1:]))
        
# Problem #3
def riffle(items, out=True):
    '''
    Given a list of items whose length is guaranteed to be even (note that “oddly” enough, zero is an
    even number), create and return a list produced by performing a perfect riffle to the items by in-
    terleaving the items of the two halves of the list in an alternating fashion.

    Ex:
    Input: [1, 2, 3, 4, 5, 6, 7, 8] 
    Result after Riffle: [1, 5, 2, 6, 3, 7, 4, 8]
    '''
    first_half = items[:len(items)//2]
    second_half = items[len(items)//2:]
    riffle_list = []
    # Out shuffle:
    if out == True:
        for i in range(len(items)//2):
            riffle_list.append(first_half[i])
            riffle_list.append(second_half[i])
    # In Shuffle:
    else:
         for i in range(len(items)//2):
            riffle_list.append(second_half[i])
            riffle_list.append(first_half[i])
       

    
    #round = 1
    #for i in range(len(items) -1): # range is 0, 7
    #    logging.debug(f"Round: {round}")
    #    logging.debug(f"i = {i}")
    #    logging.debug(f"Appending {items[i]}")
    #    riffle_list.append(items[i])
    #    riffle_i = int(len(items)/2 + round)
    #    logging.debug(f"riffle_i = {riffle_i}")
    #    riffle_list.append(items[riffle_i])
    #    round = round + 1
    return riffle_list 


# Problem 4: Even the Odds
def only_odd_digits(n):
    '''
    Check that the given positive integer n contains only odd digits (1, 3, 5, 7 and 9) when it is written out. 
    Return True if this is the case, and False otherwise. 
    Note that this question is not asking whether the number n itself is odd or even. 
    You therefore will have to look at every digit of the given number before you can proclaim that the number contains no even digits.
    '''

    numbers_list = []
    for i in str(n):
        numbers_list.append(int(i))
    
    return all(i % 2 != 0 for i in numbers_list)
            

if __name__ == '__main__':
    # personal test cases here
    exit()
