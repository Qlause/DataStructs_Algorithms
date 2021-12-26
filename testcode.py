# %%
def findOdd(num):
    if num == 1: return 1
    
    value = findOdd(num - 1) + 1
    if value % 2 == 0:
        print(value)
    return value
    
findOdd(20)
# %%
