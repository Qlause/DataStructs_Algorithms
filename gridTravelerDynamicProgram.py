def gridTravel(x, y, memo={}, path=[False], preX=0, preY=0):
    matriks = f"{x},{y}"
    if preY != 0 and path[-1] == False:
        if preY > y:
            path.insert(-2,"kanan")
    if preX != 0 and path[-1] == False:    
        if preX > x:
            path.insert(-2,"bawah")
    if x <= 0 or y <= 0:
        if path[-1] == False:
            path.pop(-2)
        return 0, 0
    if matriks == "1,1":
        path[-1] = True
        return 1, 0
    if matriks in memo:
        return memo[matriks], 0
    
    memo[matriks] = gridTravel(x - 1, y, memo, path, preY=y, preX=y)[0] + gridTravel(x, y -1, memo, path, x, y)[0]
    
    return memo[matriks], path

print(gridTravel(5,5)) 