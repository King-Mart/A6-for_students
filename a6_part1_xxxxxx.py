import string

def open_file() :
    '''None->file object
    See the assignment text for what this function should do'''
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

def lineParser(line : str) -> list[str]:
    resultLine : list[str] = []
    currentword = ''
    index = 0
    lenght = 0
    while index <  len(line):
        if line[index] == " ":
            if lenght >= 2 : resultLine.append(currentword); 
            currentword = ""; lenght = 0

        elif line[index] in string.punctuation: pass
        elif line[index] in "'-.": pass
        elif not str.isalpha(line[index]):
            print(f"THis cuased me a hiccup : {line[index]}")
            currentword = ''
            while index < len(line) :
                if line[index] != " ": break
                index += 1
        else: currentword += line[index]; lenght += 1
        index +=1
    print(f"curr word :{currentword}")
    if lenght >= 2 : resultLine.append(currentword)
    return resultLine
    
def read_file(fp : object):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    occurenceMap = {}
    for index, line in enumerate(fp):
        for word in lineParser(line):
            print(word)
            resultSet = occurenceMap.setdefault(word, set())
            resultSet.add(index + 1)
            # print(resultSet)
        print(line)
        print(lineParser(line))

def find_coexistance(D, query):
    '''(dict[str, set[int],str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    pass
    

##############################
# main
##############################
file=open_file()
d=read_file(file)
query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

# YOUR CODE GOES HERE

