# Author: Arsene Bwasisi
# Description: This program will read in a text file and produce an
#              infographic based on the file. The program will create
#              a dictionary containing all unique words and the number
#              of time they appear. This will be used to create a chart
#              of the number of small words, medium words, and large words.

from graphics import graphics

def process_file(file):
    ''' 
    This functions will read in a file and return a dictionary with
    a count of unique words.
    file: Inputed file
    '''
    
    read_file = open(file, 'r')
    count_word = dict()
    
    # loop though read_file and split each line
    # intp a list
    for line in read_file:
        if line != '\n':
            line = line.strip('\n')
            split_line = line.split()
            
            # track the number of time each word in
            # split_line appears
            for word in split_line:
                if word not in count_word:
                    count_word[word] = 0
                count_word[word] += 1
                
    return count_word
    
def words_list(dictionary):
    ''' 
    This function will return a list of all small, medium, and large words.
    dictionary: Word count dictionary
    '''
    
    small = list()
    medium = list()
    large = list()
    
    for word in dictionary.keys():
        if len(word) <= 4: # word is small if word is <= 4
            small.append(word)
        elif len(word) <= 7: # word is medium if word > 4 but <= 7
            medium.append(word)
        else: # word is large if word is >= 8
            large.append(word)
    
    return small, medium, large
    
def most_words(dictionary, small, medium, large):
    '''
    This function will return the word with the most appearance
    in each category.
    dictionary: Word count dictionary
    small: List of all small words
    medium: List of all medium words
    large: List of all large words
    '''
    
    # Compare each word in the list to find the one with 
    # most appearance
    for index in range(0, len(small)):
        if index > 0: # if it is first word, set it as the most appeared
            if dictionary[small[index]] > dictionary[small_word]:
                small_word = small[index]
        else:
            small_word = small[index]
        
    for index in range(0, len(medium)):
        if index > 0:
            if dictionary[medium[index]] > dictionary[medium_word]:
                medium_word = medium[index]
        else:
            medium_word = medium[index]
                
    for index in range(0, len(large)):
        if index > 0:
            if dictionary[large[index]] > dictionary[large_word]:
                large_word = large[index]
        else:
            large_word = large[index]
    
    return small_word, medium_word, large_word

def check_cap(dictionary):
    ''' 
    This function returns the number of words with and without capitalization.
    dictionary: Word count dictionary
    '''
    
    cap = 0
    no_cap = 0
    
    for word in dictionary.keys():
        if word[0].isupper():
            cap += 1 # add one for every word with capitalization
        else:
            no_cap += 1
        
    return cap, no_cap
    
def check_punc(dictionary):
    '''
    This function returns the number of words with and without punctuation.
    dictionary: Word count dictionary
    '''
    
    punctuation = [',', '.', '?', '!']
    punc = 0
    no_punc = 0
    
    for word in dictionary.keys():
        if word[-1] in punctuation:
            punc += 1
        else:
            no_punc += 1
            
    return punc, no_punc
    
def word_chart(gui, dictionary, small, medium, large):
    ''' 
    This function will use graphics to display a chart based on the 
    number of small words, medium words, and large words.
    gui: the grphics canvas
    dictionary: Word count dictionary
    small: List of all small words
    medium: List of all medium words
    large: List of all large words
    '''
    
    # Algorithm for charts:
    # (pixel_height / total_item_count) * category_item_count
    small_chart = (450/len(dictionary))*len(small)
    medium_chart = (450/len(dictionary))*len(medium)
    large_chart = (450/len(dictionary))*len(large)
    
    gui.text(25, 145, 'Word lengths', 'white', 20)
    gui.rectangle(25, 175, 125, int(small_chart), 'dodger blue')
    gui.rectangle(25, 175+int(small_chart), 125, int(medium_chart), 'green4')
    gui.rectangle(25, 175+int(small_chart)+int(medium_chart), 125, int(large_chart), 'dodger blue')
    
    gui.text(30, 180, 'small words', 'white', 10)
    gui.text(30, 180+int(small_chart), 'medium words', 'white', 10)
    gui.text(30, 180+int(small_chart)+int(medium_chart), 'large words', 'white', 10)
    
def cap_chart(gui, dictionary, cap, no_cap):
    ''' 
    This function will base a chart on the number of capitalized and
    non capitalized words.
    gui: the grphics canvas
    dictionary: Word count dictionary
    cap: Number of capitalized words
    no_cap: Number of non capitalized words
    '''
    
    cap_chart = (450/len(dictionary))*cap
    no_cap_chart = (450/len(dictionary))*no_cap
   
    gui.text(225, 145, 'Cap/Non-chart', 'white', 20)
    gui.rectangle(225, 175, 125, int(cap_chart), 'dodger blue')
    gui.rectangle(225, 175+int(cap_chart), 125, int(no_cap_chart), 'green4')
    
    gui.text(230, 180, 'Capitalized', 'white', 10)
    gui.text(230, 180+int(cap_chart), 'Non Capitalized', 'white', 10)
    
def punc_chart(gui, dictionary, punc, no_punc):
    ''' 
    This function will base a chart on the number of punctuated and
    non punctuated words.
    gui: the grphics canvas
    dictionary: Word count dictionary
    punc: Number of punctuated words
    no_punc: Number of non punctuated words
    '''
    
    punc_chart = (450/len(dictionary))*punc
    no_punc_chart = (450/len(dictionary))*no_punc
   
    gui.text(425, 145, 'Punct/Non-Punct', 'white', 20)
    gui.rectangle(425, 175, 125, int(punc_chart), 'dodger blue')
    gui.rectangle(425, 175+int(punc_chart), 125, int(no_punc_chart), 'green4')
    
    gui.text(430, 180, 'Punctuated', 'white', 10)
    gui.text(430, 180+int(punc_chart), 'Non Punctuated', 'white', 10)
    
def main():
    
    input_file = input('Input file:\n')
    
    dic = process_file(input_file)
    small, medium, large = words_list(dic)
    s_word, m_word, l_word= most_words(dic, small, medium, large)
    cap, no_cap = check_cap(dic)
    punc, no_punc = check_punc(dic)
    
    # display the canvas, and the data on the file:
    # most small, medium, and large words
    gui = graphics(650, 700, 'infographic')
    gui.rectangle(-10, -10, 800, 800, 'gray24')# background
    gui.text(25, 25, input_file, 'cyan', 22)
    gui.text(25, 75, 'Total Unique Words: '+ str(len(dic)), 'white', 18)
    gui.text(25, 115, 'Most used words (s/m/l):', 'white', 15)
    gui.text(190, 115, s_word + ' (' + str(dic[s_word]) + 'x) ' + m_word +\
    ' (' + str(dic[m_word]) + 'x) ' + l_word + ' (' + str(dic[l_word]) + 'x)', 'cyan', 15)
    
    # display all three chart
    word_chart(gui, dic, small, medium, large)
    cap_chart(gui, dic, cap, no_cap)
    punc_chart(gui, dic, punc, no_punc)
    
main()