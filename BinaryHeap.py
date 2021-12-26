class MinHeap:
    def __init__(self, capacity):
        self.arr = [0] * capacity
        self.capacity = capacity
        self.curEmptyIndex = 0
    
    def findParent(self, index):
        parentIndex = (index - 1) // 2
        return parentIndex >= 0, parentIndex
    
    def findLchild(self, index):
        childIndex = 2 * index + 1
        return childIndex <= self.curEmptyIndex - 2, childIndex

    def findRchild(self, index):
        childIndex = 2 * index + 2
        return childIndex <= self.curEmptyIndex - 2, childIndex

    def swap(self, index1, index2):
        temp = self.arr[index1]
        self.arr[index1] = self.arr[index2]
        self.arr[index2] = temp
    
    def heapIfyUp(self, index):
        curIndex = index
        hasParentTrue = self.findParent(curIndex)[0]
        
        if hasParentTrue == True:
            if self.arr[self.findParent(curIndex)[1]] > self.arr[curIndex]:
                self.swap(self.findParent(curIndex)[1], curIndex)
                curIndex = self.findParent(curIndex)[1]
                self.heapIfyUp(curIndex)

    def heapIfyDown(self, index):
        curIndex = index

        if self.findLchild(curIndex)[0] == True:
            indexToSwap = self.findLchild(index)[1]
            hasRchildTrue = self.findRchild(curIndex)[0]   

            if hasRchildTrue == True:
                if self.arr[self.findRchild(curIndex)[1]] < self.arr[self.findLchild(curIndex)[1]]:
                        indexToSwap = self.findRchild(index)[1]
            
            if self.arr[curIndex] > self.arr[indexToSwap]:
                self.swap(curIndex, indexToSwap)
                self.heapIfyDown(indexToSwap)


    def insert(self, value):
        if self.curEmptyIndex >= self.capacity:
            return print("arr is full, no data added")
        
        self.arr[self.curEmptyIndex] = value
        self.heapIfyUp(self.curEmptyIndex)
        self.curEmptyIndex += 1

    def delete(self):
        if self.curEmptyIndex <= 0:
            return print("arr is empty, no data deleted")
        
        self.swap(0, self.curEmptyIndex - 1)
        self.arr[self.curEmptyIndex - 1] = 0
        self.heapIfyDown(0)
        self.curEmptyIndex -= 1