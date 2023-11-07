# LinkedList class
# I have given you the basic structure of the class. ok
# TO DO: Complete the methods that have "pass" in their places kk
# and add comments for each method - 1 or 2 lines saying what it does ok
# Then test it using the LL_Tester file before doing the assignment ok
# YOUR NAME: SARA 

from Node import Node

class LinkedList:
    def __init__(self):
        self._head = Node()
        self._tail = Node()
        self._curr = Node()
    
    #changes or returns where the pointers are pointing
    #we use these instead of normal getters/setters so folks don't mess with our pointers
    # here = a Node object
    def setHead(self, here):
        self._head.link = here
    def getHead(self):
        return self._head.link
    def setTail(self, here):
        self._tail.link = here
    def getTail(self):
        return self._tail.link
    def setCurr(self, here):
        self._curr.link = here
    def getCurr(self):
        return self._curr.link
    
    def isEmpty(self):
        if self.getHead() == None:
            return True
        return False
    
    def isBeginning(self): #checks if a node is the first node in the linked list
        if self.getHead():
            return(self.getHead() == self.getCurr())
        #pass
    
    def isEnd(self): #checks if the node is that last node in the list
        return(self.getCurr() == self.getTail())
        #pass
    
    def goBeginning(self): #naviages to the head (which points to the first real node)
        (self.setCurr(self.getHead()))
        #pass
    
    def goEnd(self): #goes to last node in list
        (self.setCurr(self.getTail()))
        #pass
        
    def getSize(self): #returns how many items are in the linked list
        h = self.goBeginning()
        count = 0
        if self.isEmpty():
            return count
        else:
            while not self.isEnd():
                count+=1
                self.goNext()
            count += 1
            return count

    
    def getPos(self): #finds what the position is of cur
        #returns the current position as a number
        if self.isEmpty():
            return -1
        elif self.getHead() == self.getCurr():
            return 0
        temp = self.getHead()
        pos = 0
        while temp != self.getCurr():
            pos += 1
            temp = temp.link
        return pos
    
    def setPos(self, pos): #navigates pos in ll to pos parameter
        p = 0 
        self.goBeginning()
        while p<pos:
            self.goNext()
            p+=1
                
    def goNext(self): #navigates the the next node in the linked list
        if self.isEnd() == False and self.isEmpty() == False:
            #print("inny")
            self.setCurr(self.getCurr().link)
        #pass
    
    def goPrev(self): #navigates to the previous node in the linked list
        x = self.getPos()
        dest = x-1
        if not self.isBeginning() and not self.isEmpty():
            self.setPos(dest)
        
        
    def getData(self): #gets data from the specified node

        toRet = self.getCurr().data
        return(toRet)
        #pass
    
    def setData(self, d): #sets data in the specified node
        self.getCurr().data = d

    
    def insert(self, n):
        #inserts a new node, n, after the curr.link node
        oldLink = self.getCurr()
        self.setCurr(n)
        n.link = oldLink
        #pass
            
    def append(self, n):
        #inserts at the end of the list
        if self.getTail() != None:
            prevNode = self.getTail()
            self.setTail(n)
            prevNode.link = n
        else:
            self.setTail(n)
            self.setHead(n)
        self.setCurr(n)

            
    def insertBefore(self, n): #add a node before curr
        if self.isEmpty():
            self.setHead(n)
            self.setTail(n)
            self.setCurr(n)
            #print("1")
        elif self.isBeginning():
            self.setHead(n)
            n.link = self.getCurr()
            self.setCurr(n)
            #print("2")
        else:
            self.goPrev()
            self.insert(n)
            '''
        else: #i want to point to the curr, i want whats before curr to point to me
            print("3")
            n.link = self.getCurr()
            self.setCurr(n)
            '''
    

    def remove(self): #kill
        #removes the node at curr
        if self.isBeginning():
            self.setHead(self.getCurr().link)
        elif self.isEnd():
            self.goPrev()
            self.setTail(self._curr)
            self.getCurr().link = None
        elif not self.isEmpty():
            self.goPrev()
            self.getCurr().link = self.getCurr().link.link
        #self.setCurr(self.getCurr().link.link)
        #pass
    
    def copy(self): #control c
        #copies the list and returns a new list
        self.setCurr(self._head.link)
        temp = LinkedList()
        while self._curr.link != None:
            n = Node(self._curr.link.data)
            temp.append(n)
            self.setCurr(self._curr.link.link)
        return temp
    
    def __str__(self):
        self.setCurr(self._head.link)
        s = ""
        while self._curr.link != None:
            s += str(self._curr.link.data)
            s += "  "
            self.setCurr(self._curr.link.link)
        return s
