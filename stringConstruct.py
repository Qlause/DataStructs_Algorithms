from typing import Counter


def canContruct(string, bankword):
    if string == "": return [[]]
    count = None
    
    for i in bankword:
        if string[0] == i[0] and i in string:
            newString = string[len(i):]
            result = canContruct(newString, bankword)
            
            for x in range(0, len(result)):
                result[x].insert(0, i)
                
            if result != None:
                if count != None:
                    for x in range(0, len(result)):
                        count.insert(0, result[x])
                else:
                    count = result
                
    return count

canContruct("ardi", ["ar","di","a","i","rd","r","d"])