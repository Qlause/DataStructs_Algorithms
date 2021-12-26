def howSum(targetsum, numbers, memo={}):
    if targetsum in memo:
        return memo[targetsum]
    if targetsum == 0:
        return []
    if targetsum < 0:
        return None
    
    shortestTarget = None
    
    for i in numbers:
        remainder = targetsum - i
        remainderCombination = howSum(remainder, numbers, memo)
        if remainderCombination != None:
            combination = [x for x in remainderCombination]
            combination.append(i)
            if shortestTarget == None or len(combination) < len(shortestTarget):
                shortestTarget = combination
    
    memo[targetsum] = shortestTarget            
    return shortestTarget

howSum(100, [1,2,5])
    
    