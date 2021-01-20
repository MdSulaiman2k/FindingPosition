"""
Find the Rank
If we generate a list of all “words” made of letters G, I, N, R, T, and U in lexicographic order starting with GINRTU
and ending with UTRNIG, what position in the list will be occupied by TURING?(Alan Turing was an English mathematician
and computer scientist who, among other remarkable achievements, played a leading role in developing theoretical computer science.)

"""
import re 

def  findingPosition(words , position)  :
    reverse_word  =  words[::-1]
    lenword = len(words)
    factor = 1
    count = 1
    array = []
    while(count<lenword) :
        array.append(factor)
        factor = factor * (count + 1)
        
        count = count+1

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
    
    


words  =  input("enter the word : ")
find_pst = input("enter the which position u have to find :")
found = True 
for i in words  :
    for j in find_pst :
        if(i == j ) :
            found = True
            break
        else :
            found = False
    if( not found ) :
        break 

if(len(words) == len(find_pst)  and found  ) :
    Position = findingPosition(words , find_pst)
    print(Position)
else :
    print("your position is wrong")
    
