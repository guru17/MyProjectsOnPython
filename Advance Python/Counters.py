from collections import Counter

'''
Return no of letters count in given string 
'''
def count_no_of_letters(ipString):
    return Counter(ipString)


'''
Return no of word count in given string
'''
def count_no_of_words(ipString):
    words = ipString.split()
    return Counter(words)

'''
Return no of number count in given list
'''
def count_no_of_numbers(ipList):
    return Counter(ipList)
