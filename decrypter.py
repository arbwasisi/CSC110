# Author: Arsene Bwasisi
# Description: decrypter.py will take in an encrypted file as input along
#              with a key file containing the index of the file, and it will
#              organize the file into its original order and write it to
#              decrypter.txt.

def read_file(text_file, index_file):
    ''' This functions will open and read the inputed files.'''
    
    text_file = open(text_file, 'r')
    index_file = open(index_file, 'r')
    
    # Organize the data in both files into two seperate lists
    texts = text_file.readlines()
    indexes = []
    
    for index in index_file:
        indexes.append(int(index))
    
    return texts, indexes

def decrypter(file_list, index_list):
    ''' 
    This function will organize the encrypted file back to its 
    original format.
    '''
    
    decrypted_list = []
    
    # Sets a range similar to index_list
    for num in range(1, len(file_list) + 1):
        for index in range(len(index_list)): # loop through index_list

            # check whether value in index_list equals to num value
            # then append to decrypted_list.
            if num == index_list[index]:
                decrypted_list.append(file_list[index])
            
    return decrypted_list

def write_to_file(decrypted_list):
    ''' This functions writes in the orginal form of the file into decrypted.txt.'''
    
    decrypted_file = open('decrypted.txt', 'w') # open file in write mode
    
    # Iterate through and write content grom decrypted_list
    # into decrypted_file
    for line in decrypted_list:
        decrypted_file.write(line)
        
    decrypted_file.close() # close file

def main():
    
    encrypted_file = input("Enter the name of a mixed text file:\n")
    index_file = input("Enter the mix index file:\n")
    
    text_list, index_list = read_file(encrypted_file, index_file)
    decrypted_list = decrypter(text_list, index_list)
    write_to_file(decrypted_list)

main()