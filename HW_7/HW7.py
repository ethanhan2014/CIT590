#HW_7
#Ziyi Han

import csv

def sameAB(abstring):
    '''recursively check to see if an input string is of the form aa...bb...'''
    if abstring =='':
        return True
    elif abstring[0] =='a' and abstring[-1] == 'b':
        return sameAB(abstring[1:-1])
    else:
        return False

def flatten(lst_of_lst):
    '''recursively flatten a list which contains a collection of lists'''
    flat_lst = []
    for item in lst_of_lst:
        if type(item) is list:
            flat_lst += flatten(item)
        else:
            flat_lst.append(item)
    return flat_lst

def binary_search(lst,val):
    '''this returns true of false depending upon whether the value is in
        the list lst. Assume integer list in ascending order.'''
    if lst == []:
        return False
    if val == lst[len(lst)/2]:
        return True
    else:
        if val > lst[len(lst)/2]:
            return binary_search(lst[len(lst)/2+1:],val)
        elif val < lst[len(lst)/2]:
            return binary_search(lst[:len(lst)/2],val)

def most_frequent_alphabet(frequency_dictionary):
    '''Given a frequency dictionary returns the alphabets that appear the most times'''
    return [alphabet for alphabet, time in frequency_dictionary.items() if time == max(frequency_dictionary.values())]

def meamers(filename):
    '''returns the number of MEAM student'''
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        return len([line[0] for line in reader if line[1]=='MEAM'])

def initials(lst):
    '''Given a name list, returns the initials of each name'''
    return [name.split()[0][0]+'.'+name.split()[1][0]+'.' for name in lst]
