import string


minimalLenght : int = 2
def open_file() -> object:
    '''None->file object
    Prompts the user to type the name of a file to open.
    If the file does not exist, it keeps asking until a valid file name is entered.
    The file name has to have a .txt extension.
    The file is opened in utf-8 encoding. INstead of the device specific encoding
    '''
    # YOUR CODE GOES HERE
    validFileName : bool = False
    while not validFileName:
        try:
            toOpen = input("what file do you want to open? enter it's name : \n")
            if toOpen[-4:] != ".txt" : toOpen += ".txt"
            return open(toOpen, encoding="UTF-8")
        except: print("Invalid operation.")

#Tells you if a character is not a letter
def notalpha(char : str) -> bool:return not str.isalpha(char)

def lineParser(line : str, minimalLenght : int = minimalLenght) -> list[str]:
    '''(str)->list of str
    Takes a string, and breaks it up into a list of words. 
    A word is defined as a sequence of alphabetic characters.longer than a minimal value
    Non-alphabetic characters are ignored. This is case insensitive.
    args:
        line : A string of words to be broken up. 
    return:
        A list of the words., empty if the parameter is an empty string
    '''
    resultLine : list[str] = []; currentword = ''; index = 0
    while index <  len(line):
        if line[index] == " ":
            if len(currentword) >= minimalLenght : resultLine.append(currentword); 
            currentword = ""

        elif line[index] in string.punctuation: pass
        elif line[index] in "'-.\n": pass
        elif not line[index].isalpha():
            currentword = ''
            while index < len(line) :
                if line[index] == " ": break
                index += 1

        else: currentword += line[index].lower(); 
        index +=1
    if len(currentword) >= minimalLenght : resultLine.append(currentword)
    return resultLine
    
def read_file(fp : object):
    '''(file object)->dict
    Given a file pointer, read the file and return a dictionary of words to the lines they appear on.
    The keys in the dictionary are the words, and the values are sets of line numbers.
    The line numbers are 1-indexed; i.e. the first line is line 1.
    If a word appears on multiple lines, the set will contain all of those line numbers.
    If a word does not appear in the file, it will not be in the dictionary.
    The dictionary is case insensitive.
    '''
    # YOUR CODE GOES HERE
    occurenceMap = {}
    for index, line in enumerate(fp):
        for word in lineParser(line): resultSet = occurenceMap.setdefault(word, set()); resultSet.add(index + 1); occurenceMap[word] = resultSet
    return occurenceMap

def find_coexistance(D : dict[str, set[int]], query : str) -> list[int | str]:
    '''(dict[str, set[int],str)->list[int | str]
    Given a dictionary D of words in a file to the lines they appear on,
    and a query string, return a list of the line numbers of all the lines where ALL the words
    in the query appear. If a word in the query does not appear in the file,
    return a message indicating that the word was not found.
    If no line has all the words, return a message indicating that.
    '''
    # Parse the query string into a list of words
    parsedQuery = lineParser(query)
    if parsedQuery == []: parsedQuery = ['']
    intersect : set = D.get(parsedQuery[0], set())
    if intersect == set() : return [f"Word '{parsedQuery[0]}' not in file"]
    pointer = 1
    # loop through the rest of the words in the query
    while intersect and pointer < len(parsedQuery): # if the current word is in the dictionary, intersect with its line numbers
        if parsedQuery[pointer] in D : intersect = intersect.intersection(D[parsedQuery[pointer]]) # if the current word is not in the dictionary, return an appropriate message
        else : return [f"Word '{parsedQuery[pointer]}' not in file"] # if we have exhausted all the words in the query, and there is no intersection, return an appropriate message
        if intersect == set() : return [f"The one or more words you entered does not coexist in a same line of the file.\nCause : '{parsedQuery[pointer]}' not found on any of the lines where previous word where"]
        pointer += 1 
    return ["The one or more words you entered does not coexist in a same line of the file.\n"] + sorted(list(intersect)) # if we have exhausted all the words in the query, and there is an intersection, return the sorted list of line numbers



##############################
# main
##############################
file=open_file()
d=read_file(file)
query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

# YOUR CODE GOES HERE

while query != 'q':
    for response in find_coexistance(d, query):
        print(response, end= " ")
    query=input("\nEnter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

