
from typing import Mapping


islandMap = [["W","L","W","L","L"],
             ["L","L","W","W","L"],
             ["W","W","W","L","W"],
             ["W","L","L","W","W"],
             ["W","L","L","W","W"]]


def up(map, row, col):
    if row > 0:
        return map[row - 1][col]
    else: return None

def down(map, row, col):
    if row < len(map) - 1:
        return map[row + 1][col]
    else: return None

def left(map, row, col):
    if col > 0:
        return map[row][col - 1]
    else: return None

def right(map, row, col):
    if col < len(map[row]) - 1:
        return map[row][col + 1]
    else: return None
    
    
def dfs(map, traversed, row, col, count, mapping):
    traversed.append((row, col))
    mapping[count].insert(0, (row, col))
    if up(map, row, col) == "L" and (row - 1, col) not in traversed:
        dfs(map, traversed, row - 1, col, count, mapping)
        
        
    if down(map, row, col) == "L" and (row + 1, col) not in traversed:
        dfs(map, traversed, row + 1, col, count, mapping)
        
        
    if left(map, row, col) == "L" and (row, col - 1) not in traversed:
        dfs(map, traversed, row, col - 1, count, mapping)
        
        
    if right(map, row, col) == "L" and (row, col + 2) not in traversed:
        dfs(map, traversed, row, col + 1, count, mapping)
        


traversed = []
mapping = []
count = 0
for row in range(len(islandMap)):
    for col in range(len(islandMap[row])):
        if islandMap[row][col] == "L" and (row, col) not in traversed:
            mapping.append([])
            dfs(islandMap, traversed, row, col, count, mapping)
            count += 1
            
    
print(mapping)