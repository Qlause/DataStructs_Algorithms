from types import new_class
from typing import NewType


def canSum(Target, numbers):
    Arr = [None] * (Target + 1)
    Arr[0] = []
    for i in range(0, len(Arr)):
        if Arr[i] != None:
            for value in numbers:
                if value + i < len(Arr):
                    NewArr = [i for i in Arr[i]]
                    NewArr.append(value)
                    if Arr[value + i] != None:
                        if len(Arr[value + i]) > len(NewArr):
                            Arr[value + i] = NewArr
                    else:
                        Arr[value + i] = NewArr
    
    return Arr

canSum(5, [1,2,3])
    