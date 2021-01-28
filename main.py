"""
Find the Rank
If we generate a list of all “words” made of letters G, I, N, R, T, and U in lexicographic order starting with GINRTU
and ending with UTRNIG, what position in the list will be occupied by TURING?(Alan Turing was an English mathematician
and computer scientist who, among other remarkable achievements, played a leading role in developing theoretical computer science.)

"""
import re

def findingPosition(words, position):
    reverse_word  =  words[::-1]
    lenword = len(words)
    factor = 1
    count = 1
    array = []
    while(count<lenword) :
        array.append(factor)
        count += 1
        factor = factor * count

    count = count-2
    num_of_position = factor
    while(count >= 0) :
        for i in position :
            for j in reverse_word :

                if(i==j) :
                    reverse_word = re.sub(i,"",reverse_word)
                    position =  re.sub(i,"",position)
                    break
                else :
                    num_of_position = num_of_position - array[count]
            count = count - 1
            break

    return num_of_position

def checkrepeat(words):
    '''Returns True if words has no repeating characters; False otherwise.'''
    return sorted(''.join(set(words))) == sorted(words)

def checkEqual(words , find_pst ) :
    '''Returns True if words and find_pst have the same characters'''
    return sorted(words) == sorted(find_pst)

 # returns true when its in lexicographic order (dictionary order)
def lexicographicOrder(words)  :
    if words.isalpha(): #check if string is alphabetic or not 
        return all([c<d for c,d in zip(words,words[1:])]) 
    return False

words  =  input("enter the word : ")

find_pst = input("enter the which position u have to find :")

if(len(words) == len(find_pst)  and checkEqual(words , find_pst)  and checkrepeat(words) and lexicographicOrder(words)) :
    Position = findingPosition(words , find_pst)
    print(Position)
else :
    print("your position is wrong")
