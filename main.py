def checkvalue(word , word1) :
    check = True 
    for i in range(len(word)) :
        for j in range(len(word1)):
            if(word[i] == word[j]) :
                chk = True 
                break
            else:
                chk = False
        if(not chk) :
            break
    return chk
word = input("Enter the Word : ").upper()
findposition = input("Enter the other word :  ").upper()

arr = [0]*len(word)
top = 0


def push(s , top):
    arr[top] = s
    top += 1

def pop(s ,findposition ,top , c ) :
    ck = False
    if(top == 0) :
        push(s , top)
        return ck 
    for i in range(top) :
        if(arr[i] == findposition ):
            ck = True
            top -= 1
    if(not ck):
        push(s , top)
    return ck

if(len(word) == len(findposition) and checkvalue(word , findposition) ) :
    factor =  1
    factorial_list = [1]*(len(word)+1)
    for i  in range( 1 , len(word)+1) :
        factor *=  i
        factorial_list[i] = factor 
    i = 0
    c = 0 
    j = len(word)
    cnt = 0 
    for s in word[::-1] :
        if(s != findposition[i]) :
            if(pop(s , findposition[i]  , top , c)):
              cnt += factorial_list[j]
              top -= 1
            else :
              top += 1
            c += 1
        i += 1
        j -= 1
    print(factor - cnt)