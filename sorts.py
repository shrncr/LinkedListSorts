from LinkedList import LinkedList
from Node import Node
'''
file w sorting algs for linked list (quick, merge, opt bubble, and insert)
'''

def QuickSort(ll,first,last): #im not even going to lie i realized my quick sort wasnt working for certain lists so i redid it with partitioning instead of creating new linked lists... i did in fact take inspiration from like 3 different websites. they all had pretty much the same code.
    if first == last: #if theres no more sorting left
        return ll.getHead()
    piv = scoot(first,last) #scoot ll around
    if piv!=None and piv.link!=None: #if theres still after piv post-scoot
        QuickSort(ll,piv.link,last) #sort the larger half of the list
    if piv!=None and first!=piv:#if theres still stuff to be sorted before piv post-scoot
        QuickSort(ll,first,piv) #sort smaller half of list
def scoot(first,last): #moves nodes before or after pivot depending on their val
    piv = first
    front = first
    #everything smaller than last will be before piv and everything larger will go after piv
    while front!=last:
        if front.data<last.data: #only need to check one case and move one case bc the rest will just stay on the opposite side when not moved!
            piv=first
            temp=first.data  
            first.data = front.data
            front.data = temp
            
            first = first.link
        front = front.link
        
    temp = first.data
    first.data = last.data
    last.data = temp 
    return piv #returns the in between val

def merge(ll):
    size = ll.getSize()
    if ll.getSize() == 1: #base case
        return ll
    half1 = ll.copy() #first half
    half2 = ll.copy() #second half
    half1.setPos(size//2 - 1)
    half1.getCurr().link = None
    half1.setTail(half1.getCurr()) #makes it first half by cutting off the tail and killing the link
    half2.setPos(size//2)
    half2.setHead(half2.getCurr()) #makes it second half by switching the head

    #keep merging halves til left w base case
    ll1 = merge(half1) 
    ll2 = merge(half2)
    return(mergeAction(ll1,ll2)) #all the merges get popped, so once at base case we will actually merge and sort baby linked lists into big linked list and return

def mergeAction(l1,l2):
    fin = LinkedList()
    while not l1.isEmpty() and not l2.isEmpty():  #when you get into ifs youre gonna remove til ll are both empty
        l1.setPos(0) #first item always gonna be smallest,
        l2.setPos(0)
        data1 = l1.getData()
        data2 = l2.getData()
        if data1 < data2:
            fin.append(Node(data1))  #so if top item from first list is smaller then append it to end
            l1.remove()
        else: 
            fin.append(Node(data2))  #so if top item from bottom list is smaller then append it to end
            l2.remove() 
    #once one of the lists is dead we can populate our "fin" list with the remaining items from the other list
    while not l1.isEmpty():
        l1.setPos(0)
        item = l1.getData()
        l1.remove()
        fin.append(Node(item))
    while not l2.isEmpty():
        l2.setPos(0)
        item = l2.getData()
        l2.remove()
        fin.append(Node(item))
    return fin

def InsertionSort(ll):
    ll = ll.copy()
    ll.goBeginning()
    for i in range(1, ll.getSize()):
        currentpos = i
        while currentpos > 0:
            ll.setPos(currentpos - 1)
            datab4 = ll.getData()
            ll.setPos(currentpos)
            data = ll.getData()
            if data < datab4: #swap.
                ll.setData(datab4)
                ll.goPrev()
                ll.setData(data)
            else:
                break
            currentpos -= 1
    return(ll)

def OptBubbleSort(ll):
    ll = ll.copy()
    for i in range(1,ll.getSize()):
        sorted = True #if i can iterate through the list without swaps i can quit the process
        for i in range(1,ll.getSize()):
            ll.setPos(i-1)
            datab4 = ll.getData()
            ll.setPos(i)
            data1 = ll.getData()
            if datab4 > data1: #NOT SORTED. MAKE A SWAP
                ll.setData(datab4)
                ll.goPrev()
                ll.setData(data1)
                sorted = False 
        if sorted:
            return(ll)
    return(ll)
        
