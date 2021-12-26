map = {
    "A":["B","C","D"],
    "B":["H","G"],
    "C":["A","E","F"],
    "D":["B","G"],
    "E":["B","C","I"],
    "F":["C","H"],
    "G":["D","I"],
    "H":["F","I","K"],
    "I":["G","E","H","J"],
    "J":["I"],
    "K":["H"],
}

class Queue:
    def __init__(self):
        self.arr = []
    
    def enqueue(self, value):
        self.arr.append(value)
    
    def dequeue(self) -> int:
        if len(self.arr) <= 0:
            raise("error")
        
        temp = self.arr[0]
        self.arr.pop(0)
        return temp


def djikstra(path, start, dest):
    
    myQue = Queue()
    myQue.enqueue(start)
    traversed = []
    hop = {f"{start}": {"route" : 0, "pred":[]}}
    predAdd = start
    
    while myQue.arr:
        predAdd = myQue.arr[0]
        for i in path[myQue.arr[0]]:
            if i not in hop:
                hop[f"{i}"] = {"route" : 0, "pred":[]}
                hop[i]["route"] = hop[myQue.arr[0]]["route"] + 1
                hop[i]["pred"] = hop[myQue.arr[0]]["pred"] + list(predAdd)
            else:
                if hop[i]["route"] > hop[myQue.arr[0]]["route"]:
                    hop[i]["route"] = hop[myQue.arr[0]]["route"] + 1
                    hop[i]["pred"] = hop[myQue.arr[0]]["pred"] + list(predAdd)

            if i not in myQue.arr and i not in traversed:
                myQue.enqueue(i)
        
        traversed.append(myQue.dequeue())
    
    if start in traversed and dest in traversed:
        return hop[dest] 
    else:
        return False
        
print(djikstra(map, start="A", dest="K"))