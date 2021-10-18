# Author: Arsene Bwasisi
# Description: This program will take in an inputed file with
#              misspelled words and make correction. It will locate
#              the misspelled words and do one of two things,
#              either replace the words, or suggest the correct word.
#              This will depend on the mode(replace or suggest)

def read_file():
    '''
    This function will return a dictionary that maps misspelled
    words to correctly spelled words. 
    '''

    misspellings = {}

    misspelling_file = open('misspellings.txt', 'r')
    
    # Loop through each line in misspelling_file and 
    # split by each word into a list
    for line in misspelling_file:#['word_1', 'word_2 word_3...']
        split_line = line.strip('\n').split(':')
        misspelled = split_line.pop(1) #take last value 
        misspelled = misspelled.split(',')#split last value

        for word in misspelled:#['word_1', 'word_2', 'word_3',...]
            split_line.append(word)
        
        # Add the words in split_line in misspellings
        # First words is the value, the rest are key
        for index in range(1, len(split_line)):
            word = split_line[index]
            misspellings[word] = split_line[0]

    return misspellings

def check_punctuation(word):
    ''' 
    This function will determine if a word has a punctuation
    word: a word from the input_file
    '''
    
    punctuation = [',', '.', '?', '!']# a list of the puctuation
    
    if word is not '': # checks if word is not empty string
        if word[-1] in punctuation: # if last character in puctuation
            word = word[:-1]# get all characters but the last one
            return word, punctuation
            
    return word, punctuation

def add_punctuation(split_line, index, misspelled, punctuation):
    ''' 
    This function will add puctuation for the replace function.
    It checks if a word originally had a punctuation.
    split_line: The list containing a lines words
    index: The index at the current loop
    misspelled: The orignal word in the file(\n is stripped)
    punctuation: A list of punctuation
    '''
    
    if misspelled[-1] in punctuation: # if last character in puctuation
        character = misspelled[-1]
        split_line[index] += character # Add puctuation to word
            
    return split_line
    
def annotate(split_line, index, misspelled, punctuation, count):
    '''
    This funtion will annotate each line for the suggest function.
    it will add puctuation if necessary.
    split_line: The list containing a lines words
    index: The index at the current loop
    misspelled: The orignal word in the file(\n is stripped)
    punctuation: A list of punctuation
    count: Represents number of misspelled words
    '''
    
    # Add (i) to each misspelled word in split_line
    # Add punctuation before if necessary
    if misspelled[-1] in punctuation:
        character = misspelled[-1]
        split_line[index] += character + ' (' + str(count) + ')'
    else:
        split_line[index] += ' (' + str(count) + ')'
        
    return split_line

def convert(split_line, index, misspellings, word):
    '''
    This function will replace the misspelled with the correct
    word. It will capitalize word if necessary.
    split_line: The list containing a lines words
    index: The index at the current loop
    misspellings: Dictionay of misspelled words and correct words
    word: a word from the input_file
    '''
    
    # Check if first letter isupper(), then capitalize
    # based on the result
    # replace the value in split_line with the correct value
    misspelled = split_line[index].strip('\n')
    correction = misspellings[word]
    if misspelled[0].isupper():
        split_line[index] = correction.capitalize()
    else:
        split_line[index] = correction
            
    return split_line, misspelled
    
def capitalize(split_line, index, misspellings, word, correction):
    ''' 
    This function will capitalize misspelled words for the suggest
    function if necessary.
    split_line: The list containing a lines words
    index: The index at the current loop
    misspellings: Dictionay of misspelled words and correct words
    word: a word from the input_file
    correction: A list of the correct words
    '''
    
    misspelled = split_line[index].strip('\n')
    if misspelled[0].isupper():#check if orignal word was capitalized
        # Append to correction and correct misspelled word
        correction.append(misspellings[word].capitalize())
        split_line[index] = word.capitalize()#capitalize if true
    else:
        correction.append(misspellings[word])
        split_line[index] = word
        
    return correction, misspelled
    
def print_line(split_line, index):
    ''' 
    This prints the file content with the corrections.
    split_line: The list containing a lines words
    index: The index at the current loop
    '''
    
    if index == len(split_line)-1:
        if '\n' not in split_line[index]:
            split_line[index] += '\n'# add \n to last word in split_line

        print(split_line[index], end='')

    else:
        print(split_line[index] + ' ', end='')
    
def replace(input_file, misspellings):
    ''' 
    This function will run if mode is replace, it will replace
    all misspelled words with correctly spelled words.
    input_file: The inputed file to check
    misspellings: Dictionay of misspelled words and correct words
    '''

    file = open(input_file, 'r')
    print('\n--- OUTPUT ---')
    
    for line in file:
        split_line = line.split(' ')
        
        # Loop throuhg each line in file and check
        # if a word is in misspellings
        for index in range(0, len(split_line)):
            word = split_line[index].strip('\n').lower()
            word, punctuation = check_punctuation(word)
            if word in misspellings:
                
                # if word in misspellings, make changes to word
                split_line, misspelled = convert(split_line, index,\
                misspellings, word)
                split_line = add_punctuation(split_line, index,\
                misspelled, punctuation)
            
            print_line(split_line, index)
            
def suggest(input_file, misspellings):
    '''
    This function will run if mode is suggest, instead of replacing
    each misspelled word, it will annotate the words and suggest
    proper corrections.
    input_file: The inputed file to check
    misspellings: Dictionay of misspelled words and correct words
    '''

    file = open(input_file, 'r')
    count = 1 # keep track of number of misspelled words
    correction = [] # will contain all misspelled words
    print('\n--- OUTPUT ---')
    for line in file:
        split_line = line.split(' ')
        
        for index in range(0, len(split_line)):
            word = split_line[index].strip('\n').lower()
            word, punctuation = check_punctuation(word)
            if word in misspellings:
                correction, misspelled = capitalize(split_line, index,\
                misspellings, word, correction)
                split_line = annotate(split_line, index, misspelled,\
                punctuation, count)
                    
                count += 1
                
            print_line(split_line, index)
    
    # print the legend using the correction list
    print('\n--- LEGEND ---')
    count = 1
    for word in correction:
        print('(' + str(count) + ')', word)
        count += 1

def main():
    
    # Get input file and the mode of spellcheck
    in_file = input('Enter input file:\n')
    mode = input('Enter spellcheck mode (replace or suggest):\n')
    
    # Get the misspellings dictionary
    misspells = read_file()
    
    # Run one fuction(replace or suggest) depending on mode
    if mode == 'replace':
        replace(in_file, misspells)
    else:
        suggest(in_file, misspells)
        
main()